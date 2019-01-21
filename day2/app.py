from flask import Flask, url_for, render_template, redirect, session
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    if "board" not in session:
        # 3x3 of Nones is the board
        reset()

    return render_template("game.html", game=session["board"], turn=session["turn"], game_over=session["game_over"])

@app.route("/play/<int:row>/<int:col>")
def play(row, col):

    if "turn" not in session:
        reset()

    player = session["turn"]

    # game logic

    if session["game_over"] != None:
        return redirect(url_for('index'))

    # validate, play move
    if session["board"][row][col] != None:
        return redirect(url_for('index'))
    else:
        session["board"][row][col] = player
        if player == "X":
            session["turn"] = "O"
        elif player == "O":
            session["turn"] = "X"
        else:
            x = 1 / 0

    # check for a win
    for x in range(3):
        row_check = 0
        col_check = 0
        for y in range(3):
            if session["board"][x][y] == player:
                row_check += 1
            if session["board"][y][x] == player:
                col_check += 1
        
        if col_check == 3 or row_check == 3:
            session["game_over"] = player
            return redirect(url_for('index'))

    diag1_check = 0
    diag2_check = 0
    for i in range(3):
        if session["board"][i][i] == player:
            diag1_check += 1
        if session["board"][i][2-i] == player:
            diag2_check += 1
    if diag1_check == 3 or diag2_check == 3:
        session["game_over"] = player
        return redirect(url_for('index'))

    return redirect(url_for('index'))

@app.route('/play/reset')
def reset():
    session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
    session["turn"] = "X"
    session["game_over"] = None
    return redirect(url_for('index'))
