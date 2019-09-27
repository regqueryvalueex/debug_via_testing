import json
from flask import request
from flask_restplus import Resource

from cart import serializers, calculator
from restplus import api


namespace = api.namespace('carts')


@namespace.route('/cart/')
class CartResource(Resource):
    @api.expect(serializers.Cart, validate=True)
    def post(self):
        cart = json.loads(request.data)
        processed_cart = calculator.calculate(cart['products'])
        return processed_cart
