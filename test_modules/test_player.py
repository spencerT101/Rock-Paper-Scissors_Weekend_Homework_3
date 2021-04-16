import unittest
from modules.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("John", "rock")
        self.player_2 = Player("Sophie", "scissors")
    

    def test_player_has_name(self):
        self.assertEqual("John", self.player_1.name)
    
    def test_player_has_choice(self):
        self.assertEqual("scissors", self.player_2.choice)