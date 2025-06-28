from flask import Blueprint, jsonify

area_bp = Blueprint('area', __name__)

@area_bp.route('/areas', methods=['GET'])
def get_areas():
    # Respuesta de ejemplo, puedes modificarla según la lógica real
    return jsonify([]), 200
