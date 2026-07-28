def construct_selects(spy: ISpy, current_name: str='') ->Iterator[str]:...
if spy.is_subquery:
yield construct_subquery(spy, name=current_name)
if not spy.selected_fields:
yield current_name
for field_name, field_spy in spy.selected_fields.items():
joined_name = f'{current_name}.{field_name}'.lstrip('.')
yield from construct_selects(field_spy, joined_name)
