from flask import Flask, request, render_template

app = Flask(__name__)

USERS_DB = {}

SCHEDULE = {
    "Programmer": {
        "Понедельник": "Python Разработка, Математика",
        "Вторник": "Базы данных, Алгоритмы",
        "Среда": "Веб-технологии Flask, Английский язык",
        "Четверг": "Операционные системы, Физкультура",
        "Пятница": "Проектирование ПО, Философия"
    },
    "Designer": {
        "Понедельник": "Рисунок с натуры, История искусств",
        "Вторник": "UI/UX Проектирование, Figma",
        "Среда": "Колористика, Цифровая графика",
        "Четверг": "3D-Моделирование, Типографика",
        "Пятница": "Анимация, Психология восприятия"
    },
    "Engineer": {
        "Понедельник": "Высшая математика, Физика",
        "Вторник": "Инженерная графика, Начертательная геометрия",
        "Среда": "Теоретическая механика, Материаловедение",
        "Четверг": "Электротехника, Метрология",
        "Пятница": "Безопасность жизнедеятельности, Схемотехника"
    },
    "Modeller": {
        "Понедельник": "Введение в 3D, Скульптинг в Blender",
        "Вторник": "Анатомия для художников, Текстурирование",
        "Среда": "Запекание карт, Low-Poly моделирование",
        "Четверг": "Hard Surface моделирование, Освещение",
        "Пятница": "Анимация персонажей, Портфолио"
    }
}


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        age = request.form['age']
        email = request.form['email']
        password = request.form['password']

        for existing_email, data in USERS_DB.items():
            if existing_email == email:
                return render_template("form1.html", error="Пользователь с такой почтой уже существует!")
            if data['username'] == username:
                return render_template("form1.html", error="Это имя пользователя уже занято!")

        return render_template("group_choice.html", username=username, age=age, email=email, password=password)

    return render_template("form1.html")


@app.route("/save-user", methods=['POST'])
def save_user():
    username = request.form['username']
    age = request.form['age']
    email = request.form['email']
    password = request.form['password']
    selected_group = request.form['group']

    USERS_DB[email] = {
        'username': username,
        'age': age,
        'email': email,
        'password': password,
        'group': selected_group
    }

    user_schedule = SCHEDULE.get(selected_group, {})

    return render_template("form2.html",
                           username=username,
                           age=age,
                           email=email,
                           group=selected_group,
                           schedule=user_schedule)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email in USERS_DB and USERS_DB[email]['password'] == password:
            user_data = USERS_DB[email]
            user_schedule = SCHEDULE.get(user_data['group'], {})

            return render_template("form2.html",
                                   username=user_data['username'],
                                   age=user_data['age'],
                                   email=user_data['email'],
                                   group=user_data['group'],
                                   schedule=user_schedule)
        else:
            return render_template("login.html", error="Неверный Email или Пароль!")

    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)
