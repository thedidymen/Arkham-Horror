import investigator as inv
import phases as ph
import location as loc
import data
import skill 
import deck
import connections
import sys


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
		self.mythosdeck = deck.Deck(name="Mythos")
		self.doomtrack = 0 #needs to move to AO?
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
	def checkmonsterlimit(self):
		""""""
	def AncientOneAwake(self):
		"""returns True when Ancient One is awake else False"""
	def recallmonsters(self, dimension):
		"""returns all monsters with dimension symbool to the monstercup"""
	def FinalBattle(self):
		"""When Ancient One awakes this initiates Final Battle based on game status. kicking off new class?"""
		print "The Ancient One Awakes... The world burns"
		sys.exit()
	def Start(self):
		"""loops over phases and whitin each phase (except Mythos) over the investigators, until Victory or AncientOneAwake is 
		True. and kicks off appropriate subroutine."""
		for i in range(20):
			print
			print
			print "Round: ", i
			for phase in self.phases:
				print
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

	Agame.locations = [loc.building(expansion=l[0], name=l[1], stability=l[2], neighborhood=l[3]) for l in data.Buildings]
	Agame.locations += [loc.street(expansion=l[0], name=l[1], neighborhood=l[1]) for l in data.Streets]
	for n in range(len(Agame.locations)):
		if Agame.locations[n].name == data.connections[n][0]:
			for connectedlocation in data.connections[n][1].keys():
				for i in Agame.locations:
					if i.name == connectedlocation:
						clobj = i
						break
				Agame.locations[n].exits.append(connections.connection(location=clobj, connectiontype=data.connections[n][1][connectedlocation]))

	for investigator in data.Investigatordata:
		Agame.investigators.append(inv.Investigator(forename=investigator[0], surname=investigator[1], 
			occupation=investigator[2], stamina=investigator[4], sanity=investigator[5], focus=investigator[6], 
			items=[], allies=[], skills=[], money=0, cluetokens=0, location=Agame.getlocation(investigator[3])))
		Agame.getlocation(investigator[3]).arrive(Agame.investigators[-1])

	for otherworld in data.Otherworlds:
		Agame.locations.append(loc.otherworld(colors=otherworld[-1], expansion=otherworld[0], name=otherworld[1]))

	for mythoscard in data.mythoscards:
		Agame.mythosdeck.Cards.append(deck.Mythos(
			title=mythoscard[0], 
			expansion=mythoscard[1], 
			mtype=mythoscard[2], 
			subtype=mythoscard[3], 
			gatelocation=Agame.getlocation(mythoscard[4]), 
			cluelocation=Agame.getlocation(mythoscard[5]), 
			whitedimension=skill.Dimension(circle=mythoscard[6][0], triangle=mythoscard[6][1], cresentmoon=mythoscard[6][2], hexagon=mythoscard[6][3], square=mythoscard[6][4], diamond=mythoscard[6][5], star=mythoscard[6][6], slash=mythoscard[6][7], plus=mythoscard[6][8]), 
			blackdimension=skill.Dimension(circle=mythoscard[7][0], triangle=mythoscard[7][1], cresentmoon=mythoscard[7][2], hexagon=mythoscard[7][3], square=mythoscard[7][4], diamond=mythoscard[7][5], star=mythoscard[7][6], slash=mythoscard[7][7], plus=mythoscard[7][8]), 
			text=mythoscard[8]
			))
	Agame.mythosdeck.shuffleDeck()

	# for n in Agame.locations:
	# 	for m in n.exits:
	# 		print m.connectiontype

	for gate in data.Gates:
		# print type(gate[3])
		Agame.gates.append(connections.Gate( 
			location=Agame.getlocation(gate[1]), 
			dimension=skill.Dimension(gate[2]), 
			modifier=gate[3], 
			name=Agame.getlocation(gate[1]).name, 
			expansion=gate[0], 
			connectiontype=gate[4]))

	# for gate in Agame.gates:
	# 	print gate
	# 	print gate.location

	# for loc in Agame.locations:
	# 	print
	# 	print loc
	# 	print loc.stability
	# 	if loc.stability == False:
	# 		print loc.seal
	# 		print loc.gates

	# print Agame.mythosdeck.Cards
	# Agame.mythosdeck.shuffleDeck()
	# print Agame.mythosdeck.Cards
	
	Agame.Start()

	# for card in Agame.mythosdeck.Cards:
	# 	print
	# 	print card

	# for investigator in Agame.investigators:
	# 	print investigator
	# 	print investigator.location

	# for location in Agame.locations:
	# 	print location
	# 	print location.investigators
