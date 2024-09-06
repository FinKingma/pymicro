import requests
import os
from flask import Blueprint, jsonify

product_page = Blueprint('product_page', __name__,template_folder='templates')


BASE_URL = "https://dummyjson.com"
@product_page.route('/products', methods=['GET'])
def get_products():
    response = requests.get(f"{BASE_URL}/products")
    if response.status_code != 200:
        return jsonify({'error': response.json()['message']}), response.status_code
    products = []
    for product in response.json()['products']:
        product_data = {
            'id': product['id'],
            'title': product['title'],
            'brand': product['brand'] if 'brand' in product else None,
            'price': product['price'],
            'description': product['description']
        }
        products.append(product_data)
    return jsonify({'data': products}), 200 if products else 204