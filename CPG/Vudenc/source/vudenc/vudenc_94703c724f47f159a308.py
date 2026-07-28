"""
Round Views for the Diplomacy Tournament Visualiser.
"""
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import ValidationError
from django.forms.formsets import formset_factory
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import ugettext as _
from tournament.forms import BaseGamePlayersFormset
from tournament.forms import BasePlayerRoundFormset
from tournament.forms import BasePowerAssignFormset
from tournament.forms import GamePlayersForm
from tournament.forms import GameScoreForm
from tournament.forms import GetSevenPlayersForm
from tournament.forms import PlayerRoundForm
from tournament.forms import PowerAssignForm
from tournament.tournament_views import get_modifiable_tournament_or_404
from tournament.tournament_views import get_visible_tournament_or_404
from tournament.diplomacy import GreatPower, GameSet
from tournament.email import send_board_call
from tournament.game_seeder import GameSeeder
from tournament.models import Tournament, Round, Game
from tournament.models import TournamentPlayer, RoundPlayer, GamePlayer
def get_round_or_404(tournament, round_num):...
"""docstring"""
return tournament.round_numbered(round_num)
def round_simple(request, tournament_id, round_num, template):...
"""docstring"""
t = get_visible_tournament_or_404(tournament_id, request.user)
r = get_round_or_404(t, round_num)
context = {'tournament': t, 'round': r}
return render(request, 'rounds/%s.html' % template, context)
