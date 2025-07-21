from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-123'
DATA_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE) as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

@app.route('/')
def home():
    return render_template('index.html', tasks=load_tasks())

@app.route('/add', methods=['POST'])
def add_task():
    tasks = load_tasks()
    tasks.append({
        'id': len(tasks) + 1,
        'title': request.form['title'],
        'priority': request.form.get('priority', 'medium'),
        'completed': False
    })
    save_tasks(tasks)
    return redirect(url_for('home'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
    save_tasks(tasks)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

HEAD
from datetime import datetime, timedelta

# Helper function to identify due-soon tasks
def get_due_soon_tasks(tasks):
    due_soon = []
    today = datetime.now().date()
    
    for task in tasks:
        if task.get('due_date'):
            due_date = datetime.strptime(task['due_date'], '%Y-%m-%d').date()
            if 0 <= (due_date - today).days <= 2:  # Due in 0-2 days
                due_soon.append(task)
    return due_soon

# Updated home route
@app.route('/')
def home():
    tasks = load_tasks()
    return render_template('index.html', 
                         tasks=tasks,
                         due_soon=get_due_soon_tasks(tasks))

