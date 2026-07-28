""" The master Unit test set up. Each set of tests below should cover all
functional aspects of tournament.py. The original file tournament_test.py has
been rolled in here and its tests exist below. Most tests below are YAY/NAY
in that we're expecitng very specific results. In most cases, each function
in tournament.py returns a status code based on its behavior. These codes are
returned when non-critical events take place such as "no players found" when
trying to search for players.
"""
import time
import unittest
import psycopg2
import tournament
import tools
def connect():...
return psycopg2.connect(database='tournament', user='postgres')
