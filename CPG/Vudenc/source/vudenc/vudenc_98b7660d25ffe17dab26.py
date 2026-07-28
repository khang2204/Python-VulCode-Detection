def __init__(self, telegram_id):...
super(Explorer, self).__init__()
self.user_id = db.select('user', 'telegram_id = ' + str(telegram_id))[0]['id']
self.path = [db.select('directory', 
    "name = '/' AND parent_directory_id = 'NULL' AND user_id = " + str(self
    .user_id))[0]['id']]
self.last_action_message_ids = []
