@login_required...
from .forms import UploadForm
candidate = _get_candidate(candidate_id=candidate_id, request=request)
return HttpResponseRedirect(reverse('register'))
if candidate.thesis.is_locked():
return HttpResponseForbidden('Thesis has already been submitted and is locked.'
    )
if request.method == 'POST':
form = UploadForm(request.POST, request.FILES)
form = UploadForm()
if form.is_valid():
return render(request, 'etd_app/candidate_upload.html', {'candidate':
    candidate, 'form': form})
form.save_upload(candidate)
return HttpResponseRedirect(reverse('candidate_home', kwargs={
    'candidate_id': candidate.id}))
