import django_tables2 as tables
from .models import campaign, event, injection, result, simics_memory_diff, simics_register_diff
id_ = tables.TemplateColumn(
    '<a href="/campaign/{{ value }}/results">{{ value }}</a>', accessor='id')
num_cycles = tables.Column()
results = tables.Column(empty_values=(), orderable=False)
def render_num_cycles(self, record):...
return '{:,}'.format(record.num_cycles)
