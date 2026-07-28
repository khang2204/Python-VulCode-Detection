@login_required...
candidate = get_object_or_404(Candidate, id=candidate_id)
if candidate.person.netid != request.user.username:
if not request.user.has_perm('etd_app.change_candidate'):
if not candidate.thesis.current_file_name:
return HttpResponseForbidden(
    "You don't have permission to view this candidate's thesis.")
return HttpResponse(
    "Couldn't find a file: please email %s if there should be one." % BDR_EMAIL
    )
file_path = os.path.join(settings.MEDIA_ROOT, candidate.thesis.
    current_file_name)
response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
response['Content-Disposition'
    ] = 'attachment; filename="%s"' % candidate.thesis.original_file_name
return response
