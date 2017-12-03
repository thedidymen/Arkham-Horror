class Gate(object):
	"""docstring for Gate"""
	def __init__(self, location, dimension, modifier, otherworld, name, expansion):
		super(Gate, self).__init__()
		self.location = location
		self.dimension = dimension
		self.modifier = modifier
		self.otherworld = otherworld
		self.name = self.otherworld.name
		self.expansion = expansion


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
		
		