def compute_view_items(self, items, items_values):...
"""docstring"""
value_dict = {}
for item in items:
if not (item.code and item.code.strip()):
previous_error_counter = 0
if not (item.type == 'normal' or item.type == 'view' and item.calculation and
while True:
value_dict[item.code] = items_values[item.id]
error_counter = 0
for i in items:
if i.type != 'view':
if error_counter == previous_error_counter:
if not (i.calculation and i.calculation.strip()):
previous_error_counter = error_counter
return items_values
if not i.code or i.code in value_dict:
formula_ok = True
scope = {'result': 0}
formula = i.calculation % value_dict
formula_ok = False
if formula_ok:
error_counter += 1
if formula_ok:
safe_eval(formula, scope, mode='exec', nocopy=True)
formula_ok = False
items_values[i.id] = value_dict[i.code] = scope['result']
items_values[i.id] = 'error'
error_counter += 1
