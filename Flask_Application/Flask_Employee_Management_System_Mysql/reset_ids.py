"""
Reset SQL primary key `id` columns to start from 1.

Usage (from project folder, with venv active):
  python reset_ids.py --renumber     # Keep data; set employee ids to 1, 2, 3...
  python reset_ids.py --clear        # Delete ALL employees, attendance, leave; ids start at 1

Requires MySQL. Stop the API server first if you see lock errors.
"""

import argparse
import sys

from sqlalchemy import text

from database import SessionLocal, engine
from models import Attendance, Employee, LeaveRequest


def reset_auto_increment(table_name: str, next_value: int):
    with engine.connect() as conn:
        conn.execute(text(f"ALTER TABLE {table_name} AUTO_INCREMENT = :n"), {"n": next_value})
        conn.commit()


def renumber_table(session, table_name: str, model):
    rows = session.query(model).order_by(model.id).all()
    if not rows:
        reset_auto_increment(table_name, 1)
        return 0

    # Move to temporary negative ids to avoid primary-key clashes
    for index, row in enumerate(rows, start=1):
        session.execute(
            text(f"UPDATE {table_name} SET id = :new_id WHERE id = :old_id"),
            {"new_id": -index, "old_id": row.id},
        )
    session.commit()

    for index in range(1, len(rows) + 1):
        session.execute(
            text(f"UPDATE {table_name} SET id = :new_id WHERE id = :old_id"),
            {"new_id": index, "old_id": -index},
        )
    session.commit()

    reset_auto_increment(table_name, len(rows) + 1)
    return len(rows)


def clear_tables(session):
    session.query(Attendance).delete()
    session.query(LeaveRequest).delete()
    session.query(Employee).delete()
    session.commit()

    for table in ("attendance", "leave_requests", "employees"):
        reset_auto_increment(table, 1)


def main():
    parser = argparse.ArgumentParser(description="Reset SQL `id` primary keys to start from 1.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--renumber",
        action="store_true",
        help="Keep all rows; renumber id to 1, 2, 3... on employees, attendance, and leave_requests.",
    )
    group.add_argument(
        "--clear",
        action="store_true",
        help="Delete all rows in those tables; next id will be 1.",
    )
    args = parser.parse_args()

    session = SessionLocal()
    try:
        if args.clear:
            clear_tables(session)
            print("All employee, attendance, and leave records deleted.")
            print("SQL id counters reset. Next new row will use id = 1.")
            return

        emp_count = renumber_table(session, "employees", Employee)
        att_count = renumber_table(session, "attendance", Attendance)
        leave_count = renumber_table(session, "leave_requests", LeaveRequest)

        print(f"Renumbered {emp_count} employee(s), {att_count} attendance row(s), {leave_count} leave row(s).")
        print("SQL id columns now run from 1. Next new row gets the next number.")
    except Exception as exc:
        session.rollback()
        print(f"Error: {exc}", file=sys.stderr)
        print("Tip: stop uvicorn/Flask, then run this script again.", file=sys.stderr)
        sys.exit(1)
    finally:
        session.close()


if __name__ == "__main__":
    main()
