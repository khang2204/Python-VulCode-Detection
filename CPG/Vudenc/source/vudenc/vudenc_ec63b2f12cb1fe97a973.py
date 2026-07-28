def __init__(self, **kwargs):...
self.users_map = {u.id: u for u in User.objects.all()}
prefetch_tables = [('advisors', Advisor), ('breakdowns', Breakdown), (
    'confirmations', CustomerResponse), ('notifications', Notification)]
self.table_maps = {}
for table, model in prefetch_tables:
prefetch_map = collections.defaultdict(list)
super().__init__(**kwargs)
instances = model.objects.all()
if table == 'notifications':
instances = instances.filter(type='c').order_by('created')
for instance in instances:
prefetch_map[instance.win_id].append(instance)
self.table_maps[table] = prefetch_map
