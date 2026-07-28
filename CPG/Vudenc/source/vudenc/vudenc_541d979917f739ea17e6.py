def main():...
parser = argparse.ArgumentParser(description='Post ads on Kijiji')
parser.add_argument('-u', '--username', help='username of your kijiji account')
parser.add_argument('-p', '--password', help='password of your kijiji account')
subparsers = parser.add_subparsers(help='sub-command help')
postParser = subparsers.add_parser('post', help='post a new ad')
postParser.add_argument('inf_file', type=str, help=
    '.inf file containing posting details')
postParser.set_defaults(function=post_ad)
folderParser = subparsers.add_parser('folder', help='post ad from folder')
folderParser.add_argument('folderName', type=str, help=
    'folder containing ad details')
folderParser.set_defaults(function=post_folder)
repostFolderParser = subparsers.add_parser('repost_folder', help=
    'post ad from folder')
repostFolderParser.add_argument('folderName', type=str, help=
    'folder containing ad details')
repostFolderParser.set_defaults(function=repost_folder)
showParser = subparsers.add_parser('show', help='show currently listed ads')
showParser.set_defaults(function=show_ads)
deleteParser = subparsers.add_parser('delete', help='delete a listed ad')
deleteParser.add_argument('id', type=str, help=
    'id of the ad you wish to delete')
deleteParser.set_defaults(function=delete_ad)
nukeParser = subparsers.add_parser('nuke', help='delete all ads')
nukeParser.set_defaults(function=nuke)
checkParser = subparsers.add_parser('check_ad', help='check if ad is active')
checkParser.add_argument('folderName', type=str, help=
    'folder containing ad details')
checkParser.set_defaults(function=check_ad)
repostParser = subparsers.add_parser('repost', help='repost an existing ad')
repostParser.add_argument('inf_file', type=str, help=
    '.inf file containing posting details')
repostParser.set_defaults(function=repost_ad)
buildParser = subparsers.add_parser('build_ad', help=
    'Generates the item.inf file for a new ad')
buildParser.set_defaults(function=generate_inf_file)
args = parser.parse_args()
args.function(args)
parser.print_help()
