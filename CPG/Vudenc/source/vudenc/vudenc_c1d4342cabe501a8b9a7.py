@property...
self._check_report_owner()
passphrase = self.request.POST['key']
return False
if passphrase:
logger.info(self.invalid_access_no_key_message)
self.storage.report.decrypt_record(passphrase)
logger.warn(self.invalid_access_key_message)
return False
return True
return False
