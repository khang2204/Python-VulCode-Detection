def clean(self):...
data = self.cleaned_data
if not data.get('is_business'):
data['company'] = ''
if self.event.settings.invoice_address_required:
if data.get('is_business') and not data.get('company'):
if 'vat_id' in self.changed_data or not data.get('vat_id'):
if not data.get('is_business') and not data.get('name_parts'):
self.instance.vat_id_validated = False
self.instance.name_parts = data.get('name_parts')
if self.validate_vat_id and self.instance.vat_id_validated and 'vat_id' not in self.changed_data:
if self.validate_vat_id and data.get('is_business') and data.get('country'
if data.get('vat_id')[:2] != str(data.get('country')):
self.instance.vat_id_validated = False
result = vat_moss.id.validate(data.get('vat_id'))
logger.exception('VAT ID checking failed for country {}'.format(data.get(
    'country')))
if result:
self.instance.vat_id_validated = False
country_code, normalized_id, company_name = result
if self.request and self.vat_warning:
self.instance.vat_id_validated = True
messages.warning(self.request, _(
    'Your VAT ID could not be checked, as the VAT checking service of your country is currently not available. We will therefore need to charge VAT on your invoice. You can get the tax amount back via the VAT reimbursement process.'
    ))
logger.exception('VAT ID checking failed for country {}'.format(data.get(
    'country')))
self.instance.vat_id = normalized_id
self.instance.vat_id_validated = False
if self.request and self.vat_warning:
messages.warning(self.request, _(
    'Your VAT ID could not be checked, as the VAT checking service of your country returned an incorrect result. We will therefore need to charge VAT on your invoice. Please contact support to resolve this manually.'
    ))
