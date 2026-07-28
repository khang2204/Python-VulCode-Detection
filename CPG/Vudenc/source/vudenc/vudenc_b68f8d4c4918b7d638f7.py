@login_required...
from .forms import FormatChecklistForm
candidate = get_object_or_404(Candidate, id=candidate_id)
format_form = FormatChecklistForm(request.POST, instance=candidate.thesis.
    format_checklist)
if format_form.is_valid():
format_form.handle_post(request.POST, candidate)
return HttpResponseRedirect(reverse('approve', kwargs={'candidate_id':
    candidate_id}))
