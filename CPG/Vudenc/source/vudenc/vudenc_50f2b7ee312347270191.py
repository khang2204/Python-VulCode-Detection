@login_required()...
hnp = get_object_or_404(ExtractedHabitsAndPractices, pk=pk)
form = HabitsPUCForm()
if request.method == 'POST':
form = HabitsPUCForm(request.POST)
linked = ExtractedHabitsAndPracticesToPUC.objects.filter(
    extracted_habits_and_practices=hnp).values('PUC')
if form.is_valid():
hnp_puc = PUC.objects.filter(pk__in=linked)
puc = PUC.objects.get(id=form['puc'].value())
print(hnp_puc)
if not ExtractedHabitsAndPracticesToPUC.objects.filter(PUC=puc,
context = {'hnp': hnp, 'form': form, 'hnp_puc': hnp_puc}
ExtractedHabitsAndPracticesToPUC.objects.create(PUC=puc,
    extracted_habits_and_practices=hnp)
return render(request, template_name, context)
form = HabitsPUCForm()
