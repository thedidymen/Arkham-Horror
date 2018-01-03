class connection(object):
	"""docstring for connection"""
	def __init__(self, location, connectiontype):
		super(connection, self).__init__()
		self.location = location
		self.connectiontype = connectiontype
	def __repr__(self):
		return str(self.location) + ": " + ", ".join([n for n in self.connectiontype])


class Gate(connection):
	"""docstring for Gate"""
	def __init__(self, dimension, modifier, location, name, expansion, connectiontype):
		super(Gate, self).__init__(location, connectiontype)
		self.dimension = dimension
		self.modifier = modifier
		self.arkhamlocation = None
		self.name = location.name
		self.expansion = expansion
		self.explored = []
	def __repr__(self):
		return str(self.arkhamlocation) + " to " + str(self.location)
	def arkhamopen(self, arkhamlocation):
		self.arkhamlocation = arkhamlocation


class DevouringGate(Gate):
	"""docstring for DevouringGate"""
	def __init__(self, arg):
		super(DevouringGate, self).__init__()
		self.arg = arg


class SplitGate(object):
	"""docstring for SplitGate"""
	def __init__(self, Otherworld1, otherworld2):
		super(SplitGate, self).__init__()
		self.Otherworld1 = Otherworld1
		self.otherworld2 = otherworld2


class GateofDoom(Gate):
	"""docstring for GateofDoom"""
	def __init__(self, arg):
		super(GateofDoom, self).__init__()
		self.arg = arg


class EndlessGate(Gate):
	"""docstring for EndlessGate"""
	def __init__(self, arg):
		super(EndlessGate, self).__init__()
		self.arg = arg
		

class MonstrousGate(Gate):
	"""docstring for MonstrousGate"""
	def __init__(self, arg):
		super(MonstrousGate, self).__init__()
		self.arg = arg
		

class GateofBlood(Gate):
	"""docstring for GateofBlood"""
	def __init__(self, arg):
		super(GateofBlood, self).__init__()
		self.arg = arg
		

class GateofMadness(Gate):
	"""docstring for GateofMadness"""
	def __init__(self, arg):
		super(GateofMadness, self).__init__()
		self.arg = arg


class MovingGate(Gate):
	"""docstring for MovingGate"""
	def __init__(self, arg):
		super(MovingGate, self).__init__()
		self.arg = arg
		
		