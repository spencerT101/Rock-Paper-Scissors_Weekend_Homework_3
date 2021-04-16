from flask import render_template, request
from app import app
from modules.player import Player 
from modules.game import Game

@app.route('/games/<player_1>/<player_2>')
def result(player_1, player_2):

    if result == "get_winning_choice":
        return f"The winner is {game.get_winning_choice}"
    
    else:
        return "Player 2 wins"


