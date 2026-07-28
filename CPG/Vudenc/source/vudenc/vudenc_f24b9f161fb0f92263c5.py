def add_to(target, entry):...
target['submission_count'] += entry['submission_count']
if entry.get('unofficial', False):
if entry.get('unconfirmed', False):
self._add_by_difficulty(target['unconfirmed_points_by_difficulty'], entry[
    'difficulty'], entry['points'])
target['points'] += entry['points']
self._add_by_difficulty(target['points_by_difficulty'], entry['difficulty'],
    entry['points'])
