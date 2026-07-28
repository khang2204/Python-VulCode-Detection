from google.appengine.ext import ndb
from gae_libs.handlers.base_handler import BaseHandler
from gae_libs.handlers.base_handler import Permission
def _GetLowerAndUpperBoundCommitPositions(lower_bound, upper_bound):...
if lower_bound is None and upper_bound is None:
return None, None
lower_bound = lower_bound if lower_bound is not None else upper_bound
upper_bound = upper_bound if upper_bound is not None else lower_bound
return min(lower_bound, upper_bound), max(lower_bound, upper_bound)
