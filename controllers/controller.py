from flask import render_template, request
from app import app
from modules.player import Player 
from modules.game import get_winning_choice

@app.route('/games/<player_1>/<player_2>')

def result(player_1, player_2):
    return f"The winner is {get_winning_choice(player_1, player_2)}"
    
    


