"""
Download and prepare training and fixtures data 
from various leagues.
"""
from os.path import join
from itertools import product
from difflib import SequenceMatcher
from sqlite3 import connect
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from scipy.stats import hmean
import numpy as np
import pandas as pd
from sportsbet import SOCCER_PATH
from sportsbet.soccer import TARGET_TYPES_MAPPING
DB_CONNECTION = connect(join(SOCCER_PATH, 'soccer.db'))
LEAGUES_MAPPING = {'E0': 'Barclays Premier League', 'B1':
    'Belgian Jupiler League', 'N1': 'Dutch Eredivisie', 'E1':
    'English League Championship', 'E2': 'English League One', 'E3':
    'English League Two', 'F1': 'French Ligue 1', 'F2': 'French Ligue 2',
    'D1': 'German Bundesliga', 'D2': 'German 2. Bundesliga', 'G1':
    'Greek Super League', 'I1': 'Italy Serie A', 'I2': 'Italy Serie B',
    'P1': 'Portuguese Liga', 'SC0': 'Scottish Premiership', 'SP1':
    'Spanish Primera Division', 'SP2': 'Spanish Segunda Division', 'T1':
    'Turkish Turkcell Super Lig'}
def combine_odds(odds, target_types):...
"""docstring"""
combined_odds = 1 / pd.concat([(1 / odds[target_type]) for target_type in
    target_types], axis=1).sum(axis=1)
combined_odds.name = '+'.join(target_types)
return pd.concat([odds, combined_odds], axis=1)
