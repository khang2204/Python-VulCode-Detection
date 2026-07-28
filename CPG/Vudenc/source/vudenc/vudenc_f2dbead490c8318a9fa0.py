def _stddebug_():...
from core.boot import settings
_stddebug = lambda x: _stderr(x
    ) if settings.DEBUG_MODE is True else lambda x: None
return _stddebug
