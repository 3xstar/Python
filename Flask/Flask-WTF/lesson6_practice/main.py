from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, NumberRange

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

class IMTForm(FlaskForm):
    weight = FloatField('Weight (kg) : ', validators=[DataRequired(), NumberRange(min=20, max=300)])
    height = IntegerField('Height (cm): ', validators=[DataRequired(), NumberRange(min=100, max=250)])
    age = IntegerField('Age: ', validators=[DataRequired(), NumberRange(min=1, max=100)])

    submit = SubmitField('Result')

@app.route('/imt', methods=['GET', 'POST'])
def imt():
    form = IMTForm()
    if form.validate_on_submit():
        weight = form.weight.data
        height = form.height.data
        age = form.age.data

        bmi = round(weight / (height / 100) ** 2, 1)

        return render_template('result.html', weight=weight, height=height, age=age, bmi=bmi)
    return render_template('imt.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)