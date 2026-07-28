@api.model...
record = self.env['phone.common'].get_record_from_phone_number(phone)
if record:
partner = self.browse(record[1])
return record and partner.lang
