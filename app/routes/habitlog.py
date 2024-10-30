from flask import Blueprint, jsonify, request
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