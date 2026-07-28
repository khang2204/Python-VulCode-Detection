def check_creds(username, password, real_password):
  if username != 'admin':
    return (False, 'Username is invalid')

  if password == real_password:
    return (True, 'Password Accepted.')

  return (False, 'Password Incorrect')

def on_denylist(query):
  normalized_query = ''.join(query.split())
  queries = [
    'query{systemHealth}',
    '{systemHealth}'
  ]

  if normalized_query in queries:
    return True
  return False

def operation_name_allowed(operation_name):
  opnames_allowed = ['CreatePaste', 'CreateUser', 'EditPaste', 'getPastes', 'UploadPaste', 'ImportPaste']
  if operation_name in opnames_allowed:
    return True
  return False

def depth_exceeded(depth):
  depth_allowed = config.MAX_DEPTH
  if depth > depth_allowed:
