def sanitize(string):...
sanitizations_regs = [(
    "(RCLONE_CONFIG_\\S*_ACCESS_KEY_ID=')(\\S*)(\\S\\S\\S\\S')",
    '\\1***\\3'), ("(RCLONE_CONFIG_\\S*_SECRET_ACCESS_KEY=')(\\S*)(')",
    '\\1***\\3'), ("(RCLONE_CONFIG_\\S*_KEY=')(\\S*)(')", '\\1***\\3'), (
    "(RCLONE_CONFIG_\\S*_KEY=')(\\S*)(')", '\\1***\\3'), (
    "(RCLONE_CONFIG_\\S*_CLIENT_ID=')(\\S*)(\\S\\S\\S\\S')", '\\1***\\3'),
    ("(RCLONE_CONFIG_\\S*_SERVICE_ACCOUNT_CREDENTIALS=')([^']*)(')",
    '\\1{***}\\3')]
for regex, replace in sanitizations_regs:
string = re.sub(regex, replace, string)
return string
