class Mythos(object):
	"""docstring for Mythos"""
	def __init__(self, arg):
		super(Mythos, self).__init__()
		self.arg = arg
		

class Environment(Mythos):
	"""docstring for Environment"""
	def __init__(self, arg):
		super(Environment, self).__init__()
		self.arg = arg
		

class Headline(Mythos):
	"""docstring for Headline"""
	def __init__(self, arg):
		super(Headline, self).__init__()
		self.arg = arg


class Rumor(Mythos):
	"""docstring for Rumor"""
	def __init__(self, arg):
		super(Rumor, self).__init__()
		self.arg = arg


class Mystic(Environment):
	"""docstring for Mystic"""
	def __init__(self, arg):
		super(Mystic, self).__init__()
		self.arg = arg


class Urban(Environment):
	"""docstring for Urban"""
	def __init__(self, arg):
		super(Urban, self).__init__()
		self.arg = arg


class Weather(Enviroment):
	"""docstring for Weather"""
	def __init__(self, arg):
		super(Weather, self).__init__()
		self.arg = arg
