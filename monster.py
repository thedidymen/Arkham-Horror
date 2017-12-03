class Monster(object):
	"""docstring for Monster"""
	def __init__(self, movement, toughness, dimension, type, expansion, horrorrating, horrordamage, combatrating, combatdamage, abilities, awareness, name, flavortext, text):
		super(Monster, self).__init__()
		self.movement = movement
		self.toughness = toughness
		self.dimension = dimension
		self.type = type
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
		