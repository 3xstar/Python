import os
import random
from flask import Flask, render_template, redirect, url_for, flash, request, session, abort
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail, Message
from datetime import datetime, timezone, timedelta
from models import db, User, Exercise, ExerciseHistory
from forms import LoginForm, RegisterForm, ExerciseForm, VerifyCodeForm, ForgotPasswordForm, ResetPasswordForm
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trainings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)

app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

# ⚡ КОНФИГУРАЦИЯ FLASK-MAIL
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 465))
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

db.init_app(app)
csrf = CSRFProtect(app)
mail = Mail(app)

def check_login():
    return session.get('user_id') is not None



def send_email(target_email, subject, code_title, code_value):

    print("\n" + "=" * 50)
    print(f"🚀 [MOCK EMAIL LOGGER] Target: {target_email}")
    print(f"🚀 [MOCK EMAIL LOGGER] Subject: {subject}")
    print(f"🚀 [MOCK EMAIL LOGGER] {code_title}: {code_value}")
    print("=" * 50 + "\n")

    try:
        msg = Message(subject, recipients=[target_email])

        msg.html = f"""
        <html>
        <body style="font-family: -apple-system, BlinkMacSystemFont, sans-serif; background-color: #f1f5f9; padding: 30px; margin: 0;">
            <div style="max-width: 460px; margin: 0 auto; background-color: #ffffff; padding: 32px; border-radius: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.02); border: 1px solid #e2e8f0;">
                <h2 style="color: #0f172a; margin-top: 0; font-size: 20px; font-weight: 700; letter-spacing: -0.5px;">⚡ A-Training Telemetry</h2>
                <p style="color: #475569; font-size: 14px; line-height: 1.5;">You requested a security action. Use the high-speed verification code below to proceed:</p>
                <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; padding: 16px; border-radius: 12px; text-align: center; margin: 24px 0;">
                    <span style="display: block; font-size: 11px; text-transform: uppercase; color: #64748b; font-weight: 700; letter-spacing: 1px; margin-bottom: 4px;">{code_title}</span>
                    <span style="font-family: 'Orbitron', monospace; font-size: 32px; font-weight: 700; color: #2563eb; letter-spacing: 2px;">{code_value}</span>
                </div>
                <p style="color: #94a3b8; font-size: 12px; margin-bottom: 0;">If you did not request this code, please ignore this message.</p>
            </div>
        </body>
        </html>
        """
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Flask-Mail SMTP Error: {e}")
        # Возвращаем True, чтобы при блоке сети хостинга сайт не крашился, а пускал по коду из консоли
        return True


# --- JINJA2 CUSTOM FILTERS ---
@app.template_filter('format_datetime')
def format_datetime(value):
    if value is None:
        return ""
    return value.strftime('%d.%m.%Y %H:%M')


@app.template_filter('format_number')
def format_number(value):
    if value is None:
        return ""
    return f"{value:g}"


# --- ROUTES ---

@app.route('/', methods=['GET', 'POST'])
def index():
    if not check_login():
        return redirect(url_for('login'))

    form = ExerciseForm()
    current_user_id = session.get('user_id')

    if form.validate_on_submit():
        title_striped = form.title.data.strip()
        category_selected = form.category.data

        if category_selected == 'Strength' and not form.repeat.data:
            form.repeat.errors.append('Repetitions are required for strength exercises.')
            return render_dashboard(form, current_user_id)

        existing_exercise = Exercise.query.filter(
            Exercise.user_id == current_user_id,
            db.func.lower(Exercise.title) == db.func.lower(title_striped)
        ).first()

        repeat_val = form.repeat.data if category_selected == 'Strength' else None

        if existing_exercise:
            existing_exercise.category = category_selected
            existing_exercise.value = form.value.data
            existing_exercise.repeat = repeat_val
            existing_exercise.updated_at = datetime.now(timezone.utc)
            flash(f"Exercise '{existing_exercise.title}' successfully updated!", "success")
        else:
            existing_exercise = Exercise(
                title=title_striped,
                category=category_selected,
                value=form.value.data,
                repeat=repeat_val,
                user_id=current_user_id
            )
            db.session.add(existing_exercise)
            flash(f"Exercise '{title_striped}' successfully added!", "success")

        db.session.commit()

        history_entry = ExerciseHistory(
            exercise_id=existing_exercise.id,
            value=form.value.data,
            repeat=repeat_val
        )
        db.session.add(history_entry)
        db.session.commit()

        return redirect(url_for('index'))

    return render_dashboard(form, current_user_id)


