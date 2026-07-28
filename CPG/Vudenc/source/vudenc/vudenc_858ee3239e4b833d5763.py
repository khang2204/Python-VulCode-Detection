@permission_required('tournament.change_gameplayer')...
"""docstring"""
t = get_modifiable_tournament_or_404(tournament_id, request.user)
r = get_round_or_404(t, round_num)
GameScoreFormset = formset_factory(GameScoreForm, extra=0)
data = []
the_list = r.game_set.all()
for game in the_list:
content = {'game_name': game.name}
formset = GameScoreFormset(request.POST or None, initial=data)
for gp in game.gameplayer_set.all():
if formset.is_valid():
content[gp.power.name] = gp.score
data.append(content)
for f in formset:
return render(request, 'rounds/game_score.html', {'tournament': t, 'round':
    round_num, 'formset': formset})
g = Game.objects.get(name=f.cleaned_data['game_name'], the_round=r)
return HttpResponseRedirect(reverse('round_index', args=tournament_id))
for power, field in f.cleaned_data.items():
p = GreatPower.objects.get(name=power)
i = GamePlayer.objects.get(game=g, power=p)
i.score = field
i.full_clean()
f.add_error(None, e)
i.save()
return render(request, 'rounds/game_score.html', {'tournament': t, 'round':
    round_num, 'formset': formset})
