def default(self, line):...
if not validate(line):
print('shrub: {}: command not found. Try "help".'.format(line.split(' ', 1)[0])
    )
message = self.send_cmd(line, self.user_creds)
return
print(message)
return
