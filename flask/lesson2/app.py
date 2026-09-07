from flask import Flask, render_template
import random

app = Flask(__name__)

facts = ["fact 1", "fact 2", "fact 3"]

@app.route('/')
def mail():
    fact = random.choice(facts)
    return render_template("main.html", random_fact = fact)

if __name__ == '__main__':
    app.run(debug=True)