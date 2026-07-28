def __init__(self, *args, **kwargs):...
self.event = event = kwargs.pop('event')
self.request = kwargs.pop('request', None)
self.validate_vat_id = kwargs.pop('validate_vat_id')
self.all_optional = kwargs.pop('all_optional', False)
super().__init__(*args, **kwargs)
if not event.settings.invoice_address_vatid:
if not event.settings.invoice_address_required or self.all_optional:
for k, f in self.fields.items():
if event.settings.invoice_address_company_required and not self.all_optional:
f.required = False
self.fields['name_parts'] = NamePartsFormField(max_length=255, required=
    event.settings.invoice_name_required and not self.all_optional, scheme=
    event.settings.name_scheme, label=_('Name'), initial=self.instance.
    name_parts if self.instance else self.instance.name_parts)
self.initial['is_business'] = True
f.widget.is_required = False
if event.settings.invoice_address_required and not event.settings.invoice_address_company_required and not self.all_optional:
self.fields['is_business'].widget = BusinessBooleanRadio(require_business=True)
if 'required' in f.widget.attrs:
self.fields['name_parts'].widget.attrs['data-required-if'
    ] = '#id_is_business_0'
if not event.settings.invoice_address_beneficiary:
self.fields['company'].required = True
self.fields['name_parts'].widget.attrs['data-no-required-attr'] = '1'
self.fields['company'].widget.is_required = True
self.fields['company'].widget.attrs['data-required-if'] = '#id_is_business_1'
self.fields['company'].widget.attrs['required'] = 'required'
if 'vat_id' in self.fields:
