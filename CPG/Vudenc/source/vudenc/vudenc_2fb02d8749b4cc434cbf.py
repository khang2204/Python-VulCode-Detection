def raise_request_limit():...
from core.libs import bottle
import settings
bottle.BaseRequest.MEMFILE_MAX = settings.MAX_REQUEST
