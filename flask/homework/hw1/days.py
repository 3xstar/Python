from flask import Flask, render_template, request

app = Flask(__name__)

days = {"Понедельник": "музыка, физ-ра",
        "Вторник": "русский, математика",
        "Среда": "английский, физика",
        "Четверг": "химия, информатика",
        "Пятница": "ОБЖ, история"}

@app.route('/')
def mail():

    day = request.args.get('day')
    if day and day in days:
        return render_template("page.html", day=days[day])
    else:
        return render_template("page.html", day="Выберите день недели")


if __name__ == '__main__':
    app.run(debug=True)