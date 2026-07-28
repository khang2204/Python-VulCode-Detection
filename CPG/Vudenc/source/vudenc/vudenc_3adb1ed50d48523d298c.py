@permission_required('tournament.add_game')...
"""docstring"""
t = get_modifiable_tournament_or_404(tournament_id, request.user)
r = get_round_or_404(t, round_num)
if request.method == 'POST':
PowerAssignFormset = formset_factory(PowerAssignForm, formset=
    BasePowerAssignFormset, extra=0)
r.game_set.all().delete()
formset = PowerAssignFormset(request.POST, the_round=r)
default_set = GameSet.objects.get(pk=1)
if formset.is_valid():
data = []
for f in formset:
context = {'tournament': t, 'round': r, 'games': games, 'formset': formset}
if t.power_assignment == Tournament.AUTO:
g = f.game
send_board_call(r)
return render(request, 'rounds/seeded_games.html', context)
games = _seed_games_and_powers(t, r)
games = _seed_games(t, r)
g.name = f.cleaned_data['game_name']
return HttpResponseRedirect(reverse('game_index', args=(tournament_id,
    round_num)))
for i, g in enumerate(games, start=1):
for i, g in enumerate(games, start=1):
g.the_set = f.cleaned_data['the_set']
new_game = Game.objects.create(name='R%sG%d' % (round_num, i), the_round=r,
    the_set=default_set)
PowerAssignFormset = formset_factory(PowerAssignForm, formset=
    BasePowerAssignFormset, extra=0)
new_game = Game.objects.create(name='R%sG%d' % (round_num, i), the_round=r,
    the_set=default_set)
g.full_clean()
f.add_error(None, e)
g.save()
current = {'game_name': new_game.name, 'the_set': new_game.the_set}
formset = PowerAssignFormset(the_round=r, initial=data)
current = {'game_name': new_game.name, 'the_set': new_game.the_set}
return render(request, 'rounds/seeded_games.html', {'tournament': t,
    'round': r, 'formset': formset})
for gp_id, field in f.cleaned_data.items():
for tp, power in g:
for tp in g:
if gp_id in ['the_set', 'game_name']:
gp = GamePlayer.objects.create(player=tp.player, game=new_game, power=power)
data.append(current)
gp = GamePlayer.objects.create(player=tp.player, game=new_game)
if t.power_assignment == Tournament.PREFERENCES:
gp = GamePlayer.objects.get(id=gp_id)
current[gp.id] = power
new_game.assign_powers_from_prefs()
for tp in g:
gp.power = field
gp = GamePlayer.objects.get(player=tp.player, game=new_game)
data.append(current)
gp.full_clean()
f.add_error(None, e)
gp.save()
current[gp.id] = gp.power
return render(request, 'rounds/seeded_games.html', {'tournament': t,
    'round': r, 'formset': formset})
