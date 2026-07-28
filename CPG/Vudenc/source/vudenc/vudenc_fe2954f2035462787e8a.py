def reveal_achievement(achievement_id, player_id):...
"""docstring"""
cursor = db.connection.cursor(db.pymysql.cursors.DictCursor)
cursor.execute(
    """SELECT
                            state
                        FROM player_achievements
                        WHERE achievement_id = %s AND player_id = %s"""
    , (achievement_id, player_id))
player_achievement = cursor.fetchone()
new_state = player_achievement['state'] if player_achievement else 'REVEALED'
cursor.execute(
    """INSERT INTO player_achievements (player_id, achievement_id, state)
                        VALUES
                            (%(player_id)s, %(achievement_id)s, %(state)s)
                        ON DUPLICATE KEY UPDATE
                            state = VALUES(state)"""
    , {'player_id': player_id, 'achievement_id': achievement_id, 'state':
    new_state})
return dict(current_state=new_state)
