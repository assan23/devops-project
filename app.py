from flask import Flask, render_template_string, request, redirect, url_for, jsonify
from datetime import datetime
import json

app = Flask(__name__)

# Stockage des tâches en mémoire
tasks = []
task_id_counter = 1

# Template HTML avec CSS intégré
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestionnaire de Tâches - DevOps Todo</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }
        
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }
        
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        
        .header p {
            opacity: 0.9;
        }
        
        .add-task {
            padding: 30px;
            background: #f8f9fa;
            border-bottom: 1px solid #e0e0e0;
        }
        
        .add-task form {
            display: flex;
            gap: 10px;
        }
        
        .add-task input {
            flex: 1;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        
        .add-task input:focus {
            outline: none;
            border-color: #667eea;
        }
        
        .add-task button {
            padding: 12px 30px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
            transition: transform 0.2s;
        }
        
        .add-task button:hover {
            transform: translateY(-2px);
        }
        
        .tasks-list {
            padding: 30px;
        }
        
        .task-item {
            background: white;
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            transition: all 0.3s;
        }
        
        .task-item:hover {
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transform: translateX(5px);
        }
        
        .task-content {
            flex: 1;
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .task-checkbox {
            width: 24px;
            height: 24px;
            cursor: pointer;
        }
        
        .task-text {
            font-size: 16px;
            color: #333;
        }
        
        .task-text.completed {
            text-decoration: line-through;
            color: #999;
        }
        
        .task-date {
            font-size: 12px;
            color: #999;
            margin-left: 10px;
        }
        
        .task-actions {
            display: flex;
            gap: 10px;
        }
        
        .delete-btn {
            background: #ff4757;
            color: white;
            border: none;
            padding: 5px 15px;
            border-radius: 5px;
            cursor: pointer;
            transition: background 0.3s;
        }
        
        .delete-btn:hover {
            background: #ff3838;
        }
        
        .edit-btn {
            background: #ffa502;
            color: white;
            border: none;
            padding: 5px 15px;
            border-radius: 5px;
            cursor: pointer;
            transition: background 0.3s;
        }
        
        .edit-btn:hover {
            background: #ff9500;
        }
        
        .stats {
            background: #f8f9fa;
            padding: 20px 30px;
            display: flex;
            justify-content: space-between;
            border-top: 1px solid #e0e0e0;
        }
        
        .stats div {
            text-align: center;
        }
        
        .stats-number {
            font-size: 24px;
            font-weight: bold;
            color: #667eea;
        }
        
        .stats-label {
            font-size: 12px;
            color: #666;
            margin-top: 5px;
        }
        
        .empty-state {
            text-align: center;
            padding: 40px;
            color: #999;
        }
        
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(-10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .task-item {
            animation: slideIn 0.3s ease;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📝 Gestionnaire de Tâches</h1>
            <p>Organisez vos tâches efficacement</p>
        </div>
        
        <div class="add-task">
            <form method="POST" action="/add">
                <input type="text" name="task" placeholder="Ajouter une nouvelle tâche..." required>
                <button type="submit">➕ Ajouter</button>
            </form>
        </div>
        
        <div class="tasks-list">
            {% if tasks %}
                {% for task in tasks %}
                <div class="task-item">
                    <div class="task-content">
                        <form method="POST" action="/toggle/{{ task.id }}" style="margin: 0;">
                            <input type="checkbox" class="task-checkbox" onchange="this.form.submit()" {% if task.completed %}checked{% endif %}>
                        </form>
                        <div>
                            <span class="task-text {% if task.completed %}completed{% endif %}">{{ task.title }}</span>
                            <span class="task-date">{{ task.date }}</span>
                        </div>
                    </div>
                    <div class="task-actions">
                        <form method="GET" action="/edit/{{ task.id }}" style="margin: 0;">
                            <button type="submit" class="edit-btn">✏️ Modifier</button>
                        </form>
                        <form method="POST" action="/delete/{{ task.id }}" style="margin: 0;">
                            <button type="submit" class="delete-btn">🗑️ Supprimer</button>
                        </form>
                    </div>
                </div>
                {% endfor %}
            {% else %}
                <div class="empty-state">
                    <p>✨ Aucune tâche pour le moment</p>
                    <p>Ajoutez votre première tâche ci-dessus !</p>
                </div>
            {% endif %}
        </div>
        
        <div class="stats">
            <div>
                <div class="stats-number">{{ total_tasks }}</div>
                <div class="stats-label">Total des tâches</div>
            </div>
            <div>
                <div class="stats-number">{{ completed_tasks }}</div>
                <div class="stats-label">Tâches complétées</div>
            </div>
            <div>
                <div class="stats-number">{{ pending_tasks }}</div>
                <div class="stats-label">Tâches en cours</div>
            </div>
        </div>
    </div>
</body>
</html>
"""

# Page d'édition
EDIT_TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modifier la tâche</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            max-width: 500px;
            width: 100%;
            background: white;
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }
        
        h1 {
            color: #667eea;
            margin-bottom: 20px;
            text-align: center;
        }
        
        input {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 16px;
            margin-bottom: 20px;
        }
        
        input:focus {
            outline: none;
            border-color: #667eea;
        }
        
        button {
            padding: 12px 30px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            font-size: 16px;
            margin-right: 10px;
        }
        
        a {
            text-decoration: none;
            padding: 12px 30px;
            background: #999;
            color: white;
            border-radius: 10px;
            display: inline-block;
        }
        
        .buttons {
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>✏️ Modifier la tâche</h1>
        <form method="POST" action="/update/{{ task.id }}">
            <input type="text" name="task" value="{{ task.title }}" required>
            <div class="buttons">
                <button type="submit">💾 Enregistrer</button>
                <a href="/">❌ Annuler</a>
            </div>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    
    return render_template_string(
        HTML_TEMPLATE, 
        tasks=tasks[::-1],  # Afficher les plus récentes en premier
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        pending_tasks=pending_tasks
    )

@app.route('/add', methods=['POST'])
def add_task():
    global task_id_counter
    title = request.form.get('task')
    if title and title.strip():
        tasks.append({
            'id': task_id_counter,
            'title': title.strip(),
            'completed': False,
            'date': datetime.now().strftime('%d/%m/%Y %H:%M')
        })
        task_id_counter += 1
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>')
def edit_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return render_template_string(EDIT_TEMPLATE, task=task)
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    new_title = request.form.get('task')
    for task in tasks:
        if task['id'] == task_id:
            if new_title and new_title.strip():
                task['title'] = new_title.strip()
            break
    return redirect(url_for('index'))

# API REST pour accéder aux tâches en JSON
@app.route('/api/tasks')
def api_tasks():
    return jsonify(tasks)

@app.route('/api/stats')
def api_stats():
    return jsonify({
        'total': len(tasks),
        'completed': sum(1 for task in tasks if task['completed']),
        'pending': sum(1 for task in tasks if not task['completed'])
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)