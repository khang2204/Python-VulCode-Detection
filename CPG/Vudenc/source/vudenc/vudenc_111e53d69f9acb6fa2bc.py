def game_index(request, tournament_id, round_num):...
"""docstring"""
t = get_visible_tournament_or_404(tournament_id, request.user)
r = get_round_or_404(t, round_num)
the_list = r.game_set.all()
context = {'round': r, 'game_list': the_list}
return render(request, 'games/index.html', context)
