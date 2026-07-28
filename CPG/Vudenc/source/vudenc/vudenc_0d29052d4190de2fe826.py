def parse_arguments(arguments):...
"""docstring"""
parser = argparse.ArgumentParser()
parser.add_argument('message')
return parser.parse_args(arguments)
