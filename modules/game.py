from modules.player import Player

def get_winning_choice(player_1, player_2):
    if player_1 == player_2:
        return None
        
    if player_1 == "rock":
        if player_2 == "scissors" or player_2 == "bazooka":
            return player_1
        
    if player_1 == "scissors":
        if player_2 == "paper" or player_2 == "bazooka":
            return player_1
        
    if player_1 == "paper":
        if player_2 == "rock" or player_2 == "bazooka":
            return player_1
        
    return player_2

