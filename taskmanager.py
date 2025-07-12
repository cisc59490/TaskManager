@app.route('/search')
def search():
    query = request.args.get('q', '').lower()
    priority_filter = request.args.get('priority')
    
    tasks = load_tasks()
    
    # Apply filters
    if query:
        tasks = [t for t in tasks if query in t['title'].lower()]
    if priority_filter:
        tasks = [t for t in tasks if t['priority'] == priority_filter]
    
    return render_template('index.html', 
                         tasks=tasks,
                         search_query=query,
                         selected_priority=priority_filter)
