def _str_get(self, task, level=0, border='***', context={}):...
return border + ' ' + (task.user_id and task.user_id.name.upper() or '') + (
    level and ': L' + str(level) or '') + ' - %.1fh / %.1fh' % (task.
    effective_hours or 0.0, task.planned_hours) + ' ' + border + '\n' + border[
    0] + ' ' + (task.name or '') + '\n' + (task.description or '') + '\n\n'
