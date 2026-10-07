from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, NumberRange, Optional


class LoginForm(FlaskForm):
    login_input = StringField('Email or Username', validators=[DataRequired(), Length(3, 120)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired(), Length(3, 50)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(5, 120)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, message='Password must be at least 6 characters long')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')


class ExerciseForm(FlaskForm):
    title = StringField('Exercise Name', validators=[DataRequired(), Length(1, 120)])
    category = SelectField('Type', choices=[('Strength', '💪 Strength'), ('Cardio', '🏃 Cardio')], validators=[DataRequired()])
    value = FloatField('Value', validators=[DataRequired(), NumberRange(min=0.01, message='Value must be greater than 0')])
    repeat = IntegerField('Repetitions', validators=[Optional(), NumberRange(min=1, max=1000)])
    submit = SubmitField('Save Exercise')


class VerifyCodeForm(FlaskForm):
    code = StringField('Verification Code', validators=[DataRequired(), Length(6, 6, message="Code must be 6 digits")])
    submit = SubmitField('Verify')


class ForgotPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Send Reset Code')


class ResetPasswordForm(FlaskForm):
    code = StringField('Reset Code', validators=[DataRequired(), Length(6, 6)])
    password = PasswordField('New Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Reset Password')