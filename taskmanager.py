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

def add_task(title, priority, due date):
    print(f"Adding task: {title} (Priority: {priority}, Due: {due_date})")
def complete_task(task_id):
    print(f"Completing task {task_id}")
def delete_task(task_id):
    print(f"Deleting task {task_id}")
def save_task():
    print("Tasks are auto-saved to local Json")
def search_tasks(query):
    print(f"searching for tasks matching: {query}")
def filter_tasks(criteria):
    print(f"Filtering tasks by {criteria}")
feature/search-filter
