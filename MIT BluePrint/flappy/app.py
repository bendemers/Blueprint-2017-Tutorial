from flask import Flask 
from flask import render_template	
from operator import itemgetter

app= Flask("Flappy Bird")


class Leaderboard:
	def __init__(self):
		self.scores = []
		self.capacity = 10

	def submit_score(self, name, score):
		self.scores.append((name, score))
		self.scores = sorted(self.scores, key=itemgetter(1), reverse=True)
		if len(self.scores) > self.capacity:
			self.scores.pop(self.capacity)

leaderboard = Leaderboard()
leaderboard.submit_score("Jeff", 5)
leaderboard.submit_score("Tim", 2)
leaderboard.submit_score("Austin", 10)

@app.route("/")	
def home():

	    return render_template("index.html", scores=leaderboard.scores)

if __name__ == "__main__":
    app.run()