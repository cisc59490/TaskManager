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
