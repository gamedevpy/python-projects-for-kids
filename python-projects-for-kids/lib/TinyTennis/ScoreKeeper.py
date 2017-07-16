class ScoreKeeper():

	def __init__(self):
		self.player1_score = 0
		self.player2_score = 0
		

	def incrementPlayer1Score(self):
		self.player1_score += 1

	def incrementPlayer2Score(self):
		self.player2_score += 1

	def getPlayer1Score(self):
		return self.player1_score

	def getPlayer2Score(self):
		return self.player2_score