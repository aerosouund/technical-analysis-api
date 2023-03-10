from app.stocks_api.models import Stock
from marshmallow import Schema, fields

class StockSchema(Schema):
    id = fields.String()
    name = fields.String()
    price = fields.String()
    availability = fields.String()

    class Meta:
        model = Stock