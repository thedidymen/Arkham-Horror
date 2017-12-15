import investigator as inv
import phases as ph
import location as loc
import data
import skill 


class Game(object):
	"""docstring for Game"""
	def __init__(self):
		super(Game, self).__init__()
		self.phases = [ph.Upkeep(self), ph.Movement(self), ph.ArkhamEncounter(self), ph.OtherWorldEncounters(self)]
		self.mythos = ph.Mythos(self)
		self.investigators = []
		self.locations = []
		self.gates = []
		self.monstercup = []
		self.monsteringame = []
		# self.commonitems = deck()
		# self.uniqueitems = deck()
		# self.spells = deck()
		# self.hospitals = [] # wont change during game, easier to set up once?
		# self.asylums = [] # wont change during game, easier to set up once?
		# self.monsterlimit = 0 # #investigators + 3, can change during the game
		# self.terrorlevel = 0 
	def newstartingplayer(self):
		"""puts current starting player at end of list"""
		self.investigators.append(self.investigators.pop(0))
	def LoadingGame(self):
		"""sets up the game. takes investigators, expansions. does not check compatiblity?"""
	def Victory(self):
		"""
		returns True when winning condition is achieved else False
		Victory is achieved by 6 seals on the board or with no gates on the board and #Gatethrophies >= #investigators
		"""
	def Endgameandfinalscore(self):
		"""calculates final score and closes cleans the game"""
	def AncientOneAwake(self):
		"""returns True when Ancient One is awake else False"""
	def recallmonsters(self, dimension):
		"""returns all monsters with dimension symbool to the monstercup"""
	def FinalBattle(self):
		"""When Ancient One awakes this initiates Final Battle based on game status. kicking off new class?"""
	def Start(self):
		"""loops over phases and whitin each phase (except Mythos) over the investigators, until Victory or AncientOneAwake is 
		True. and kicks off appropriate subroutine."""
		for i in range(100):
			print "Round: ", i
			for phase in self.phases:
				for investigator in self.investigators:
					phase.start(investigator)
					if self.Victory():
						self.Endgameandfinalscore()
					elif self.AncientOneAwake():
						self.FinalBattle()
			self.mythos.start()
			self.newstartingplayer()
	# temp:
	def getlocation(self, locationstr):
		"""takes a location string, returns location object. probably needs to move to the game loading class thingy"""
		for location in self.locations:
			if location.name == locationstr:
				return location
		return




if __name__ == '__main__':
	Agame = Game()

	Agame.locations = [loc.location(expansion=l[0], name=l[1]) for l in data.Locations]
	for n in range(len(Agame.locations)):
		if Agame.locations[n].name == data.connections[n][0]:
			for connectedlocation in data.connections[n][1].keys():
				for i in Agame.locations:
					if i.name == connectedlocation:
						clobj = i
						break
				Agame.locations[n].exits.append(loc.connection(location=clobj, colors=data.connections[n][1][connectedlocation]))

	for investigator in data.Investigatordata:
		Agame.investigators.append(inv.Investigator(forename=investigator[0], surname=investigator[1], 
			occupation=investigator[2], stamina=investigator[4], sanity=investigator[5], focus=investigator[6], 
			items=[], allies=[], skills=[], money=0, cluetokens=0, location=Agame.getlocation(investigator[3])))

	for otherworld in data.Otherworlds:
		Agame.locations.append(loc.otherworld(colors=otherworld[-1], expansion=otherworld[0], name=otherworld[1]))


	Agame.Start()

	# for investigator in Agame.investigators:
	# 	print investigator
	# 	print investigator.location

	# for location in Agame.locations:
	# 	print location
	# 	print location.investigators
