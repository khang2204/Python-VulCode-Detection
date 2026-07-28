def parse_args(argv):...
parser = argparse.ArgumentParser()
parser.add_argument('content_src_dir', help=
    'Source directory containing content to be intalled.')
parser.add_argument('content_dst_dir', help=
    'Name of directory under <WWW-ROOT> for content to be located.')
parser.add_argument('--www-root', help='WWW root path to install to.')
parser.add_argument('--log-path', help='Directory to write logfiles to.')
args = parser.parse_args(argv)
return args
