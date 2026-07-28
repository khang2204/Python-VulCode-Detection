import json
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from cuckoo.common.config import config
from cuckoo.core.submit import SubmitManager
from cuckoo.web.bin.utils import api_post, JsonSerialize, json_error_response
submit_manager = SubmitManager()
def defaults():...
machinery = config('cuckoo:cuckoo:machinery')
if config('routing:vpn:enabled'):
vpns = config('routing:vpn:vpns')
vpns = []
return {'machine': config('%s:%s:machines' % (machinery, machinery)),
    'package': None, 'priority': 2, 'timeout': config(
    'cuckoo:timeouts:default'), 'routing': {'route': config(
    'routing:routing:route'), 'inetsim': config('routing:inetsim:enabled'),
    'tor': config('routing:tor:enabled'), 'vpns': vpns}, 'options': {
    'enable-services': False, 'enforce-timeout': False, 'full-memory-dump':
    config('cuckoo:cuckoo:memory_dump'), 'no-injection': False,
    'process-memory-dump': True, 'simulated-human-interaction': True}}
