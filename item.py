class Item(object):
	"""docstring for Item"""
	def __init__(self, Name,):
		super(Item, self).__init__()
		self.Name = Name


class Spell(Item):
	"""docstring for Spell"""
	def __init__(self, arg):
		super(Spell, self).__init__()
		self.arg = arg

class Masks(Item):
	"""docstring for Masks"""
	def __init__(self, arg):
		super(Masks, self).__init__()
		self.arg = arg


class Tasks(Item):
	"""docstring for Tasks"""
	def __init__(self, arg):
		super(Tasks, self).__init__()
		self.arg = arg


class Missions(Task):
	"""docstring for Missions"""
	def __init__(self, arg):
		super(Missions, self).__init__()
		self.arg = arg


class Tomes(Item):
	"""docstring for Tomes"""
	def __init__(self, arg):
		super(Tomes, self).__init__()
		self.arg = arg
		

class Weapons(Item):
	"""docstring for Weapons"""
	def __init__(self, arg):
		super(Weapons, self).__init__()
		self.arg = arg

		