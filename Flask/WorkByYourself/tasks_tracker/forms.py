from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateTimeField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from datetime import datetime


class TaskForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    description = TextAreaField('Описание')
    deadline = DateTimeField('Дедлайн', validators=[DataRequired()], format='%Y-%m-%dT%H:%M')
    priority = SelectField('Priority', validators=[DataRequired()],
                           choices=[
                                ('low', 'Low'),
                                ('medium', 'Medium'),
                                ('high', 'High')])
    submit = SubmitField('Сохранить')

    def validate_deadline(self, field):
        if field.data < datetime.now():
            raise ValidationError("Deadline can't be in past")