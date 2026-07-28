def after_feature(context, feature):...
context.browser.quit()
cleanup_all_mails(context)
context.last_mail = None
