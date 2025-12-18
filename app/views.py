from flask import jsonify, request
from app import app
from app import data
from datetime import datetime
import uuid

@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"message": "Welcome!"}), 200


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({
        "status": "ok",
        "date": datetime.now().isoformat()
    }), 200


# User endpoints
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(data.users.values())), 200


@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = data.users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404


@app.route('/user', methods=['POST'])
def create_user():
    user_data = request.get_json()
    user_id = uuid.uuid4().hex
    user = {"id": user_id, **user_data}
    data.users[user_id] = user
    return jsonify(user), 201


@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in data.users:
        del data.users[user_id]
        return '', 204
    return jsonify({"error": "User not found"}), 404


# Category endpoints
@app.route('/category', methods=['GET'])
def get_categories():
    return jsonify(list(data.categories.values())), 200


@app.route('/category', methods=['POST'])
def create_category():
    category_data = request.get_json()
    category_id = uuid.uuid4().hex
    category = {"id": category_id, **category_data}
    data.categories[category_id] = category
    return jsonify(category), 201


@app.route('/category/<category_id>', methods=['DELETE'])
def delete_category(category_id):
    if category_id in data.categories:
        del data.categories[category_id]
        return '', 204
    return jsonify({"error": "Category not found"}), 404


# Record endpoints
@app.route('/record/<record_id>', methods=['GET'])
def get_record(record_id):
    record = data.records.get(record_id)
    if record:
        return jsonify(record), 200
    return jsonify({"error": "Record not found"}), 404


@app.route('/record', methods=['POST'])
def create_record():
    record_data = request.get_json()
    record_id = uuid.uuid4().hex
    record = {
        "id": record_id,
        "created_at": datetime.now().isoformat(),
        **record_data
    }
    data.records[record_id] = record
    return jsonify(record), 201


@app.route('/record/<record_id>', methods=['DELETE'])
def delete_record(record_id):
    if record_id in data.records:
        del data.records[record_id]
        return '', 204
    return jsonify({"error": "Record not found"}), 404


@app.route('/record', methods=['GET'])
def get_records():
    user_id = request.args.get('user_id')
    category_id = request.args.get('category_id')

    if not user_id and not category_id:
        return jsonify({"error": "user_id or category_id parameter required"}), 400

    filtered_records = []
    for record in data.records.values():
        if user_id and category_id:
            if record.get('user_id') == user_id and record.get('category_id') == category_id:
                filtered_records.append(record)
        elif user_id:
            if record.get('user_id') == user_id:
                filtered_records.append(record)
        elif category_id:
            if record.get('category_id') == category_id:
                filtered_records.append(record)

    return jsonify(filtered_records), 200
