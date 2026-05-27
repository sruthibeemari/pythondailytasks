# Flask Employee Management System

A simple employee management system with a Flask frontend and FastAPI backend.

## Features
- Employee dashboard
- Add / edit / delete employees
- Attendance tracking
- Leave request submission

## Setup
1. Create a Python virtual environment:

   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. Configure database connection if needed using environment variables:

   - `DB_USER`
   - `DB_PASSWORD`
   - `DB_HOST`
   - `DB_NAME`
   - `FLASK_SECRET_KEY`

4. Run the backend API:

   ```powershell
   uvicorn server:app --reload
   ```

5. Run the Flask frontend:

   ```powershell
   python app.py
   ```

## Notes
- The frontend calls the backend API at `http://127.0.0.1:8000`.
- Use `.gitignore` to keep virtual environments and local secrets out of version control.
