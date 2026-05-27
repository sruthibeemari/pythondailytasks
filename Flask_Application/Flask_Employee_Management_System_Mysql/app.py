from flask import Flask, render_template, request, redirect, flash, session, url_for, jsonify
from functools import wraps
import os
import requests

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "change-this-secret")

API_URL = "http://127.0.0.1:8000"


def format_inr(value):
    """Format a numeric amount in Indian Rupees (₹) with Indian digit grouping."""
    try:
        amount = float(value)
    except (ValueError, TypeError):
        if value is None or value == '':
            return '₹0'
        return f'₹{value}'

    sign = '-' if amount < 0 else ''
    amount = abs(amount)
    integer_part = int(amount)
    decimal_part = round(amount - integer_part, 2)

    digits = str(integer_part)
    if len(digits) > 3:
        last_three = digits[-3:]
        remaining = digits[:-3]
        groups = []
        while len(remaining) > 2:
            groups.insert(0, remaining[-2:])
            remaining = remaining[:-2]
        if remaining:
            groups.insert(0, remaining)
        formatted_int = ','.join(groups) + ',' + last_three
    else:
        formatted_int = digits

    if decimal_part:
        paise = int(round(decimal_part * 100))
        return f'{sign}₹{formatted_int}.{paise:02d}'
    return f'{sign}₹{formatted_int}'


app.jinja_env.filters['inr'] = format_inr

DEPARTMENTS = [
    {"id": 1, "name": "Engineering"},
    {"id": 2, "name": "Human Resources"},
    {"id": 3, "name": "Sales"},
    {"id": 4, "name": "Design"}
]

EMPLOYEE_ASSIGNMENTS = {}
EMPLOYEE_DESIGNATIONS = {}

VALID_USERS = {
    os.getenv('APP_USERNAME', 'admin'): {
        'password': os.getenv('APP_PASSWORD', 'admin123'),
        'role': 'admin'
    },
    os.getenv('HR_USERNAME', 'hr'): {
        'password': os.getenv('HR_PASSWORD', 'hr123'),
        'role': 'hr'
    },
    os.getenv('EMPLOYEE_USERNAME', 'employee'): {
        'password': os.getenv('EMPLOYEE_PASSWORD', 'employee123'),
        'role': 'employee'
    }
}

def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if not session.get('logged_in'):
            flash('Please log in to continue.', 'warning')
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return wrapped_view


def api_error_message(response):
    try:
        payload = response.json()
    except ValueError:
        return 'Something went wrong. Please try again.'

    detail = payload.get('detail', 'Something went wrong. Please try again.')
    if isinstance(detail, list):
        first = detail[0]
        if isinstance(first, dict):
            return first.get('msg', str(first))
        return str(first)
    return str(detail)


def get_next_employee_id():
    try:
        response = requests.get(f'{API_URL}/next_employee_id', timeout=5)
        if response.ok:
            return response.json().get('employee_id', 'EMP001')
    except requests.RequestException:
        pass
    return 'EMP001'


def enrich_employees(employees):
    for emp in employees:
        emp['department'] = EMPLOYEE_ASSIGNMENTS.get(emp['id'], 'Unassigned')
        emp['designation'] = EMPLOYEE_DESIGNATIONS.get(emp['id'], 'Staff')
        emp['status'] = 'Active'
        emp['attendance'] = 'Present' if emp['id'] % 2 == 0 else 'Absent'
    return employees


@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        user = VALID_USERS.get(username)
        if user and password == user['password']:
            session['logged_in'] = True
            session['username'] = username
            session['role'] = user['role']
            flash('Logged in successfully.', 'success')
            return redirect(url_for('index'))

        flash('Invalid username or password.', 'danger')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

# ---------------- DASHBOARD ---------------- #

@app.route('/')
@login_required
def index():
    employees = requests.get(f"{API_URL}/employees").json()

    return render_template(
        'index.html',
        employees=employees
    )

# ---------------- ADD EMPLOYEE ---------------- #

