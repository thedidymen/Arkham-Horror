# class Exits(object):
# 	"""docstring for Exits"""
# 	def __init__(self):
# 		super(Exits, self).__init__()
# 		self.exits = {}
# 	def add(self, key, value):
# 		"""takes location object as key and a list as value"""
# 		self.exits[key] = value
# 		return
# 	def __repr__(self):
# 		return "".join(['%s: %s \n' % (key, value) for (key, value) in self.exits.items()])
# 	def giveexit(self, color):
# 		"""takes a color (string), returns list of location with color connection."""
# 		return [location for location in self.exits.keys() if color in self.exits[location]]




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
		self.exits = []
	def __repr__(self):
		return self.name
	def monsterinlocation(self):
		"""returns True if monster in location, else False"""
		if hasattr(self, 'self.monsters'):
			return len(self.monsters) > 0
		else:
			return False
	def gateinlocation(self):
		"""returns True if gate in location, else False"""
		return self.gates != None
	def arrive(self, investigator):
		"""appends investigator to locations investigatorlist"""
		self.investigators.append(investigator)
	def depart(self, investigator):
		"""Pops investigator form locations investigatorlist and returns the investigator"""
		self.investigators.remove(investigator)

		
		
class Outskirt(location):
	"""docstring for Outskirt"""
	def __init__(self, name, expansion, investgatorlocation=False):
		super(Outskirt, self).__init__(name)


class Sky(location):
	"""docstring for Sky"""
	def __init__(self, name, expansion, investgatorlocation=False):
		super(Sky, self).__init__(name)
		

class Lostintimeandspace(location):
	"""docstring for Lostintimeandspace"""
	def __init__(self, name, expansion, monsterlocation=False):
		super(Lostintimeandspace, self).__init__(name, expansion)
		

class building(location):
	"""docstring for building"""
	def __init__(self, name, expansion, neighborhood, stability):
		super(building, self).__init__(name, expansion)
		self.neighborhood = neighborhood
		self.stability = stability
		if self.stability == False:
			self.seal = False
		self.gate = None
		# self.EncouterArkham = deck()
		self.open = True
		#self.buildingaction = buildingaction
	def opengate(self, gate):
		self.gate = gate

		

class street(location):
	"""docstring for street"""
	def __init__(self, name, expansion, neighborhood):
		super(street, self).__init__(name, expansion)
		self.neighborhood = neighborhood
		self.gate = None

		
class otherworld(object):
	"""docstring for otherworld"""
	def __init__(self, colors, name, expansion):
		super(otherworld, self).__init__()
		self.colors = colors
		self.name = name
		self.expansion = expansion
		self.left = []
		self.right = []
		self.gateexits = []
		# self.encoutersOtherworld = deck()
	def __repr__(self):
		return self.name
	def arriveleft(self, investigator):
		"""appends investigator to otherworld left location"""
		self.left.append(investigator)
	def departleft(self, investigator):
		"""Pops investigator form otherworld left location"""
		self.left.remove(investigator)
	def arriveright(self, investigator):
		"""appends investigator to otherworld right location"""
		self.right.append(investigator)
	def departright(self, investigator):
		"""Pops investigator form otherworld right location"""
		self.right.remove(investigator)





# if __name__ == '__main__':
	# Warpnet = location(name="Warpnet", expansion="Akrham Horror")
	# Foodfellas = location(name="Foodfellas", expansion="Akrham Horror")
	# Steenhouwerskade = location(name="Steenhouwerskade", expansion="Akrham Horror")
	# Warpnet.exits.add(Foodfellas, ['black', 'white'])
	# Foodfellas.exits.add(Warpnet, [])
	# print Warpnet
	# print Foodfellas
	# print Steenhouwerskade
	# print Warpnet.exits
	# print Foodfellas.exits
	# print Steenhouwerskade.exits
	# print Warpnet.exits.giveexit("black")[0].expansion
	# print Warpnet.exits.giveexit("black")
	# print Foodfellas.exits.giveexit('black')

if __name__ == '__main__':
	loc = [location(expansion=l[0], name=l[1]) for l in Locations]
	for n in range(len(loc)):
		if loc[n].name == connections[n][0]:
			for connectedlocation in connections[n][1].keys():
				for i in loc:
					if i.name == connectedlocation:
						clobj = i
						break
				loc[n].exits.append(connection(location=clobj, colors=connections[n][1][connectedlocation]))
	for n in loc:
		print
		print n.name
		print "exits into"
		for m in n.exits:
			print m
