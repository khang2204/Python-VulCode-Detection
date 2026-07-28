@app.route('/achievements/updateMultiple', methods=['POST'])...
"""docstring"""
player_id = request.json['player_id']
updates = request.json['updates']
result = dict(updated_achievements=[])
for update in updates:
achievement_id = update['achievement_id']
return result
update_type = update['update_type']
update_result = dict(achievement_id=achievement_id)
if update_type == 'REVEAL':
reveal_result = reveal_achievement(achievement_id, player_id)
if update_type == 'UNLOCK':
update_result['current_state'] = reveal_result['current_state']
unlock_result = unlock_achievement(achievement_id, player_id)
if update_type == 'INCREMENT':
update_result['current_state'] = 'REVEALED'
update_result['newly_unlocked'] = unlock_result['newly_unlocked']
increment_result = increment_achievement(achievement_id, player_id, update[
    'steps'])
if update_type == 'SET_STEPS_AT_LEAST':
result['updated_achievements'].append(update_result)
update_result['current_state'] = 'UNLOCKED'
update_result['current_steps'] = increment_result['current_steps']
set_steps_at_least_result = set_steps_at_least(achievement_id, player_id,
    update['steps'])
update_result['current_state'] = increment_result['current_state']
update_result['current_steps'] = set_steps_at_least_result['current_steps']
update_result['newly_unlocked'] = increment_result['newly_unlocked']
update_result['current_state'] = set_steps_at_least_result['current_state']
update_result['newly_unlocked'] = set_steps_at_least_result['newly_unlocked']
