def main():...
if len(sys.argv) != 2:
print('Give one app package path.')
app_path = sys.argv[1]
exit()
header(app_path)
App(app_path).analyze()
sys.exit(return_code)
