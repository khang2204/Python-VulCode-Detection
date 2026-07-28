@staticmethod...
i = content.rfind(',')
if i > -1:
return cmdTemplate[0] % (content[:i], content[i + 1:]) + '\n'
return cmdTemplate[1] % content + '\n'
