class Investigatorlocation(object):
	"""docstring for Investigatorlocation"""
	def __init__(self, investigators):
		super(Investigatorlocation, self).__init__()
		self.investigators = investigators


class Monsterlocation(object):
	"""docstring for Monsterlocation"""
	def __init__(self, monsters):
		super(Monsterlocation, self).__init__()
		self.monsters = monsters
		
		
class Outskirt(Monsterlocation):
	"""docstring for Outskirt"""
	def __init__(self, name):
		super(Outskirt, self).__init__()
		self.name = name

class Sky(Monsterlocation):
	"""docstring for Sky"""
	def __init__(self, name):
		super(Sky, self).__init__()
		self.name = name
		

class Lostintimeandspace(Investigatorlocation):
	"""docstring for Lostintimeandspace"""
	def __init__(self, name):
		super(Lostintimeandspace, self).__init__()
		self.name = name
		

class location(Investigatorlocation, Monsterlocation):
	"""docstring for location"""
	def __init__(self, name, expansion):
		super(location, self).__init__()
		self.name = name
		self.expansion = expansion
		

class building(location):
	"""docstring for building"""
	def __init__(self, neighborhood, stability, encountertypes, ):
		super(building, self).__init__()
		self.neighborhood = neighborhood
		self.stability = stability
		if self.stability == False:
			self.gates = []
		self.EncouterArkham = deck()
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
		self.left = location(name=self.name, expansion=self.expansion)
		self.right = location(name=self.name, expansion=self.expansion)
		self.encoutersOtherworld = deck()
		