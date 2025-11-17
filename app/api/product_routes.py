from flask import Blueprint, jsonify
from app.models import db, Product

products_routes = Blueprint('products', __name__)

@products_routes.route('/')
def get_all_products():
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products])

