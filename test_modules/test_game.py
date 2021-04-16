import unittest
from modules.game import *
from modules.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.rock = Player("John", "rock")
        self.scissors = Player("Sophie", "scissors")
    

    def test_same_player_choice_equals_None(self):
        result = Game.get_winning_choice(self.rock,self.rock)
        self.assertEqual(None, result)

    def test_rock_beats_scissors(self):
        result = Game.get_winning_choice(self.rock, self.scissors)
        self.assertEqual(self.rock, result)
    
    def test_scissors_loses_to_rock(self):
        result = Game.get_winning_choice(self.scissors, self.rock)
        self.assertEqual(self.rock, result)
    
    def 

    


    


     
    



