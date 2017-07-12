class Ball():

	def __init__(self, x_pos, y_pos, x_vel=3, y_vel=3, radius=20):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.x_vel = x_vel
		self.y_vel = y_vel
		self.radius = radius


	def setScreenHeight(self, height):
		self.screen_height = height

	def setScreenWidth(self, width):
		self.screen_width = width

	def setXPos(self, x_pos):
		self.x_pos = x_pos

	def setYPos(self, y_pos):
		self.y_pos = y_pos

	def getXPos(self):
		return self.x_pos

	def getYPos(self):
		return self.y_pos

	def setXVel(self, x_vel):
		self.x_vel = x_vel

	def setYVel(self, y_vel):
		self.y_vel = y_vel

	def changeXVel(self):
		self.x_vel *= -1

	def setRadius(self, radius):
		self.radius = radius

	def getRadius(self):
		return self.radius
		
	def updatePosition(self):
		self.x_pos += self.x_vel
		self.y_pos += self.y_vel

		# collision of ball with top/bottom of screen
		if self.y_pos - self.radius <= 0 or self.y_pos + self.radius >= self.screen_height:
			self.y_vel *= -1

	def serve(self):
		self.x_pos = int(self.screen_width / 2)
		self.y_pos = int(self.screen_height / 2)
