class Game:


    def get_winning_choice(player_1, player_2):

        if player_1.choice == player_2.choice:
            return None
        
        if player_1.choice == "rock" and player_2.choice == "scissors":
            return player_1
        
        
        return player_2
    

     