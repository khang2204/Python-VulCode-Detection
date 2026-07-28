@products.route('/<productId>/reviews/<userId>', methods=['PUT'])...
review = get_review()
ProductsRepository.add_product_review(productId, userId, review)
return 'Duplicate'
return 'Ok'
