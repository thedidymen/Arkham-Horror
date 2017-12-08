class Game(object):
	"""docstring for Game"""
	def __init__(self):
		super(Game, self).__init__()
		self.investigators = []
		self.locations =[]
		self.gates = []
		self.monstercup = []
		self.monsteringame = []
		self.commonitems = deck()
		self.uniqueitems = deck()
		self.spells = deck()
		self.hospitals = [] # wont change during game, easier te set up once?
		self.asylums = [] # wont change during game, easier te set up once?
	def LoadingGame():
	"""sets up the game. takes investigators, expansions. does not check compatiblity?"""
	def Victory():
		"""
		returns True when winning condition is achieved else False
		Victory is achieved by 6 seals on the board or with no gates on the board and #Gatethrophies >= #investigators
		"""
	def Endgameandfinalscore():
		"""calculates final score and closes cleans the game"""
	def AncientOneAwake():
		"""returns True when Ancient One is awake else False"""
	def recallmonsters(dimension):
		"""returns all monsters with dimension symbool to the monstercup"""
	def FinalBattle():
		"""When Ancient One awakes this initiates Final Battle based on game status. kicking off new class?"""
	def Start():
		"""loops over phases and whitin each phase (except Mythos) over the investigators, until Victory or AncientOneAwake is 
		True. and kicks off appropriate subroutine."""