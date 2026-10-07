from flask import Flask, render_template, request, redirect, jsonify
from models import db, Task
from forms import TaskForm
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_manager.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'

db.init_app(app)


@app.route('/')
def index():
    now = datetime.now()
    today_end = now.replace(hour=23, minute=59, second=59)
    week_end = today_end + timedelta(days=7)

    # 1. Получаем только необходимые данные для счетчиков (быстро)
    completed_count = Task.query.filter_by(is_done=True).count()
    total_count = Task.query.count()

    # Просроченные
    overdue = Task.query.filter_by(is_done=False).filter(Task.deadline < now).order_by(Task.deadline.asc()).all()

    # Активные задачи (не выполненные и не просроченные)
    # Получаем их одним запросом и сортируем по дедлайну
    active_tasks = Task.query.filter_by(is_done=False).filter(Task.deadline >= now).order_by(Task.deadline.asc()).all()

    # Разделяем активные задачи на группы в Python (это очень быстро по сравнению с запросами к БД)
    today = []
    this_week = []
    later = []

    for task in active_tasks:
        if task.deadline <= today_end:
            today.append(task)
        elif task.deadline <= week_end:
            this_week.append(task)
        else:
            later.append(task)

    # Выполненные задачи (можно ограничить количество, например, последние 50)
    completed = Task.query.filter_by(is_done=True).order_by(Task.deadline.desc()).limit(50).all()

    return render_template('index.html',
                           overdue=overdue,
                           today=today,
                           this_week=this_week,
                           later=later,
                           completed=completed,
                           completed_count=completed_count,
                           total_count=total_count)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            deadline=form.deadline.data,
            priority=form.priority.data
        )
        db.session.add(task)
        db.session.commit()
        return redirect('/')
    return render_template("add.html", form=form)


@app.route('/toggle-task/<int:id>')
def toggle_task(id):
    task = Task.query.get_or_404(id)
    task.is_done = not task.is_done
    db.session.commit()
    return redirect("/")


@app.route('/delete-task/<int:id>')
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect("/")


@app.route('/update-task-group', methods=['POST'])
def update_task_group():
    data = request.get_json(silent=True) or {}
    task_id = data.get('task_id')
    new_group = data.get('group')

    if not task_id or not new_group:
        return jsonify({'success': False, 'error': 'bad payload'}), 400

    task = db.session.get(Task, int(task_id))
    if not task:
        return jsonify({'success': False}), 404

    new_group = data.get('group')
    now = datetime.now()

    if new_group == 'completed':
        task.is_done = True
    else:
        task.is_done = False
        if new_group == 'overdue':
            task.deadline = now - timedelta(days=1)  # Делаем задачу просроченной
        elif new_group == 'today':
            task.deadline = now.replace(hour=23, minute=59)
        elif new_group == 'this_week':
            task.deadline = now + timedelta(days=3)
        elif new_group == 'later':
            task.deadline = now + timedelta(days=8)

    db.session.commit()
    return jsonify({'success': True})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
