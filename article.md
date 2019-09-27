####Debug via testing

#####TL;DR


Use your testing framework in your everyday routine, it can drastically decrease
amount of repeated actions you perform during debugging, investigation or just
playing with your code

#####DRY

You know that principle? DRY - don't repeat yourself. It can be applicable not
only for code. Over the years, working side by side with many others
developers, i noticed that in most cases we all fail to follow this principle.
The simplest example - you have a bug in your API and you need to fix. Most
of the people will follow next steps:
 - send a broken request to broken API endpoint
 - find an issue
 - fix the issue
 - check if all working fine
 - if not - repeat all the steps

That is the simplest approach and it works perfectly fine, so why would i complain
about it?

In ideal world, you need to send request twice, fist time - to find bug, second - to 
ensure, that everything is fine. Since the world is not ideal, you may stuck  again 
for hours sending request over and over.  

####Automate everything

That's when tests come to the rescue. Lets go over small, simple and naive example.

Here's a small web api to receive a shopping list and calculate a total price for 
product in cart

#####serializers.py

```python
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
```

#####resources.py

```python
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

```

#####calculator.py

```python
def calculate(products):
    products = list(products)
    result = {
        'products': list(products),
    }

    for product in result['products']:
        product['total'] = product['quantity'] * product['price']

    result['total'] = sum(product['total'] for product in products)
    result['average'] = result['total'] / sum(product['quantity'] for product in products)

    return result

```
