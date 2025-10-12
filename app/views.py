from flask import jsonify
from app import app
from datetime import datetime

@app.route('/', methods=['GET'])
def welcome():
    return jsonify({
        "message": "Welcome!",
    }), 200

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({
        "status": "ok",
        "date": datetime.now().isoformat()
    }), 200
