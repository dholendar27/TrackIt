import datetime
import uuid

from app.extension import db
from sqlalchemy import Column, String, DATETIME, INTEGER, Integer, ForeignKey,BOOLEAN

INTERVAL_CHOICES = (
    ('daily','daily'),('monthly','monthly'),('weekly','weekly')
)

class Habit(db.Model):
    __tablename__ = 'habits'

    id = Column(String(36), primary_key=True,nullable=False,default=lambda: str(uuid.uuid4()))
    habit = Column(String(255),nullable=False)
    description = Column(String(255),nullable=True)
    interval = Column(String(50),nullable=False,default='daily')
    goal = Column(Integer,nullable=False)
    created_at = Column(DATETIME, default=datetime.datetime.now(datetime.timezone.utc))
    updated_at = Column(DATETIME, default=datetime.datetime.now(datetime.timezone.utc), onupdate=datetime.datetime.now(datetime.timezone.utc))
    habitlog = db.relationship('HabitLog', backref='habit', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'habit': self.habit,
            'description': self.description,
            'interval': self.interval,
            'goal': self.goal,
        }


class HabitLog(db.Model):
    __tablename__ = 'habitlog'

    id = Column(String(36), primary_key=True,nullable=False,default=lambda: str(uuid.uuid4()))
    habit_id = Column(String(36), ForeignKey('habits.id'), nullable=False)
    date = Column(DATETIME, default=datetime.datetime.now(datetime.timezone.utc))
    completed = Column(BOOLEAN,nullable=False)
