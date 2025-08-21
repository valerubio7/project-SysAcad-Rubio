from marshmallow import Schema, fields, post_load, validate
from app.models.universidad import Universidad


class UniversidadMapping(Schema):
    """
    Universidad Mapping Schema
    """
    id = fields.Integer()
    nombre = fields.String(required=True, validate = validate.Length(min=1, max=100))
    sigla = fields.String(required=True, validate = validate.Length(min=1, max=100))

    @post_load
    def nueva_universidad(self, data, **kwargs):
        """
        Create a new Universidad instance from the deserialized data.
        
        :param data: The deserialized data.
        :return: A new Universidad instance.
        """
        return Universidad(**data)