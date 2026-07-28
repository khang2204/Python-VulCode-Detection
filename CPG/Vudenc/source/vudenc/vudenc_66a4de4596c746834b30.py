def get_aws_browser():...
if aws_browser is None:
aws_browser = Browser()
return aws_browser
lr = AWSLoginRequest(aws_browser, admin_info['username'], admin_info[
    'password'], base_url=AWS_BASE_URL)
aws_browser.login(lr)
