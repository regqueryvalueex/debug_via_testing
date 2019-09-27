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
