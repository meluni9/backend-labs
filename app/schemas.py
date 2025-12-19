from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=2))

class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    user_id = fields.Int(load_default=None)

class RecordSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)
    amount = fields.Float(required=True)
    created_at = fields.DateTime(dump_only=True)

class RecordQuerySchema(Schema):
    user_id = fields.Int(required=False)
    category_id = fields.Int(required=False)
