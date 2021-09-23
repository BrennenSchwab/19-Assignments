from boggle import Boggle
from flask import Flask, request, render_template, jsonify, session

boggle_game = Boggle()

app = Flask(__name__)
app.config["SECRET_KEY"] = "whateverthisis9182"

@app.route("/")
def get_board():
    """Display the Board here."""
    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get("highscore", 0)
    plays = session.get("plays", 0)
    return render_template("index.html", board=board, highscore=highscore, plays=plays)


@app.route("/check-word")
def check_word():
    """Check validity of word according to words.txt"""

    word = request.args["word"]
    board = session["board"]
    resp = boggle_game.check_valid_word(board, word)
    return jsonify({'result': resp})

@app.route("/post-score", methods=["POST"])
def post_score():
    """Get your score, update the highscore (if necessary) and amount of plays"""

    score = request.json["score"]
    highscore = session.get("highscore", 0)
    plays = session.get("plays", 0)
    session['plays'] = plays + 1
    session['highscore'] = max(score, highscore)
    return jsonify(newRecord= score > highscore)
    