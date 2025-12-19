from flask import jsonify, request
from sqlalchemy.exc import IntegrityError
from app import app, db
from app.models import User, Category, Record
from app.schemas import UserSchema, CategorySchema, RecordSchema, RecordQuerySchema
from marshmallow import ValidationError
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from passlib.hash import pbkdf2_sha256


@app.route('/register', methods=['POST'])
def register():
    schema = UserSchema()
    try:
        data = schema.load(request.get_json())
    except ValidationError as err:
        return jsonify(err.messages), 400

    hashed_password = pbkdf2_sha256.hash(data["password"])

    new_user = User(
        username=data['username'],
        password=hashed_password
    )

    try:
        db.session.add(new_user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "User already exists"}), 400

    return jsonify(schema.dump(new_user)), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Missing username or password"}), 400

    user = User.query.filter_by(username=data["username"]).first()

    if user and pbkdf2_sha256.verify(data["password"], user.password):
        access_token = create_access_token(identity=str(user.id))
        return jsonify({"access_token": access_token}), 200

    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    users = User.query.all()
    return jsonify(UserSchema(many=True).dump(users)), 200


@app.route('/user/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(UserSchema().dump(user)), 200


@app.route('/user/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return '', 204


@app.route('/category', methods=['GET'])
@jwt_required()
def get_categories():
    user_id = request.args.get('user_id')

    current_user_id = get_jwt_identity()

    query = Category.query.filter(Category.user_id == None)

    if current_user_id:
        query = Category.query.filter((Category.user_id == None) | (Category.user_id == current_user_id))

    categories = query.all()
    return jsonify(CategorySchema(many=True).dump(categories)), 200


@app.route('/category', methods=['POST'])
@jwt_required()
def create_category():
    schema = CategorySchema()
    try:
        data = schema.load(request.get_json())
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_category = Category(name=data['name'], user_id=data.get('user_id'))
    db.session.add(new_category)
    db.session.commit()
    return jsonify(schema.dump(new_category)), 201


@app.route('/category/<int:category_id>', methods=['DELETE'])
@jwt_required()
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return '', 204


@app.route('/record', methods=['POST'])
@jwt_required()
def create_record():
    schema = RecordSchema()
    try:
        data = schema.load(request.get_json())
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_record = Record(
        user_id=data['user_id'],
        category_id=data['category_id'],
        amount=data['amount']
    )
    try:
        db.session.add(new_record)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "User or Category not found"}), 400

    return jsonify(schema.dump(new_record)), 201


@app.route('/record/<int:record_id>', methods=['GET'])
@jwt_required()
def get_record(record_id):
    record = Record.query.get_or_404(record_id)
    return jsonify(RecordSchema().dump(record)), 200


@app.route('/record', methods=['GET'])
@jwt_required()
def get_records_filtered():
    schema = RecordQuerySchema()
    try:
        args = schema.load(request.args)
    except ValidationError as err:
        return jsonify(err.messages), 400

    user_id = args.get('user_id')
    category_id = args.get('category_id')

    query = Record.query
    if user_id:
        query = query.filter_by(user_id=user_id)
    if category_id:
        query = query.filter_by(category_id=category_id)

    records = query.all()
    return jsonify(RecordSchema(many=True).dump(records)), 200


@app.route('/record/<int:record_id>', methods=['DELETE'])
@jwt_required()
def delete_record(record_id):
    record = Record.query.get_or_404(record_id)
    db.session.delete(record)
    db.session.commit()
    return '', 204


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"status": "ok", "message": "Database connected"}), 200


@app.route('/')
def welcome():
    return jsonify({"message": "Welcome to Lab 4 with Auth!"})
