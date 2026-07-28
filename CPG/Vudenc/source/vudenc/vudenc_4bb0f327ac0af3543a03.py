@products.route('/department/<department>', methods=['GET'])...
filters = get_filters()
products = ProductsRepository.get_department_products(filters, department)
total_products = ProductsRepository.get_total_departments_products(filters,
    department)
total_pages = ceil(total_products / filters['perPage'])
return jsonify(products=products, total_products=total_products,
    total_pages=total_pages)
