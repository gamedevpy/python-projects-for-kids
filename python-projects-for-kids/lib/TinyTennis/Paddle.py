class Paddle():

	def __init__(self, x_pos, y_pos, width=25, height=25):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.width = width
		self.height = height
		

	def setHeight(self, height):
		self.height = height

	def setWidth(self, width):
		self.width = width

	def getHeight(self):
		return self.height

	def getWidth(self):
		return self.width

	def setXPos(self, x_pos):
		self.x_pos = x_pos

	def setYPos(self, y_pos):
		self.y_pos = y_pos

	def getXPos(self):
		return self.x_pos

	def getYPos(self):
		return self.y_pos

	def setScreenHeight(self, height):
		self.screen_height = height

	def moveDown(self):
		self.y_pos -= 5

	def moveUp(self):
		self.y_pos += 5


	def updateVerticalPosition(self):
		# collision of paddle with top/bottom of screen
		if self.y_pos < 0:
			self.y_pos = 0
		elif self.y_pos + self.height > self.screen_height:
			self.y_pos = self.screen_height - self.height
