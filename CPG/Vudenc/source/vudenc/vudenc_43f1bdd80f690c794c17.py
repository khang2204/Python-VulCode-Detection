@products.route('/<id>/reviews', methods=['GET'])...
filters = get_filters()
product_reviews = ProductsRepository.get_product_reviews(id, filters)
total_product_reviews = ProductsRepository.get_total_product_reviews(id)
total_pages = ceil(total_product_reviews / filters['perPage'])
return jsonify(product_reviews=product_reviews, total_product_reviews=
    total_product_reviews, total_pages=total_pages)
