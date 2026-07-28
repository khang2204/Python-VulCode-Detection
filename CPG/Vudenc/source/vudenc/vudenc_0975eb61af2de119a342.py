def setup_logger(logging_level, logging_format):...
"""docstring"""
logger = logging.getLogger('ray')
if type(logging_level) is str:
logging_level = logging.getLevelName(logging_level.upper())
logger.setLevel(logging_level)
_default_handler = logging.StreamHandler()
_default_handler.setFormatter(logging.Formatter(logging_format))
logger.addHandler(_default_handler)
logger.propagate = False
