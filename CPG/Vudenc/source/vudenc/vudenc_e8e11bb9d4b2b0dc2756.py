def form_valid(self, form):...
selected_flags = []
for question in entry_form_config:
flag = form.cleaned_data.get(str(question['id']), False)
return self.render_to_response({'form': form, 'submitted': True,
    'claimable_benefits': Benefit.objects.find_claimable(selected_flags)})
if flag:
selected_flags.append(getattr(BenefitRequirement.flags, build_question_flag
    (question)))
