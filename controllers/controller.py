from flask import render_template, request
from app import app
from modules.player import Player 
from modules.game import get_winning_choice



@app.route('/')
def index():
    return render_template("welcome.html", title = "Home")

@app.route('/game', methods= ['POST'])
def add_choice():
    add_choice1 = request.form["choice1"]
    add_choice2 = request.form["choice2"]
    new_choice = get_winning_choice(add_choice1, add_choice2)
    winner = f"the winner is {new_choice}"
    return render_template("index.html", title = "Game", victor = winner, choice1 = add_choice1, choice2 = add_choice2)


@app.route('/game')
def result(player_1, player_2):
    winner =  f"The winner is {get_winning_choice(player_1, player_2)}"
    return render_template("index.html", title = "Game", victor = winner)

    
    


