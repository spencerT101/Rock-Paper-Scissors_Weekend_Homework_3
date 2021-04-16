import unittest
from modules.game import *
from modules.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.rock = Player("John", "rock")
        self.scissors = Player("Sophie", "scissors")
        self.paper = Player("Peter", "paper")
        self.bazooka = Player("Barry", "bazooka")
    

    def test_same_player_choice_equals_None(self):
        result = Game.get_winning_choice(self.rock,self.rock)
        self.assertEqual(None, result)

    def test_rock_beats_scissors(self):
        result = Game.get_winning_choice(self.rock, self.scissors)
        self.assertEqual(self.rock, result)
    
    def test_scissors_loses_to_rock(self):
        result = Game.get_winning_choice(self.scissors, self.rock)
        self.assertEqual(self.rock, result)
    
    def test_rock_beats_bazooka(self):
        result = Game.get_winning_choice(self.rock, self.bazooka)
        self.assertEqual(self.rock, result)
    
    def test_bazooka_loses_to_rock(self):
        result = Game.get_winning_choice(self.bazooka, self.rock)
        self.assertEqual(self.rock, result)
    
    def test_scissors_beats_paper(self):
        result = Game.get_winning_choice(self.scissors, self.paper)
        self.assertEqual(self.scissors, result)
    
    def test_paper_loses_to_scissors(self):
        result = Game.get_winning_choice(self.paper, self.scissors)
        self.assertEqual(self.scissors, result)
    
    def test_scissors_beats_bazooka(self):
        result = Game.get_winning_choice(self.scissors, self.bazooka)
        self.assertEqual(self.scissors, result)
    
    def test_bazooka_loses_to_scissors(self):
        result = Game.get_winning_choice(self.bazooka, self.scissors)
        self.assertEqual(self.scissors, result)
    


    


     
    



