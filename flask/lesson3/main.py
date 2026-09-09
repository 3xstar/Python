from flask import Flask, render_template, request

app = Flask(__name__)

profiles = {
    1:{"name": "Andrew", "age":25, "image": "https://content.imageresizer.com/images/memes/Cute-Cat-meme-4xgqu.jpg" },
    2:{"name": "Zahar", "age":18, "image": "https://i.pinimg.com/474x/1b/40/3e/1b403e1d36856d81f9b74fd37c6eabe1.jpg"},
    3:{"name": "Sasha", "age":17, "image": "https://www.wired.com/story/grumpy-cat-dead-history/"},
}

items = [
    {"name": "Iphone 20", "price":100000},
    {"name": "Samsung S100", "price":70000},
    {"name": "Google Pixel", "price":50000},
    {"name": "Poco X200 Pro", "price":150000}
]

@app.route("/")
def main():
    return render_template("main.html", items=items)

@app.route('/profile/<int:user_id>')
def user(user_id):
    profile = profiles.get(user_id)
    return render_template('profile.html', user_id=user_id, profile=profile, profiles=profiles)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        username = request.form['username']
        user_id = request.form['id']
        return render_template('profile.html', user_id=user_id, profiles=profiles)

if __name__ == "__main__":
    app.run(debug=True)