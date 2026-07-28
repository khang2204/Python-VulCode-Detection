def _execute(self, command):...
byteOutput = subprocess.check_output(command, shell=True)
output = byteOutput.decode('UTF-8').rstrip()
return output
