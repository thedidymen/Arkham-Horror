class Monster(object):
	"""docstring for Monster"""
	def __init__(self, movement, toughness, dimension, expansion, horrorrating, horrordamage, combatrating, combatdamage, abilities, awareness, name, flavortext, text):
		super(Monster, self).__init__()
		self.movement = movement
		self.toughness = toughness
		self.dimension = dimension
		self.expansion = expansion
		self.horrorrating = horrorrating
		self.horrordamage = horrordamage
		self.combatrating = combatrating
		self.combatdamage = combatdamage
		self.abilities = abilities
		self.awareness = awareness
		self.name = name
		self.flavortext = flavortext
		self.text = text
		self.location = None
	def __repr__(self):
		return self.name
	def arrive(self, location):
		self.location = location
	def move(self, color):
		newlocation = self.location.exithastype(color)[0]
		newlocation.location.monsters.append(self.location.monsters.pop(self.location.monsters.index(self)))
		self.location = newlocation.location



class Yellow(Monster):
	"""docstring for Yellow"""
	def __init__(self, arg):
		super(Yellow, self).__init__()
		self.arg = arg


class Red(Monster):
	"""docstring for Ret"""
	def __init__(self, arg):
		super(Red, self).__init__()
		self.arg = arg


class Green(Monster):
	"""docstring for Green"""
	def __init__(self, arg):
		super(Green, self).__init__()
		self.arg = arg


class Blue(Monster):
	"""docstring for Blue"""
	def __init__(self, arg):
		super(Blue, self).__init__()
		self.arg = arg


class Purple(Monster):
	"""docstring for Purple"""
	def __init__(self, arg):
		super(Purple, self).__init__()
		self.arg = arg


class Orange(Monster):
	"""docstring for Orange"""
	def __init__(self, arg):
		super(Orange, self).__init__()
		self.arg = arg

														