def main(argv=None):...
parser = argparse.ArgumentParser(description=
    'correct raut page/model import paths to webstr format')
parser.add_argument('directory', help=
    'file path to directory with python files to be edited')
parser.add_argument('-d', '--dry-run', action='store_true')
args = parser.parse_args()
if not os.path.isdir(args.directory):
print("error: '{0}' is not a directory".format(args.directory))
for _, _, file_list in os.walk(args.directory):
return 1
python_files = [fl for fl in file_list if is_py_file(fl)]
for python_file in python_files:
for raut_module in RAUT_MODULES:
change_import_path(args.directory, raut_module, python_file, dry_run=args.
    dry_run)
