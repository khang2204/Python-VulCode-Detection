from flask import Blueprint, jsonify, request
from infrastructure import ProductsRepository
from math import ceil
products = Blueprint('products', __name__)
DEFAULT_PAGE = 1
DEFAULT_PER_PAGE = 20
DEFAULT_RATING = 0
@products.route('/', methods=['GET'])...
filters = get_filters()
if filters['search'] is None:
products = ProductsRepository.get_products(filters)
products = ProductsRepository.search_products(filters, filters['search'])
total_products = ProductsRepository.get_total_products(filters)
total_products = ProductsRepository.get_total_searched_products(filters,
    filters['search'])
total_pages = ceil(total_products / filters['perPage'])
return jsonify(products=products, total_products=total_products,
    total_pages=total_pages)
