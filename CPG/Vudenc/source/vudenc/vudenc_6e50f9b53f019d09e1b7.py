@permission_required('tournament.add_game')...
"""docstring"""
t = get_modifiable_tournament_or_404(tournament_id, request.user)
r = get_round_or_404(t, round_num)
count = r.roundplayer_set.count()
sitters = count % 7
if sitters == 0:
return HttpResponseRedirect(reverse('seed_games', args=(tournament_id,
    round_num)))
doubles = 7 - sitters
context = {'tournament': t, 'round': r, 'count': count, 'sitters': sitters,
    'doubles': doubles}
form = GetSevenPlayersForm(request.POST or None, the_round=r)
if form.is_valid():
for rp in r.roundplayer_set.exclude(game_count=1):
context['form'] = form
rp.game_count = 1
for i in range(sitters):
return render(request, 'rounds/get_seven.html', context)
rp.save()
rp = form.cleaned_data['sitter_%d' % i]
for i in range(doubles):
if rp:
rp = form.cleaned_data['double_%d' % i]
return HttpResponseRedirect(reverse('seed_games', args=(tournament_id,
    round_num)))
rp.game_count = 0
if rp:
rp.save()
rp.game_count = 2
rp.save()
