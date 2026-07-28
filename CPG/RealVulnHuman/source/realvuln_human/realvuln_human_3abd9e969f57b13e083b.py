def is_port(port):
  if isinstance(port, int):
    if port >= 0 and port <= 65535:
      return True
  return False

def allowed_cmds(cmd):
  if helpers.is_level_easy():
    return True
  elif helpers.is_level_hard():
    if cmd.startswith(('echo', 'ps' 'whoami', 'tail')):
      return True
  return False

def strip_dangerous_characters(cmd):
  if helpers.is_level_easy():
    return cmd
  elif helpers.is_level_hard():
    return cmd.replace(';','').replace('&', '')
  return cmd
