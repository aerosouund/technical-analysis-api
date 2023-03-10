from app.stocks_api.models import Stock
from marshmallow import Schema, fields

class StockSchema(Schema):
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    company_name = fields.String()

    class Meta:
        model = Stock