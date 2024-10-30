from flask import Blueprint, jsonify, request
from app.extension import db
from app.models import Habit, HabitLog


api = Blueprint('api', __name__,url_prefix='/habits')

error_messages = {
    "DATA_NOT_FOUND" : "Data not found.",
}

@api.route('/create', methods=['POST'])
def create_habit():
    """
    @return:
    """
    data = request.get_json()
    habit = Habit(habit=data['habit'], description=data['description'], interval=data['interval'], goal=data['goal'])
    db.session.add(habit)
    db.session.commit()
    return jsonify(habit.to_dict(), "Data added successfully"),201

@api.route('/list', methods=['GET'])
def get_habit_list():
    """
    @return:
    """
    habits = Habit.query.all()
    data = [habit.to_dict() for habit in habits]
    return jsonify(data),200


@api.route('/delete/<string:habit_id>', methods=['DELETE'])
def delete_habit(habit_id):
    """
    @param habit_id:
    @return:
    """
    habit = Habit.query.get(habit_id)
    if not habit:
        return jsonify({"error": error_messages.get("DATA_NOT_FOUND")}), 404
    db.session.delete(habit)
    db.session.commit()
    return jsonify({"success": "habit deleted successfully"}), 200


@api.route('/get/<string:habit_id>', methods=['GET'])
def get_habit(habit_id):
    """
    @param habit_id:
    @return:
    """
    habit = Habit.query.get(habit_id)
    if not habit:
        return jsonify({"error": error_messages.get("DATA_NOT_FOUND")}), 404
    return jsonify(habit.to_dict()), 200


@api.route('/update/<string:habit_id>', methods=['PUT'])
def update_habit(habit_id):
    """
    @param habit_id:
    @return:
    """
    data = request.get_json()
    habit = Habit.query.get(habit_id)
    if not habit:
        return jsonify({"error": error_messages.get("DATA_NOT_FOUND")}), 404
    habit.habit = data['habit']
    habit.description = data['description']
    habit.interval = data['interval']
    habit.goal = data['goal']
    db.session.commit()
    return jsonify(habit.to_dict()), 200
