@aiohttp_jinja2.template('index.html')...
images = natsorted(glob(os.path.join(settings.STORAGE_DIR, '**/*.jpg'),
    recursive=True), key=lambda x: x.upper())
return {'images': (Item(x.replace(settings.STORAGE_DIR, '')) for x in images)}
