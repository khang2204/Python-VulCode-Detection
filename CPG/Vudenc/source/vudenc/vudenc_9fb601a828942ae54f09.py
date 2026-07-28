def try_update_handler(new_stream):...
logger = logging.getLogger('ray')
if _default_handler:
new_handler = logging.StreamHandler(stream=new_stream)
new_handler.setFormatter(_default_handler.formatter)
_default_handler.close()
_default_handler = new_handler
logger.addHandler(_default_handler)
