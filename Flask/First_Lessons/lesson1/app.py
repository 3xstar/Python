import flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return ("<h1>Welcome to Flask</h1><br>"
            "<a href='schedule'>schedule</a>")


@app.route('/schedule')
def schedule():
    return ("<h1>Today's schedule</h1>"
            "<a href='home'>Home</a>")

@app.route("/user/<string:username>/<int:id>")
def user(username, id):
    return (f"<h1>User {username}</h1>"
            f"id {id}")


lessons = ["math", "russian", "programming"]
@app.route('/search')
def search():
        search = flask.request.args.get('lesson', None)
        day = flask.request.args.get('day', None)

        if search in lessons:
            return(f"<h1>{day} {search} есть в списке</h1>")
        else:
            return (f"<h1>{day} {search} нет в списке</h1>")


if __name__ == '__main__':
    app.run(debug=True)