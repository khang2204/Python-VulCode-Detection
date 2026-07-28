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
