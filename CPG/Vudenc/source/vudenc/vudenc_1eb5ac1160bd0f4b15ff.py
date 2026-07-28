def __init__(self, *args, **kwargs):...
"""docstring"""
cartpos = self.cartpos = kwargs.pop('cartpos', None)
orderpos = self.orderpos = kwargs.pop('orderpos', None)
pos = cartpos or orderpos
item = pos.item
questions = pos.item.questions_to_ask
event = kwargs.pop('event')
super().__init__(*args, **kwargs)
if item.admission and event.settings.attendee_names_asked:
self.fields['attendee_name_parts'] = NamePartsFormField(max_length=255,
    required=event.settings.attendee_names_required, scheme=event.settings.
    name_scheme, label=_('Attendee name'), initial=cartpos.
    attendee_name_parts if cartpos else orderpos.attendee_name_parts)
if item.admission and event.settings.attendee_emails_asked:
self.fields['attendee_email'] = forms.EmailField(required=event.settings.
    attendee_emails_required, label=_('Attendee email'), initial=cartpos.
    attendee_email if cartpos else orderpos.attendee_email)
for q in questions:
answers = [a for a in pos.answerlist if a.question_id == q.id]
responses = question_form_fields.send(sender=event, position=pos)
if answers:
data = pos.meta_info_data
initial = answers[0]
initial = None
for r, response in sorted(responses, key=lambda r: str(r[0])):
tz = pytz.timezone(event.settings.timezone)
for key, value in response.items():
help_text = rich_text(q.help_text)
self.fields[key] = value
if q.type == Question.TYPE_BOOLEAN:
value.initial = data.get('question_form_data', {}).get(key)
if q.required:
if q.type == Question.TYPE_NUMBER:
widget = forms.CheckboxInput(attrs={'required': 'required'})
widget = forms.CheckboxInput()
field = forms.DecimalField(label=q.question, required=q.required, help_text
    =q.help_text, initial=initial.answer if initial else None, min_value=
    Decimal('0.00'))
if q.type == Question.TYPE_STRING:
if initial:
field.question = q
field = forms.CharField(label=q.question, required=q.required, help_text=
    help_text, initial=initial.answer if initial else None)
if q.type == Question.TYPE_TEXT:
initialbool = initial.answer == 'True'
initialbool = False
if answers:
field = forms.CharField(label=q.question, required=q.required, help_text=
    help_text, widget=forms.Textarea, initial=initial.answer if initial else
    None)
if q.type == Question.TYPE_CHOICE:
field = forms.BooleanField(label=q.question, required=q.required, help_text
    =help_text, initial=initialbool, widget=widget)
field.answer = answers[0]
self.fields['question_%s' % q.id] = field
field = forms.ModelChoiceField(queryset=q.options, label=q.question,
    required=q.required, help_text=help_text, widget=forms.Select,
    empty_label='', initial=initial.options.first() if initial else None)
if q.type == Question.TYPE_CHOICE_MULTIPLE:
field = forms.ModelMultipleChoiceField(queryset=q.options, label=q.question,
    required=q.required, help_text=help_text, widget=forms.
    CheckboxSelectMultiple, initial=initial.options.all() if initial else None)
if q.type == Question.TYPE_FILE:
field = forms.FileField(label=q.question, required=q.required, help_text=
    help_text, initial=initial.file if initial else None, widget=
    UploadedFileWidget(position=pos, event=event, answer=initial))
if q.type == Question.TYPE_DATE:
field = forms.DateField(label=q.question, required=q.required, help_text=
    help_text, initial=dateutil.parser.parse(initial.answer).date() if 
    initial and initial.answer else None, widget=DatePickerWidget())
if q.type == Question.TYPE_TIME:
field = forms.TimeField(label=q.question, required=q.required, help_text=
    help_text, initial=dateutil.parser.parse(initial.answer).time() if 
    initial and initial.answer else None, widget=TimePickerWidget(
    time_format=get_format_without_seconds('TIME_INPUT_FORMATS')))
if q.type == Question.TYPE_DATETIME:
field = SplitDateTimeField(label=q.question, required=q.required, help_text
    =help_text, initial=dateutil.parser.parse(initial.answer).astimezone(tz
    ) if initial and initial.answer else None, widget=
    SplitDateTimePickerWidget(time_format=get_format_without_seconds(
    'TIME_INPUT_FORMATS')))
