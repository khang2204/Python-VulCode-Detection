@staticmethod...
if new_state == TaskStatus.MAPPED:
project.tasks_mapped += 1
if new_state == TaskStatus.VALIDATED:
if action == 'change':
project.tasks_validated += 1
if new_state == TaskStatus.BADIMAGERY:
if new_state == TaskStatus.MAPPED:
if last_state == TaskStatus.MAPPED:
project.tasks_bad_imagery += 1
user.tasks_mapped += 1
if new_state == TaskStatus.VALIDATED:
project.tasks_mapped -= 1
if last_state == TaskStatus.VALIDATED:
user.tasks_validated += 1
if new_state == TaskStatus.INVALIDATED:
if action == 'undo':
project.tasks_validated -= 1
if last_state == TaskStatus.BADIMAGERY:
user.tasks_invalidated += 1
if last_state == TaskStatus.MAPPED:
project.tasks_bad_imagery -= 1
user.tasks_mapped -= 1
if last_state == TaskStatus.VALIDATED:
user.tasks_validated -= 1
if last_state == TaskStatus.INVALIDATED:
user.tasks_invalidated -= 1