def render_dashboard(form, user_id):
    strength_exercises = Exercise.query.filter_by(user_id=user_id, category='Strength').all()
    cardio_exercises = Exercise.query.filter_by(user_id=user_id, category='Cardio').all()
    return render_template('index.html', form=form, strength=strength_exercises, cardio=cardio_exercises)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if check_login():
        return redirect(url_for('index'))

    form = RegisterForm()
    if form.validate_on_submit():
        username = form.name.data.strip()
        email = form.email.data.strip().lower()

        if User.query.filter_by(name=username).first():
            form.name.errors.append('This username is already taken.')
            return render_template('register.html', form=form)

        if User.query.filter_by(email=email).first():
            form.email.errors.append('A user with this email is already registered.')
            return render_template('register.html', form=form)

        verify_code = str(random.randint(100000, 999999))

        session['temp_register_user'] = {
            'name': username,
            'email': email,
            'password_hash': generate_password_hash(form.password.data)
        }
        session['temp_verification_code'] = verify_code

        send_email(email, "Verify Your A-Training Account", "REGISTRATION CODE", verify_code)
        flash("Verification code processed! Check your email or system console.", "info")
        return redirect(url_for('verify_registration'))

    return render_template('register.html', form=form)


@app.route('/verify-registration', methods=['GET', 'POST'])
def verify_registration():
    if check_login() or 'temp_register_user' not in session:
        return redirect(url_for('index'))

    form = VerifyCodeForm()
    if form.validate_on_submit():
        if form.code.data == session.get('temp_verification_code'):
            user_data = session['temp_register_user']

            user = User(name=user_data['name'], email=user_data['email'], password_hash=user_data['password_hash'])
            db.session.add(user)
            db.session.commit()

            session.pop('temp_register_user', None)
            session.pop('temp_verification_code', None)

            session['user_id'] = user.id
            session['username'] = user.name
            session.permanent = True

            flash("Registration verified! Welcome to A-Training.", "success")
            return redirect(url_for('index'))
        else:
            form.code.errors.append("Invalid verification code. Try again.")

    return render_template('verify.html', form=form, title="Account Verification")


@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if check_login():
        return redirect(url_for('index'))

    form = ForgotPasswordForm()
    if form.validate_on_submit():
        email = form.email.data.strip().lower()
        user = User.query.filter_by(email=email).first()

        if user:
            reset_code = str(random.randint(100000, 999999))
            session['temp_reset_email'] = email
            session['temp_reset_code'] = reset_code

            send_email(email, "Reset Your A-Training Password", "PASSWORD RESET CODE", reset_code)
            flash("Reset code processed! Check your email or system console.", "info")
            return redirect(url_for('reset_password'))
        else:
            flash("If the email exists, a reset code has been sent.", "info")
            return redirect(url_for('reset_password'))

    return render_template('forgot_password.html', form=form)


@app.route('/reset-password', methods=['GET', 'POST'])
def reset_password():
    if check_login() or 'temp_reset_email' not in session:
        return redirect(url_for('index'))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        if form.code.data == session.get('temp_reset_code'):
            email = session.get('temp_reset_email')
            user = User.query.filter_by(email=email).first()

            if user:
                user.password_hash = generate_password_hash(form.password.data)
                db.session.commit()

                session.pop('temp_reset_email', None)
                session.pop('temp_reset_code', None)

                flash("Password updated successfully. Please login.", "success")
                return redirect(url_for('login'))
        else:
            form.code.errors.append("Incorrect reset token.")

    return render_template('reset_password.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if check_login():
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        input_data = form.login_input.data.strip()

        user = User.query.filter((User.email == input_data.lower()) | (User.name == input_data)).first()

        if user and check_password_hash(user.password_hash, form.password.data):
            session.clear()
            session['user_id'] = user.id
            session['username'] = user.name

            session.permanent = True
            if form.remember.data:
                app.permanent_session_lifetime = timedelta(days=7)
            else:
                app.permanent_session_lifetime = timedelta(minutes=10)

            flash("You have successfully logged in.", "success")
            return redirect(url_for('index'))

        flash("Invalid email/username or password", "danger")

    return render_template('login.html', form=form)


@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))


@app.route('/exercise/<int:id>/history', methods=['GET'])
def exercise_history(id):
    if not check_login():
        return redirect(url_for('login'))

    exercise = Exercise.query.get_or_404(id)

    if exercise.user_id != session.get('user_id'):
        abort(403)

    history_records = ExerciseHistory.query.filter_by(exercise_id=id).order_by(ExerciseHistory.created_at.desc()).all()
    return render_template('history.html', exercise=exercise, history=history_records)


@app.route('/exercise/<int:id>/delete', methods=['POST'])
def delete_exercise(id):
    if not check_login():
        return redirect(url_for('login'))

    exercise = Exercise.query.get_or_404(id)
    if exercise.user_id != session.get('user_id'):
        abort(403)

    db.session.delete(exercise)
    db.session.commit()

    flash(f"Exercise '{exercise.title}' and its full history have been cleared.", "info")
    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    port = int(os.environ.get("SERVER_PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
