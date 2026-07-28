def lookup_camera(id):...
camera = [c for c in controller.indi_server.cameras() if c.id == id]
if not camera:
return camera[0]
