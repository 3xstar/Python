from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_manager.db' # путь для бд
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False # отключение отслеживания бд
app.config['SECRET_KEY'] = 'secret'

db = SQLAlchemy(app) # объявление бд

class Task(db.Model): # создание таблицы
    id = db.Column(db.Integer, primary_key=True) # создание полей
    title = db.Column(db.String, nullable = False)
    description = db.Column(db.Text, nullable = False)
    done = db.Column(db.Boolean, nullable = False)
    category = db.Column(db.String, nullable=False)


class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()]) # Заменили StringField на TextAreaField
    done = BooleanField('Done Status')
    category = SelectField('Category', validators=[DataRequired()],
                           choices=[
                               ('education', 'Education'),
                               ('sport', 'Sport'),
                               ('work', 'Work'),
                               ('home', 'Home'),
                               ('other', 'Other')
                           ])
    submit = SubmitField('Save')


# запись данных в бд
@app.route('/add', methods=['GET', 'POST'])
def add():
    form = TaskForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        category = form.category.data
        task = Task(title=title, description=description, done=False, category=category)
        db.session.add(task)
        db.session.commit()
        return redirect('/')
    return render_template("add.html", form=form)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=="POST":
        category_filter = request.form.get("search-request", "all")
        status_filter = request.form.get("status-request", "all")

        query = Task.query


        if category_filter and category_filter != "all":
            query = query.filter(Task.category == category_filter)

        if status_filter == "completed":
            query = query.filter(Task.done == True)
        elif status_filter == "open":
            query = query.filter(Task.done == False)

        tasks = query.all()

        return render_template("main.html",
                               tasks=tasks,
                               search_data=category_filter,
                               status_data=status_filter)

    tasks = Task.query.all()
    return render_template('main.html', tasks=tasks, search_data="all", status_data="all")

@app.route('/task/<int:id>')
def task(id):
    task = Task.query.get(id) # получить информацию по эл. БД
    return render_template("task.html", task=task)

@app.route('/delete-task/<int:id>')
def delete_task(id):
    task = Task.query.get(id) # получить заметку
    db.session.delete(task) # удалить заметку
    db.session.commit() # сохранить изменения
    return redirect("/") # вернуться на главную

@app.route('/complete-task/<int:id>')
def complete_task(id):
    task = Task.query.get(id) # получить заметку
    if task:
        task.done = True
        db.session.commit()  # сохранить изменения
    return redirect("/") # вернуться на главную

@app.route('/edit-task/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    task = Task.query.get(id)
    form = TaskForm(obj=task) #obj=note передать объект в форму
    if form.validate_on_submit(): # условие что данные были отправлены
        task.title = form.title.data
        task.description = form.description.data
        task.done = False
        task.category = form.category.data
        db.session.commit()
        return redirect("/")
    return render_template("update.html", form=form)

if __name__ == '__main__':
    with app.app_context(): # открытие всех файлов приложения
        db.create_all() # создание файла БД
    app.run(debug=True)