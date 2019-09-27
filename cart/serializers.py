from restplus import api
from flask_restplus import fields


Product = api.model('Product', {
    'product': fields.String(required=True),
    'price': fields.Float(required=True),
    'quantity': fields.Integer(required=True),
})


Cart = api.model('Cart', {
    'products': fields.List(fields.Nested(Product), min_items=1),
})


ProcessedProduct = api.inherit('ProcessedProduct', Product, {
    'total': fields.Float(required=True),
})


ProcessedCart = api.model('ProcessedCart', {
    'products': fields.List(fields.Nested(ProcessedProduct), min_items=1),
    'total': fields.Float(required=True),
})
