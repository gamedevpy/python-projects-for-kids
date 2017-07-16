class Screen():

	def __init__(self, width=600, height=400):
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