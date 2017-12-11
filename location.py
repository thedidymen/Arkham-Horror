class Exits(object):
	"""docstring for Exits"""
	def __init__(self, exit={}):
		super(Exits, self).__init__()
		self.exits = exit
	def add(self, key, value):
		"""takes location object as key and a list as value"""
		self.exits[key] = value
	def __repr__(self):
		s = ""
		return s.join(['%s: %s \n' % (key, value) for (key, value) in self.exits.items()])





class location(object):
	"""docstring for location"""
	def __init__(self, name, expansion, investgatorlocation=True, monsterlocation=True):
		super(location, self).__init__()
		self.name = name
		self.expansion = expansion
		if investgatorlocation == True:
			self.investigators = []
		if monsterlocation == True:
			self.monsters = []
		self.exits = Exits()
	def __repr__(self):
		return self.name
		
		
class Outskirt(location):
	"""docstring for Outskirt"""
	def __init__(self, name, investgatorlocation=False):
		super(Outskirt, self).__init__()


class Sky(location):
	"""docstring for Sky"""
	def __init__(self, name, investgatorlocation=False):
		super(Sky, self).__init__()
		

class Lostintimeandspace(location):
	"""docstring for Lostintimeandspace"""
	def __init__(self, name, monsterlocation=False):
		super(Lostintimeandspace, self).__init__()
		

class building(location):
	"""docstring for building"""
	def __init__(self, neighborhood, stability, encountertypes, ):
		super(building, self).__init__()
		self.neighborhood = neighborhood
		self.stability = stability
		if self.stability == False:
			self.gates = []
			self.seal = False
		self.EncouterArkham = deck()
		self.open = True
		#self.buildingaction = buildingaction
		

class street(location):
	"""docstring for street"""
	def __init__(self, neighborhood, ):
		super(street, self).__init__()
		self.neighborhood = neighborhood
		self.gates = []

		
class otherworld(object):
	"""docstring for otherworld"""
	def __init__(self, colors, name, expansion):
		super(otherworld, self).__init__()
		self.colors = colors
		self.name = name
		self.expansion = expansion
		self.left = []
		self.right = []
		self.encoutersOtherworld = deck()


if __name__ == '__main__':
	Warpnet = location(name="Warpnet", expansion="Akrham Horror")
	Foodfellas = location(name="Foodfellas", expansion="Akrham Horror")
	Steenhouwerskade = location(name="Steenhouwerskade", expansion="Akrham Horror")
	Warpnet.exits.add(Foodfellas, ['black', 'white'])
	Foodfellas.exits.add(Warpnet, [])
	print Warpnet
	print Foodfellas
	print Steenhouwerskade
	print Warpnet.exits
	print Foodfellas.exits
	print Steenhouwerskade.exits

