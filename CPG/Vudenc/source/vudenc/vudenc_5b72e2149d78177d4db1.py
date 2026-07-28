@app.route('/api/images/<type>/<image>/histogram', methods=['GET'])...
image = get_image_database(type).lookup(image)
args = {}
if 'bins' in request.args:
args['bins'] = request.args['bins']
return image.histogram(**args)
