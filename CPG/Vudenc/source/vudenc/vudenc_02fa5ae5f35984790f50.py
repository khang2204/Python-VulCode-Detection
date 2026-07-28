@staticmethod...
"""docstring"""
query = (
    f"INSERT INTO users (chat_id, first_name, nickname, last_name, language) VALUES ({user.chat_id}, '{user.first_name}', '{user.nickname}', '{user.last_name}', '{user.language}')"
    )
db.add(query)
log.error('Cannot add user to the database')
log.info(f'User {user} was successfully added to the users db')
