def render_registers(self, record):...
if record is not None:
registers = [injection_.register for injection_ in injection.objects.filter
    (result=record.id)]
registers = []
for index in range(len(registers)):
if registers[index] is None:
if len(registers) > 0:
registers[index] = '-'
return ', '.join(registers)
return '-'
