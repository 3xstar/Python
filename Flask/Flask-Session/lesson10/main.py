from flask import Flask, render_template, request, session, redirect
from flask_wtf import FlaskForm
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, IntegerField, SubmitField, RadioField
from wtforms.validators import DataRequired

schedule = {
    "9/2 РПО 25/1" : {"Понедельник" : ["Python"]},
    "9/2 РПО 25/2" : {"Понедельник" : ["Python"]},
    "9/1 РПО 26/1" : {"Понедельник" : ["Python"]},
    "9/1 РПО 26/2" : {"Понедельник" : ["Python"]},
    "9/1 РПО 26/3" : {"Понедельник" : ["Python"]}
}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'VERYSECRETKEY'

app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sessions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_KEY_PREFIX'] = 'session:'
app.config['SESSION_PERMANENT'] = True

Session(app)

class choiceGroup(FlaskForm):
    groupRadioButton = RadioField('Выберите группу', validators = [DataRequired()],
                                  choices= [
                                      ("9/2 РПО 25/1", "9/2 РПО 25/1"),
                                      ("9/2 РПО 25/2", "9/2 РПО 25/2"),
                                      ("9/2 РПО 26/1", "9/2 РПО 26/1"),
                                      ("9/2 РПО 26/2", "9/2 РПО 26/2"),
                                      ("9/2 РПО 26/3", "9/2 РПО 26/3"),
                                  ])
    submit = SubmitField("Confirm")

@app.route('/', methods=['GET', 'POST'])
def index():
    group = session.get('group')
    if group is None:
        form = choiceGroup()
        if request.method == 'POST':
            group = str(form.groupRadioButton.data)
            session['group'] = group
            return render_template('schedule.html', schedule=schedule, user_group=group)
        return render_template('index.html', form=form)
    else:
        return render_template('schedule.html', schedule=schedule, user_group=str(group))

@app.route('/change-group')
def change_group():
    session.pop('group', None)
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
