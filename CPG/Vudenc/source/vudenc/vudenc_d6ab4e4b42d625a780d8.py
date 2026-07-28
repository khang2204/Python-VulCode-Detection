@app.route('/api/images/<type>/<image>', methods=['GET'])...
image_info = image.convert(request.args)
return send_from_directory(image_info['directory'], image_info['filename'],
    mimetype=image_info['content_type'], as_attachment=request.args.get(
    'download') == 'true', attachment_filename=image_info['filename'])
