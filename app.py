from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# In-memory storage for game sessions and player responses
games = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_game', methods=['POST'])
def create_game():
    game_id = random.randint(1000, 9999)
    games[game_id] = {'players': [], 'responses': []}
    return redirect(url_for('game', game_id=game_id))

@app.route('/game/<int:game_id>')
def game(game_id):
    return render_template('game.html', game_id=game_id)

@app.route('/submit_response', methods=['POST'])
def submit_response():
    game_id = request.form.get('game_id')
    player_name = request.form.get('player_name')
    response = request.form.get('response')
    games[game_id]['responses'].append((player_name, response))
    return redirect(url_for('game', game_id=game_id))

if __name__ == '__main__':
    app.run(debug=True)
