@staticmethod...
"""docstring"""
users = User.get_all_users_not_pagainated()
users_updated = 1
total_users = len(users)
for user in users:
UserService.check_and_update_mapper_level(user.id)
return users_updated
if users_updated % 50 == 0:
print(f'{users_updated} users updated of {total_users}')
users_updated += 1
