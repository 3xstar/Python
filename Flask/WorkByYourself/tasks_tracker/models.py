from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)

    # Добавляем index=True для полей, по которым часто фильтруем
    deadline = db.Column(db.DateTime, nullable=False, index=True)
    priority = db.Column(db.String(10), default='medium', index=True)
    is_done = db.Column(db.Boolean, default=False, index=True)

    created_at = db.Column(db.DateTime, default=datetime.now)

    @property
    def is_overdue(self):
        return not self.is_done and self.deadline < datetime.utcnow()
