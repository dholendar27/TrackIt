from datetime import timedelta

from flask import Blueprint, jsonify, request
from sqlalchemy import and_

from app.extension import db
from app.models import HabitLog

habitlog = Blueprint('habitlog', __name__,url_prefix='/habitlog')


@habitlog.route('/add', methods=['POST'])
def add_habit_log():
    data = request.get_json()
    habitlog = HabitLog(**data)
    db.session.add(habitlog)
    db.session.commit()
    return jsonify("Message","Data added successfully"), 200


@habitlog.route('/streak/<string:habit_id>',methods=['POST'])
def get_streak(habit_id):
    current_streak = 0
    max_streak = 0
    last_date = None
    completed_days = 0

    data = request.get_json()
    habitlogs = HabitLog.query.filter_by(habit_id=habit_id).filter(and_(HabitLog.date >= data.get('start_date'), HabitLog.date <= data.get('end_date'))).order_by(HabitLog.date).all()
    for log in habitlogs:

        log = log.to_dict()
        print(log)
        if log.get('completed'):
            completed_days += 1

            if last_date and log.get('date') == last_date + timedelta(days=1):
                current_streak += 1
            else:
                current_streak = 1

        max_streak = max(max_streak, current_streak)
        last_date = log.get('date')

    return jsonify("highest_streak",max_streak), 200