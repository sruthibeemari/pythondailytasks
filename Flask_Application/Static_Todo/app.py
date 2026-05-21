from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# -----------------------------------------
# Store Todos
# -----------------------------------------

todos = []

# -----------------------------------------
# Welcome Page
# -----------------------------------------

@app.route('/')
def welcome():
    return render_template('welcome.html')

# -----------------------------------------
# TODO Page
# -----------------------------------------

@app.route('/todo')
def home():
    return render_template('index.html', todos=todos)

# -----------------------------------------
# Add Todo
# -----------------------------------------

@app.route('/add', methods=['POST'])
def add():

    task = request.form['task']

    todos.append(task)

    return redirect('/todo')

# -----------------------------------------
# Delete Todo
# -----------------------------------------

@app.route('/delete/<int:index>')
def delete(index):

    todos.pop(index)

    return redirect('/todo')

# -----------------------------------------
# Open Update Page
# -----------------------------------------

@app.route('/update/<int:index>')
def update(index):

    task = todos[index]

    return render_template(
        'update.html',
        task=task,
        index=index
    )

# -----------------------------------------
# Save Updated Task
# -----------------------------------------

@app.route('/edit/<int:index>', methods=['POST'])
def edit(index):

    updated_task = request.form['task']

    todos[index] = updated_task

    return redirect('/todo')

# -----------------------------------------
# Run App
# -----------------------------------------

if __name__ == '__main__':
    app.run(debug=True)