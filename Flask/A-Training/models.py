from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    # ⚡ Современная связь: при удалении пользователя удалятся и его упражнения (cascade)
    exercises = db.relationship('Exercise', backref='racer', lazy=True, cascade="all, delete-orphan")


class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(20), nullable=False)  # 'Strength' или 'Cardio'
    value = db.Column(db.Float, nullable=False)
    repeat = db.Column(db.Integer, nullable=True)  # Только для силовых

    # Использование актуального стандарта timezone.utc
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc),
                           onupdate=lambda: datetime.now(timezone.utc))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # ⚡ Связь с историей: удаление упражнения автоматически очистит таблицу истории
    history = db.relationship('ExerciseHistory', backref='track', lazy=True, cascade="all, delete-orphan")


class ExerciseHistory(db.Model):
    __tablename__ = 'exercise_history'

    id = db.Column(db.Integer, primary_key=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
    value = db.Column(db.Float, nullable=False)
    repeat = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
