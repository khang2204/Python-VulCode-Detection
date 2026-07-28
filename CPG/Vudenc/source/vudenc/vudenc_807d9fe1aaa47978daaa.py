@login_required...
from .forms import MetadataForm
candidate = _get_candidate(candidate_id=candidate_id, request=request)
return HttpResponseRedirect(reverse('register'))
if candidate.thesis.is_locked():
return HttpResponseForbidden('Thesis has already been submitted and is locked.'
    )
if request.method == 'POST':
post_data = request.POST.copy()
form = MetadataForm(instance=candidate.thesis)
post_data['candidate'] = candidate.id
context = {'candidate': candidate, 'form': form, 'ID_VAL_SEPARATOR':
    ID_VAL_SEPARATOR}
form = MetadataForm(post_data, instance=candidate.thesis)
return render(request, 'etd_app/candidate_metadata.html', context)
if form.is_valid():
thesis = form.save()
if thesis.abstract != form.cleaned_data['abstract']:
messages.info(request,
    "Your abstract contained invisible characters that we've removed. Please make sure your abstract is correct in the information section below."
    )
if thesis.title != form.cleaned_data['title']:
messages.info(request,
    "Your title contained invisible characters that we've removed. Please make sure your title is correct in the information section below."
    )
if _user_keywords_changed(thesis, request.POST.getlist('keywords', [])):
messages.info(request,
    "Your keywords contained invisible characters that we've removed. Please make sure your keywords are correct in the information section below."
    )
return HttpResponseRedirect(reverse('candidate_home', kwargs={
    'candidate_id': candidate.id}))
