def get_group_by_args():...
"""docstring"""
group_by = request.args.get('group_by')
if not group_by:
group_by = ''
return group_by
