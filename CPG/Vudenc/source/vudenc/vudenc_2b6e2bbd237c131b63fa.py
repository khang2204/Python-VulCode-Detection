def construct_subquery(spy: ISpy, name: str) ->str:...
select_fields = _flatten(construct_selects(field_spy, field_name) for 
    field_name, field_spy in spy.selected_fields.items())
return f"(SELECT {', '.join(select_fields)} FROM {name})"
