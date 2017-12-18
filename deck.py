import random

class Deck(object):
	"""docstring for Deck"""
	def __init__(self, name, Cards=[], Discardpile=[]):
		super(Deck, self).__init__()
		self.name = name
		self.Cards = Cards
		self.Discardpile = Discardpile
	def __repr__(self):
		return "Deck of " + self.name
	def drawCard(self):
		"""returns top card"""
		return self.Cards.pop(0)
	def shuffleDeck(self):
		"""combines discardpile and cards and shuffles them"""
		random.shuffle(self.Cards)
	def bottomDraw(self, n):
		"""Returns bottom n cards as objects in list"""

class card(object):
	"""docstring for card"""
	def __init__(self):
		super(card, self).__init__()
		
class Mythos(card):
	"""docstring for Mythos"""
	def __init__(self, title, expansion, mtype, subtype, gatelocation, cluelocation, whitedimension, blackdimension, text):
		super(Mythos, self).__init__()
		self.title = title
		self.expansion = expansion
		self.mtype = mtype
		self.subtype = subtype
		self.gatelocation = gatelocation
		self.cluelocation = cluelocation
		self.whitedimension = whitedimension
		self.blackdimension = blackdimension
		self.text = text
	def __repr__(self):
			# return "\n".join([self.title, self.mtype, self.subtype, str(self.gatelocation), str(self.cluelocation), str(self.whitedimension), str(self.blackdimension)])
		return self.title		

		