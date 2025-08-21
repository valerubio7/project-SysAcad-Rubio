from flask import jsonify, Blueprint, request
from app.mapping.universidad_mapping import UniversidadMapping
from app.services.universidad_service import UniversidadService

universidad_bp = Blueprint('universidad', __name__)
universidad_mapping = UniversidadMapping()

@universidad_bp.route('/universidades', methods=['GET'])
def buscar_universidad():
    universidades = UniversidadService.buscar_todos()
    return universidad_mapping.dump(universidades, many=True), 200

@universidad_bp.route('/universidades/<int:id>', methods=['GET'])
def buscar_universidad_por_id(id):
    universidad = UniversidadService.buscar_por_id(id)
    return universidad_mapping.dump(universidad), 200

@universidad_bp.route('/universidades', methods=['POST'])
def crear_universidad():
    universidad = universidad_mapping.load(request.get_json())
    UniversidadService.crear_universidad(universidad)
    return jsonify("Universidad creada"), 200

@universidad_bp.route('/universidades/<int:id>', methods=['PUT'])
def borrar_universidad(id):
    UniversidadService.borrar_por_id(id) 
    return jsonify("Universidad borrada"), 200