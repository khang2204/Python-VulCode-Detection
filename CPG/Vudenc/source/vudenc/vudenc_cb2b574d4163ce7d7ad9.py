@permission_required('tournament.add_roundplayer')...
"""docstring"""
t = get_modifiable_tournament_or_404(tournament_id, request.user)
PlayerRoundFormset = formset_factory(PlayerRoundForm, extra=2, formset=
    BasePlayerRoundFormset)
if round_num:
r = get_round_or_404(t, round_num)
round_set = t.round_set.all()
round_set = t.round_set.filter(pk=r.pk)
data = []
for tp in t.tournamentplayer_set.all():
current = {'player': tp.player}
if round_num:
rps = tp.roundplayers()
formset = PlayerRoundFormset(request.POST or None, tournament=t, round_num=
    int(round_num), initial=data)
formset = PlayerRoundFormset(request.POST or None, tournament=t, initial=data)
for r in round_set:
if formset.is_valid():
played = rps.filter(the_round=r).exists()
data.append(current)
for form in formset:
return render(request, 'tournaments/round_players.html', {'title': _(
    'Roll Call'), 'tournament': t, 'post_url': reverse('roll_call', args=(
    tournament_id,)), 'formset': formset})
current['round_%d' % r.number()] = played
r = t.current_round()
p = form.cleaned_data['player']
i, created = TournamentPlayer.objects.get_or_create(player=p, tournament=t)
if not round_num or r.number() == round_num:
i.full_clean()
form.add_error(form.fields['player'], e)
if created:
if t.seed_games:
i.delete()
i.save()
for r_name, value in form.cleaned_data.items():
if r.roundplayer_set.count() % 7 == 0:
return HttpResponseRedirect(reverse('create_games', args=(tournament_id, r.
    number())))
return render(request, 'tournaments/round_players.html', {'title': _(
    'Roll Call'), 'tournament': t, 'post_url': reverse('roll_call', args=(
    tournament_id,)), 'formset': formset})
if r_name == 'player':
return HttpResponseRedirect(reverse('seed_games', args=(tournament_id, r.
    number())))
return HttpResponseRedirect(reverse('get_seven', args=(tournament_id, r.
    number())))
i = int(r_name[6:])
r = t.round_numbered(i)
if value is True:
i, created = RoundPlayer.objects.get_or_create(player=p, the_round=r)
RoundPlayer.objects.filter(player=p, the_round=r).delete()
i.full_clean()
form.add_error(None, e)
if created:
i.delete()
i.save()
return render(request, 'tournaments/round_players.html', {'title': _(
    'Roll Call'), 'tournament': t, 'post_url': reverse('roll_call', args=(
    tournament_id,)), 'formset': formset})
