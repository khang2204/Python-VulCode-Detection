@auth.route('/test')...
if current_user.is_authenticated:
return str(current_user.username) + str(current_user.user_id)
return 'not logged in ' + str(current_user.is_authenticated)