@app.route('/add_employee', methods=['GET', 'POST'])
@login_required
def add_employee():
    suggested_id = get_next_employee_id()

    if request.method == 'POST':
        employee_id = request.form.get('employee_id', '').strip()
        data = {
            'employee_id': employee_id,
            'name': request.form.get('name', '').strip(),
            'salary': request.form.get('salary', '').strip(),
            'email': request.form.get('email', '').strip(),
        }

        try:
            response = requests.post(f'{API_URL}/add_employee', json=data, timeout=5)
        except requests.RequestException:
            flash('Could not reach the employee service. Please try again.', 'danger')
            return render_template('add_employee.html', suggested_id=employee_id or suggested_id)

        if response.status_code == 400:
            flash(api_error_message(response), 'danger')
            return render_template('add_employee.html', suggested_id=employee_id or suggested_id)

        if not response.ok:
            flash(api_error_message(response), 'danger')
            return render_template('add_employee.html', suggested_id=employee_id or suggested_id)

        flash('Employee added successfully.', 'success')
        return redirect('/')

    return render_template('add_employee.html', suggested_id=suggested_id)

# ---------------- EDIT EMPLOYEE ---------------- #

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):

    employees = requests.get(f"{API_URL}/employees").json()

    employee = None

    for emp in employees:
        if emp['id'] == id:
            employee = emp

    if employee is None:
        flash("Employee not found.", "error")
        return redirect('/')

    if request.method == 'POST':
        data = {
            'employee_id': request.form.get('employee_id', '').strip(),
            'name': request.form.get('name', '').strip(),
            'salary': request.form.get('salary', '').strip(),
            'email': request.form.get('email', '').strip(),
        }

        try:
            response = requests.put(f'{API_URL}/edit_employee/{id}', json=data, timeout=5)
        except requests.RequestException:
            flash('Could not reach the employee service. Please try again.', 'danger')
            return render_template('edit_employee.html', employee=employee)

        if response.status_code == 400:
            flash(api_error_message(response), 'danger')
            return render_template('edit_employee.html', employee=employee)

        if not response.ok:
            flash(api_error_message(response), 'danger')
            return render_template('edit_employee.html', employee=employee)

        flash('Employee updated successfully.', 'success')
        return redirect('/')

    return render_template('edit_employee.html', employee=employee)

# ---------------- DELETE ---------------- #

@app.route('/delete/<int:id>')
@login_required
def delete(id):

    requests.delete(f"{API_URL}/delete_employee/{id}")
    flash("Employee deleted successfully.", "success")

    return redirect('/')

# ---------------- SEARCH ---------------- #

@app.route('/search', methods=['POST'])
@login_required
def search():

    name = request.form['name']

    employees = requests.get(
        f"{API_URL}/search_employee/{name}"
    ).json()

    return render_template(
        'index.html',
        employees=employees
    )

# ---------------- ATTENDANCE ---------------- #

@app.route('/attendance', methods=['GET', 'POST'])
@login_required
def attendance():

    if request.method == 'POST':
        data = {
            'employee_id': request.form.get('employee_id', '').strip(),
            'date': request.form.get('date', '').strip(),
            'status': request.form.get('status', 'Present').strip(),
        }

        try:
            response = requests.post(f'{API_URL}/mark_attendance', json=data, timeout=5)
        except requests.RequestException:
            flash('Could not reach the employee service. Please try again.', 'danger')
            return redirect('/attendance')

        if response.status_code == 400:
            flash(api_error_message(response), 'danger')
            return redirect('/attendance')

        if not response.ok:
            flash(api_error_message(response), 'danger')
            return redirect('/attendance')

        flash('Attendance recorded successfully.', 'success')
        return redirect('/attendance')

    attendance = requests.get(f'{API_URL}/attendance').json()

    return render_template(
        'attendance.html',
        attendance=attendance
    )

# ---------------- LEAVE ---------------- #

@app.route('/leave', methods=['GET', 'POST'])
@login_required
def leave():

    if request.method == 'POST':
        data = {
            'employee_id': request.form.get('employee_id', '').strip(),
            'leave_date': request.form.get('leave_date', '').strip(),
            'reason': request.form.get('reason', '').strip(),
        }

        try:
            response = requests.post(f'{API_URL}/apply_leave', json=data, timeout=5)
        except requests.RequestException:
            flash('Could not reach the employee service. Please try again.', 'danger')
            return redirect('/leave')

        if response.status_code == 400:
            flash(api_error_message(response), 'danger')
            return redirect('/leave')

        if not response.ok:
            flash(api_error_message(response), 'danger')
            return redirect('/leave')

        flash('Leave request submitted successfully.', 'success')
        return redirect('/leave')

    leaves = requests.get(f'{API_URL}/leave_requests').json()

    return render_template(
        'leave.html',
        leaves=leaves
    )


