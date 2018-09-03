class Cell:
	def __init__(self, pos=(0, 0), vel=(1, 0)):
		self.position = pos
		self.velocity = vel
		self.stack = []

	def step(self, cell=None):
		x, y = self.position
		dx, dy = self.velocity
		self.position = (x + dx, y + dy)

	def interact(self, cell):
		pass

	def operate(self):
		pass

	def output(self):
		pass