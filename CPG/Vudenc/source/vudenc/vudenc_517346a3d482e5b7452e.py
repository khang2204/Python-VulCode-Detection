@staticmethod...
"""docstring"""
user = UserService.get_user_by_id(user_id)
verification_email_sent = False
if user_dto.email_address and user.email_address != user_dto.email_address.lower(
SMTPService.send_verification_email(user_dto.email_address.lower(), user.
    username)
user.update(user_dto)
user.set_email_verified_status(is_verified=False)
return dict(verificationEmailSent=verification_email_sent)
verification_email_sent = True
