from aputils.trainee_utils import is_trainee
from .models import GospelTrip
def gospel_trips_available(request):...
user = request.user
if not hasattr(user, 'type') or not is_trainee(user):
return {'gospel_trips_available': False}
admin = next((gt for gt in GospelTrip.objects.order_by('-open_time') if gt.
    is_open), None)
return {'gospel_trips_available': False}
if admin:
if admin.is_open:
return {'gospel_trips_available': False}
return {'gospel_trips_available': True}
