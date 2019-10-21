import json

from flask import Flask, Blueprint, request
from flask_restplus import Resource, fields, Api


api = Api(version='1.0', title='Test API', doc='/doc')
namespace = api.namespace('carts')


def calculate(products):
    result = {
        'products': list(products),
    }

    for product in result['products']:
        product['total'] = product['quantity'] * product['price']

    result['total'] = sum(product['total'] for product in products)
    result['average'] = result['total'] / sum(product['quantity'] for product in products)

    return result


# serializers
Product = api.model('Product', {
    'product': fields.String(required=True),
    'price': fields.Float(required=True),
    'quantity': fields.Integer(required=True, min=1),
})


Cart = api.model('Cart', {
    'products': fields.List(fields.Nested(Product), min_items=1),
})


@namespace.route('/cart/')
class CartResource(Resource):
    @api.expect(Cart, validate=True)
    def post(self):
        cart = json.loads(request.data)
        processed_cart = calculate(cart['products'])
        return processed_cart


def create_app():
    flask_app = Flask(__name__)

    blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
    api.init_app(blueprint)
    api.add_namespace(namespace)

    flask_app.register_blueprint(blueprint)

    return flask_app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
