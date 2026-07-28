def make_input(self, version, name, value, attribute):...
contact_name, contact_phone, contact_email = ((value or '').split('|') + [
    '', '', ''])[:3]
return """<table>
                    <tr><td class="label">%s</td><td>%s</td></tr>
                    <tr><td class="label">%s</td><td>%s</td></tr>
                    <tr><td class="label">%s</td><td>%s</td></tr>
                  </table>""" % (
    _('Name'), self.text_input(name + '.name', contact_name), _('Phone'),
    self.text_input(name + '.phone', contact_phone), _('E-mail'), self.
    text_input(name + '.email', contact_email))
