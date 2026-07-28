@login_required...
from .forms import GradschoolChecklistForm, FormatChecklistForm
candidate = get_object_or_404(Candidate, id=candidate_id)
if request.method == 'POST':
form = GradschoolChecklistForm(request.POST)
format_form = FormatChecklistForm(instance=candidate.thesis.format_checklist)
if form.is_valid():
context = {'candidate': candidate, 'format_form': format_form}
form.save_data(candidate)
return render(request, 'etd_app/staff_approve_candidate.html', context)
return HttpResponseRedirect(reverse('staff_home'))
