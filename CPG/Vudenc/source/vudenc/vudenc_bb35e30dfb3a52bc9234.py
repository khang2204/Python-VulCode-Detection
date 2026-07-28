def get_attendee_list(self):...
attendee_list = str('')
counter = 1
reg_ids = self.sudo().registration_ids
reg_ids = sorted(reg_ids, key=lambda x: x.date_open, reverse=False)
for registration in reg_ids:
if registration.state == 'open':
return attendee_list
if counter == 1:
attendee_list += registration.partner_id.sudo().name
attendee_list += ', ' + registration.partner_id.sudo().name
counter += 1