def update_leave_status(leave_id, status):
    try:
        response = requests.patch(
            f'{API_URL}/leave_requests/{leave_id}/status',
            json={'status': status},
            timeout=5,
        )
    except requests.RequestException:
        flash('Could not reach the employee service. Please try again.', 'danger')
        return redirect('/leave')

    if not response.ok:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({'error': api_error_message(response)}), 500
        flash(api_error_message(response), 'danger')
        return redirect('/leave')

    # Successful update: return JSON for AJAX requests, otherwise redirect.
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({'status': status, 'message': f'Leave request {status.lower()}.'})

    flash(f'Leave request {status.lower()}.', 'success')
    return redirect('/leave')


@app.route('/leave/<int:leave_id>/approve', methods=['POST'])
@login_required
def approve_leave(leave_id):
    return update_leave_status(leave_id, 'Approved')


@app.route('/leave/<int:leave_id>/reject', methods=['POST'])
@login_required
def reject_leave(leave_id):
    return update_leave_status(leave_id, 'Rejected')


@app.route('/employee/<int:id>')
@login_required
def employee_profile(id):
    employees = enrich_employees(requests.get(f"{API_URL}/employees").json())
    employee = next((emp for emp in employees if emp['id'] == id), None)

    if employee is None:
        flash('Employee not found.', 'error')
        return redirect(url_for('index'))

    return render_template('employee_profile.html', employee=employee)


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        flash('Profile updated successfully.', 'success')
        return redirect(url_for('profile'))

    return render_template(
        'profile.html',
        username=session.get('username', 'User'),
        role=session.get('role', 'employee')
    )


@app.route('/departments', methods=['GET', 'POST'])
@login_required
def departments():
    employees = enrich_employees(requests.get(f"{API_URL}/employees").json())

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add_department':
            name = request.form.get('department_name', '').strip()
            if name and not any(dep['name'].lower() == name.lower() for dep in DEPARTMENTS):
                DEPARTMENTS.append({'id': len(DEPARTMENTS) + 1, 'name': name})
                flash('Department added successfully.', 'success')
            else:
                flash('Department already exists or name is empty.', 'warning')
        elif action == 'assign_department':
            employee_id = int(request.form.get('employee_id', 0))
            department_name = request.form.get('department_name', '').strip()
            EMPLOYEE_ASSIGNMENTS[employee_id] = department_name
            flash('Employee assigned to department.', 'success')
        return redirect(url_for('departments'))

    return render_template(
        'departments.html',
        departments=DEPARTMENTS,
        employees=employees,
        assignments=EMPLOYEE_ASSIGNMENTS
    )


@app.route('/reports')
@login_required
def reports():
    employees = enrich_employees(requests.get(f"{API_URL}/employees").json())
    attendance = requests.get(f"{API_URL}/attendance").json()
    leaves = requests.get(f"{API_URL}/leave_requests").json()

    summary = {
        'total_employees': len(employees),
        'present_today': sum(1 for emp in employees if emp['attendance'] == 'Present'),
        'absent_today': sum(1 for emp in employees if emp['attendance'] == 'Absent'),
        'pending_leaves': len([
            leave for leave in leaves
            if leave.get('status', 'Pending') == 'Pending'
        ])
    }

    return render_template(
        'reports.html',
        summary=summary,
        employees=employees,
        attendance=attendance,
        leaves=leaves
    )


@app.route('/payroll')
@login_required
def payroll():
    employees = enrich_employees(requests.get(f"{API_URL}/employees").json())
    payrolls = []

    for emp in employees:
        salary_value = 0
        try:
            salary_value = float(emp['salary'])
        except (ValueError, TypeError):
            salary_value = 0

        monthly = salary_value / 12 if salary_value else 0
        payrolls.append({
            'id': emp['id'],
            'name': emp['name'],
            'employee_id': emp['employee_id'],
            'salary': format_inr(salary_value) if salary_value else format_inr(0),
            'monthly_pay': format_inr(monthly),
        })

    return render_template('payroll.html', payrolls=payrolls)


if __name__ == '__main__':
    app.run(debug=True)