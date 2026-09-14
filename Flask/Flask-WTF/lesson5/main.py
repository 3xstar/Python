from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, BooleanField, TextAreaField, IntegerField, SelectField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email, NumberRange, Length, EqualTo
import email_validator

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    country = SelectField('Country', validators=[DataRequired()],
                          choices=[
                              ('ru', 'Russia'),
                              ('us', 'USA'),
                              ('ca', 'Canada'),
                              ('cn', 'China')
                          ])
    gender = RadioField('Gender', validators=[DataRequired()],
                        choices=[
                            ("male", "Male"),
                            ("female", "Female")
                        ])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=0, max=100)])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=12)])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])

    subscribe = BooleanField('Subscribe')

    submit = SubmitField('Submit')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        country = form.country.data
        gender = form.gender.data
        age = form.age.data
        password = form.password.data
        subscribe = form.subscribe.data

        print(name, email, country, gender, age, password, subscribe)

        return render_template('result.html', name=name, email=email)
    return render_template('signup.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)