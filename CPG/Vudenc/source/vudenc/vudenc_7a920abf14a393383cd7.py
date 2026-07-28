@permission_required('tournament.add_game')...
"""docstring"""
t = get_modifiable_tournament_or_404(tournament_id, request.user)
r = get_round_or_404(t, round_num)
games = r.game_set.all()
data = []
for g in games:
current = {'game_name': g.name, 'the_set': g.the_set}
round_players = r.roundplayer_set.count()
for gp in g.gameplayer_set.all():
expected_games = (round_players + 6) // 7
current[gp.power.name] = gp.roundplayer()
data.append(current)
if expected_games < 1:
expected_games = 1
GamePlayersFormset = formset_factory(GamePlayersForm, extra=expected_games -
    games.count(), formset=BaseGamePlayersFormset)
formset = GamePlayersFormset(request.POST or None, the_round=r, initial=data)
if formset.is_valid():
for f in formset:
return render(request, 'rounds/create_games.html', {'tournament': t,
    'round': r, 'formset': formset})
send_board_call(r)
g, created = Game.objects.get_or_create(name=f.cleaned_data['game_name'],
    the_round=r, the_set=f.cleaned_data['the_set'])
g.full_clean()
f.add_error(None, e)
if created:
return HttpResponseRedirect(reverse('game_index', args=(tournament_id,
    round_num)))
g.delete()
g.save()
for power, field in f.cleaned_data.items():
return render(request, 'rounds/create_games.html', {'tournament': t,
    'round': r, 'formset': formset})
p = GreatPower.objects.get(name=power)
i = GamePlayer.objects.get(game=g, power=p)
i = GamePlayer(player=field.player, game=g, power=p)
i.player = field.player
i.full_clean()
f.add_error(None, e)
i.save()
i.delete()
return render(request, 'rounds/create_games.html', {'tournament': t,
    'round': r, 'formset': formset})
