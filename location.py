class Exits(object):
	"""docstring for Exits"""
	def __init__(self, exit={}):
		super(Exits, self).__init__()
		self.exits = exit
	def add(self, key, value):
		"""takes location object as key and a list as value"""
		self.exits[key] = value
	def __repr__(self):
		return "".join(['%s: %s \n' % (key, value) for (key, value) in self.exits.items()])
	def giveexit(self, color):
		"""takes a color (string), returns list of location with color connection."""
		return [location for location in self.exits.keys() if color in self.exits[location]]


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

	Locations = [
		    ["Arkham Horror", "Ye Olde Magick Shoppe"], 
		    ["Arkham Horror", "Woods"],
		    ["Arkham Horror", "Velma's Diner"],
		    ["Arkham Horror", "Unvisited Isle"],
		    ["Arkham Horror", "Train Station"],
		    ["Arkham Horror", "The Witch House"],
		    ["Arkham Horror", "The Unnamable"],
		    ["Arkham Horror", "St. Mary's Hospital"],
		    ["Arkham Horror", "South Church"],
		    ["Arkham Horror", "Silver Twilight Lodge"],
		    ["Arkham Horror", "Science Building"],
		    ["Arkham Horror", "River Docks"],
		    ["Arkham Horror", "Police Station"],
		    ["Arkham Horror", "Newspaper"],
		    ["Arkham Horror", "Ma's Boarding House"],
		    ["Arkham Horror", "Library"],
		    ["Arkham Horror", "Inner Sanctum"],
		    ["Arkham Horror", "Independence Square"],
		    ["Arkham Horror", "Administration Building"],
		    ["Arkham Horror", "Arkham Asylum"],
		    ["Arkham Horror", "Bank of Arkham"],
		    ["Arkham Horror", "Black Cave"],
		    ["Arkham Horror", "Curiositie Shoppe"],
		    ["Arkham Horror", "General Store"],
		    ["Arkham Horror", "Graveyard"],
		    ["Arkham Horror", "Hibb's Roadhouse"],
		    ["Arkham Horror", "Historical Society"],
		    ["Arkham Horror", "Northside"],
		    ["Arkham Horror", "Downtown"],
		    ["Arkham Horror", "Easttown"],
		    ["Arkham Horror", "Rivertown"],
		    ["Arkham Horror", "Miskatonic University"],
		    ["Arkham Horror", "French Hill"],
		    ["Arkham Horror", "Uptown"],
		    ["Arkham Horror", "Southside"],
		    ["Arkham Horror", "Merchant District"],
		]
	connections = [
	    ["Ye Olde Magick Shoppe", {"Uptown" : ['black', 'white'] }], 
	    ["Woods", {"Uptown" : ['black', 'white'] }],
	    ["Velma's Diner", {"Easttown" : ['black', 'white'] }],
	    ["Unvisited Isle", {"Merchant District" : ['black', 'white'] }],
	    ["Train Station", {"Northside" : ['black', 'white'] }],
	    ["The Witch House", {"French Hill" : ['black', 'white'] }],
	    ["The Unnamable", {"Merchant District" : ['black', 'white'] }],
	    ["St. Mary's Hospital", {"Uptown" : ['black', 'white'] }],
	    ["South Church", {"Southside" : ['black', 'white'] }],
	    ["Silver Twilight Lodge", {"French Hill" : ['black', 'white'] }],
	    ["Science Building", {"Miskatonic University" : ['black', 'white'] }],
	    ["River Docks", {"Merchant District" : ['black', 'white'] }],
	    ["Police Station", {"Easttown" : ['black', 'white'] }],
	    ["Newspaper", {"Northside" : ['black', 'white'] }],
	    ["Ma's Boarding House", {"Southside" : ['black', 'white'] }],
	    ["Library", {"Miskatonic University" : ['black', 'white'] }],
	    ["Inner Sanctum", {"French Hill" : ['black', 'white'] }],
	    ["Independence Square", {"Downtown" : ['black', 'white'] }],
	    ["Administration Building", {"Miskatonic University" : ['black', 'white'] }],
	    ["Arkham Asylum", {"Downtown" : ['black', 'white'] }],
	    ["Bank of Arkham", {"Downtown" : ['black', 'white'] }],
	    ["Black Cave", {"Rivertown" : ['black', 'white'] }],
	    ["Curiositie Shoppe", {"Northside" : ['black', 'white'] }],
	    ["General Store", {"Rivertown" : ['black', 'white'] }],
	    ["Graveyard", {"Rivertown" : ['black', 'white'] }],
	    ["Hibb's Roadhouse", {"Easttown" : ['black', 'white'] }],
	    ["Historical Society", {"Southside" : ['black', 'white'] }],
	    ["Northside", {"Downtown" : ['white'], "Merchant District" : ['black'] }],
	    ["Downtown", {"Merchant District": [], "Easttown" : ['white'], "Northside" : ['black'] }],
	    ["Easttown", {"Rivertown" : ['white'], "Downtown" : ['black'] }],
	    ["Rivertown", {"Merchant District": [], "French Hill" : ['white'], "Easttown" : ['black'] }],
	    ["Miskatonic University", {"Merchant District" : ['white'], "Uptown" : ['black'] }],
	    ["French Hill", {"French Hill" : ['white'], "Easttown" : ['black'] }],
	    ["Uptown", {"Miskatonic University" : ['white'], "Southside" : ['black'] }],
	    ["Southside", {"Uptown" : ['white'], "French Hill" : ['black'] }],
	    ["Merchant District", {"Downtown": [], "Rivertown": [], "Northside" : ['white'], "Miskatonic University" : ['black'] }],
		]

	# print Locations
	print connections

	loc = []
	for l in Locations:
		print l[0], l[1]
		loc.append(location(expansion=l[0], name=l[1]))
	

