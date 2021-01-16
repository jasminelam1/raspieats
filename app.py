from flask import Flask, render_template
import raspieats
import catchem
 
app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/game')

def game():
    my_game = raspieats.Game()
    my_game.run()
    return "Game Ran"

@app.route('/game2')

def game2():
    return "Game2 Ran"





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')