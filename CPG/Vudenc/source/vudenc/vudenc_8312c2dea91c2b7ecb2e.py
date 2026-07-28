def round_simple(request, tournament_id, round_num, template):...
"""docstring"""
t = get_visible_tournament_or_404(tournament_id, request.user)
r = get_round_or_404(t, round_num)
context = {'tournament': t, 'round': r}
return render(request, 'rounds/%s.html' % template, context)
