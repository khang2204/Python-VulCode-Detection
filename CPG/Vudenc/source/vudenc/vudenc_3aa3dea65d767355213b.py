def SetUpOutputRedirect(cmd):...
i = cmd.index('>')
sys.stdout = open(cmd[i + 1], 'w')
print('this is a test')
