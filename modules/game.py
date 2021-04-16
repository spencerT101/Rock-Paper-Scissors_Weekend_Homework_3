class Game:


    def get_winning_choice(player_1, player_2):

        if player_1.choice == player_2.choice:
            return None
        
        if player_1.choice == "rock":
            if player_2.choice == "scissors" or player_2.choice == "bazooka":
                return player_1
        
        if player_1.choice == "scissors":
            if player_2.choice == "paper" or player_2.choice == "bazooka":
                return player_1
    
        
        
        return player_2
    

     