import os

from flask import Flask, render_template, redirect, url_for, flash, session, abort
from flask_wtf.csrf import CSRFProtect
from datetime import datetime, timezone, timedelta
from models import db, User, Exercise, ExerciseHistory
from forms import LoginForm, RegisterForm, ExerciseForm
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trainings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)

# ⚡ СОВРЕМЕННАЯ БЕЗОПАСНОСТЬ СЕССИЙ (Защита от сессионного угона)
app.config['SESSION_COOKIE_HTTPONLY'] = True  # Запрещает JavaScript доступ к куки (Защита от XSS)
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # Ограничивает передачу куки со сторонних сайтов (Защита от CSRF)

db.init_app(app)
csrf = CSRFProtect(app)


# Ручная проверка авторизации
def check_login():
    return session.get('user_id') is not None


# --- JINJA2 CUSTOM FILTERS ---
@app.template_filter('format_datetime')
def format_datetime(value):
    if value is None:
        return ""
    # Переводим UTC время базы данных в локальное при желании, либо выводим по ТЗ: ДД.ММ.ГГГГ ЧЧ:ММ
    return value.strftime('%d.%m.%Y %H:%M')


@app.template_filter('format_number')
def format_number(value):
    if value is None:
        return ""
    return f"{value:g}"  # Убирает висящие нули (60.0 -> 60)


# --- ROUTES ---

@app.route('/', methods=['GET', 'POST'])
def index():
    if not check_login():
        return redirect(url_for('login'))

    form = ExerciseForm()
    current_user_id = session.get('user_id')

    if form.validate_on_submit():
        title_striped = form.title.data.strip()
        category_selected = form.category.data

        # Строгая проверка ТЗ: Силовым упражнениям обязательны повторы
        if category_selected == 'Strength' and not form.repeat.data:
            form.repeat.errors.append('Repetitions are required for strength exercises.')
            return render_dashboard(form, current_user_id)

        # Не зависимый от регистра поиск через LOWER()
        existing_exercise = Exercise.query.filter(
            Exercise.user_id == current_user_id,
            db.func.lower(Exercise.title) == db.func.lower(title_striped)
        ).first()

        # Для кардио сбрасываем повторы в None
        repeat_val = form.repeat.data if category_selected == 'Strength' else None

        if existing_exercise:
            # Обновление показателей существующего трека
            existing_exercise.category = category_selected
            existing_exercise.value = form.value.data
            existing_exercise.repeat = repeat_val
            existing_exercise.updated_at = datetime.now(timezone.utc)
            flash(f"Exercise '{existing_exercise.title}' successfully updated!", "success")
        else:
            # Создание новой записи
            existing_exercise = Exercise(
                title=title_striped,
                category=category_selected,
                value=form.value.data,
                repeat=repeat_val,
                user_id=current_user_id
            )
            db.session.add(existing_exercise)
            flash(f"Exercise '{title_striped}' successfully added!", "success")

        db.session.commit()

        # Коммитим лог в историю изменений
        history_entry = ExerciseHistory(
            exercise_id=existing_exercise.id,
            value=form.value.data,
            repeat=repeat_val
        )
        db.session.add(history_entry)
        db.session.commit()

        return redirect(url_for('index'))

    return render_dashboard(form, current_user_id)


def render_dashboard(form, user_id):
    # Благодаря lazy=True и связям, запросы отработают моментально
    strength_exercises = Exercise.query.filter_by(user_id=user_id, category='Strength').all()
    cardio_exercises = Exercise.query.filter_by(user_id=user_id, category='Cardio').all()
    return render_template('index.html', form=form, strength=strength_exercises, cardio=cardio_exercises)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if check_login():
        return redirect(url_for('index'))

    form = RegisterForm()
    if form.validate_on_submit():
        username = form.name.data.strip()
        email = form.email.data.strip().lower()

        # Наглядная проверка на уникальность
        if User.query.filter_by(name=username).first():
            form.name.errors.append('This username is already taken.')
            return render_template('register.html', form=form)

        if User.query.filter_by(email=email).first():
            form.email.errors.append('A user with this email is already registered.')
            return render_template('register.html', form=form)

        # Запись хэша пароля
        user = User(name=username, email=email, password_hash=generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()

        # Авторизация сессии
        session.clear()
        session['user_id'] = user.id
        session['username'] = user.name
        session.permanent = True

        flash("Registration successful! Welcome to A-Training.", "success")
        return redirect(url_for('index'))

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if check_login():
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        input_data = form.login_input.data.strip()

        # Ищем совпадение либо по Имени, либо по Email
        user = User.query.filter((User.email == input_data.lower()) | (User.name == input_data)).first()

        if user and check_password_hash(user.password_hash, form.password.data):
            session.clear()
            session['user_id'] = user.id
            session['username'] = user.name

            session.permanent = True
            # Реализация "Remember Me" через лимиты сессий
            if form.remember.data:
                app.permanent_session_lifetime = timedelta(days=7)  # Запомнить на неделю
            else:
                app.permanent_session_lifetime = timedelta(minutes=10)  # Сбросить через 10 мин по ТЗ

            flash("You have successfully logged in.", "success")
            return redirect(url_for('index'))

        # Размытая ошибка ради кибербезопасности согласно ТЗ
        flash("Invalid email/username or password", "danger")

    return render_template('login.html', form=form)


@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))


@app.route('/exercise/<int:id>/history', methods=['GET'])
def exercise_history(id):
    if not check_login():
        return redirect(url_for('login'))

    exercise = Exercise.query.get_or_404(id)

    # Защита приватности: смотреть логи может только создатель
    if exercise.user_id != session.get('user_id'):
        abort(403)

    # Сортировка: новые логи сверху (.desc())
    history_records = ExerciseHistory.query.filter_by(exercise_id=id).order_by(ExerciseHistory.created_at.desc()).all()
    return render_template('history.html', exercise=exercise, history=history_records)


@app.route('/exercise/<int:id>/delete', methods=['POST'])
def delete_exercise(id):
    if not check_login():
        return redirect(url_for('login'))

    exercise = Exercise.query.get_or_404(id)
    if exercise.user_id != session.get('user_id'):
        abort(403)

    # Благодаря каскаду cascade="all, delete-orphan" в модели Exercise,
    # вызов db.session.delete(exercise) автоматически сотрет всю историю этого упражнения!
    db.session.delete(exercise)
    db.session.commit()

    flash(f"Exercise '{exercise.title}' and its full history have been cleared.", "info")
    return redirect(url_for('index'))


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
