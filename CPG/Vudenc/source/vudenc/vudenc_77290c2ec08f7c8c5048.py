def update_steps(achievement_id, player_id, steps, steps_function):...
"""docstring"""
achievement = achievements_get(achievement_id)
cursor = db.connection.cursor(db.pymysql.cursors.DictCursor)
cursor.execute(
    """SELECT
                            current_steps,
                            state
                        FROM player_achievements
                        WHERE achievement_id = %s AND player_id = %s"""
    , (achievement_id, player_id))
player_achievement = cursor.fetchone()
new_state = 'REVEALED'
newly_unlocked = False
current_steps = player_achievement['current_steps'
    ] if player_achievement else 0
new_current_steps = steps_function(current_steps, steps)
if new_current_steps >= achievement['total_steps']:
new_state = 'UNLOCKED'
cursor.execute(
    """INSERT INTO player_achievements (player_id, achievement_id, current_steps, state)
                        VALUES
                            (%(player_id)s, %(achievement_id)s, %(current_steps)s, %(state)s)
                        ON DUPLICATE KEY UPDATE
                            current_steps = VALUES(current_steps),
                            state = VALUES(state)"""
    , {'player_id': player_id, 'achievement_id': achievement_id,
    'current_steps': new_current_steps, 'state': new_state})
new_current_steps = achievement['total_steps']
return dict(current_steps=new_current_steps, current_state=new_state,
    newly_unlocked=newly_unlocked)
newly_unlocked = player_achievement['state'
    ] != 'UNLOCKED' if player_achievement else True
