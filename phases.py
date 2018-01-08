import random as rnd
import os
import location

class Phase(object):
	"""
	contains all the action needed through out each phase: 
	- skillchecks:
		will, fight, sneak, luck lore, speed, horrorcheck, combatcheck, ...
	- die roll

	"""
	def __init__(self):
		super(Phase, self).__init__()
	def die(self, numberofdie):
		"""returns list of die results"""
		return [rnd.randint(1,6) for i in range(numberofdie+1)]
	def SumofSkills(self, ):
		"""Adds skill modifiers of all components of the game: event, AO, Environment, items, investigator...."""
	def Skillcheck(self, Numberofdie, difficulty, blessed=None):
		"""
		returns True if succeses of number of die match difficulty.
		numberofdie => number of die to roll
		difficulty => hits needed
		blessed => None hits (5,6), True hits (4, 5, 6), False hits (6)
		"""
		# print "blessed", blessed, "difficulty", difficulty, "numberofdie", Numberofdie
		if blessed:
			succes = [4, 5, 6]
		elif not blessed:
			succes = [6]
		else:
			succes = [5, 6]
		return difficulty <= len([True for i in self.die(Numberofdie) if i in succes])
	def InvestigatorHeathCheck(self):
		"""
		checks if player is still conscious. and sane?
		Unconscious and insane => devoured
		Unconscious => to hospital
		Insane => Asylum
		Needs games hospitals and asylums
		PlayersChoice which
		returns True if healthy, False if deported to Hospital or Asylum
		"""

	def Battlefield(self, investigator, evaded=[], throphies=[]):
		"""
		For monster in investigator.location.monsters:
			PlayerChoice(Evade or Combat)
			if Evade:
				if Evade: 
					Evaded.append(monster)
					break
				else: MonsterDamage
			set movement => 0
			if horrorcheck:
				evaded, throphies = fightorflight(investigator, monster, evaded, throphies)

		output: evaded monsters?
		investigator => gain throphies
		return
		"""
		# for i in range(1, 20):
		# 	print self.Skillcheck(Numberofdie=i, difficulty=self.playerschoice(range(1, 4)), blessed=self.playerschoice([True, None, False]))
		print "!! Battlefield between", investigator, "and"
		for monster in investigator.location.monsters:
			choice = self.playerschoice(['E', 'C'])
			if choice == 'E':
				if self.Evadecheck(investigator=investigator, monster=monster):
					evaded.append(monster)
					break
				else:
					self.Monsterdamage(investigator=investigator, monster=monster)
			investigator.movementpoints = 0
			if self.Horrorcheck(investigator=investigator, monster=monster):
				evaded, throphies = self.fightorflight(investigator=investigator, monster=monster, evaded=evaded, throphies=throphies)
			else:
				print "!! The Horror.... ARRGhhhhhh...."


	def Horrorcheck(self, investigator, monster):
		"""
		Make a horrorcheck {will + monster horror rating, difficulty 1}
		investigatorheathcheck
		returns true if succesful
		"""
		print "!! oh the horror", monster
		return self.Skillcheck(Numberofdie=investigator.skills.getskill("Will")+investigator.skills.getskill("Horrorcheck")-monster.horrorrating, difficulty=1, blessed=None)

	def Evadecheck(self, investigator, monster):
		"""
		Makes Evadecheck {sneak + monster awareness, difficulty 1}
		returns true if succesful
		"""
		print "!! lucky me I evaded", monster
		return self.Skillcheck(Numberofdie=investigator.skills.getskill("Sneak")+investigator.skills.getskill("Evadecheck")-monster.awareness, difficulty=1, blessed=None)


	def Combatcheck(self, monster):
		"""
		makes Combat check  {fight + used weapons + monster combatrating (+game(AO, Environment), 
		difficulty: monster thoughtness}
		returns true if succesful
		playerschoice(used weapons(including spells))
		"""
		return self.Skillcheck(Numberofdie=investigator.skills.getskill("Fight")+investigator.skills.getskill("Combatcheck")-monster.horrorrating, difficulty=monster.thoughtness, blessed=None)


	def fightorflight(self, investigator, monster, evaded=[], throphies=[]):
		"""
		playerchoice(fight or flight)
		Flight:
			if Evade: Evaded.append(monster) return evaded, throphies
			else 
				MonsterDamage
				fightorflight(investigator, monster)
		fight:
			if Combatcheck: throphies.append(monster), return evaded, throphies
			else 
				MonsterDamage
				fightorflight(investigator, monster)
		"""
		print "!! dancing around, bla bla"
		return evaded, throphies
	# def drawmonster(self, gatelocation):
	# 	pass
	# def investigatoratgate(self, location):
	# 	pass

	def Monsterdamage(self, investigator, monster):
		"""
		deals monster damage to investigator(spendEssence).
		investigatorheathcheck
		"""
		print "!! Ouch, you hurt me"
		return
	def playerschoice(self, choices):
		"""choices is a list, returns on of the objects in the list. later perhaps in own class."""
		if len(choices) >= 0:
			rnd.seed()
			keuze = rnd.choice(choices)
			return keuze
		return



class Upkeep(Phase):
	"""
	Upkeep:
	- refresh exhausted cards
	- gain movementpoints
	- perform upkeep actions:
		-bank loans, blessed/cursed
	- adjust skills
	"""
	def __init__(self, game):
		super(Upkeep, self).__init__()
		self.game = game
	def start(self, investigator):
		"""starts upkeep loop for this investigator"""
		print "Upkeep for:", investigator
	def refresh():
		"""loops over investigator items, if hasattr(item, exhausted) ==> item.exhausted == true"""
	def gainBenefits():
		"""player gains advantages of a retainer, ..."""
	def rollupkeep():
		"""Roll for every special that requires upkeep, on a 1 discard, else keep (needs a die function) """
	def adjustskill():
		"""Gives to PlayerChoice(function), all possilbe choices including doing nothing or partial use 
		of ability (as a list/dict?)"""



class Movement(Phase):
	""""""
	def __init__(self, game):
		super(Movement, self).__init__()
		self.game = game
	def start(self, investigator):
		"""
		if delayed: standup and return
		gainmovement():
		while movement > 0:
			if isinstance(investigator.location, otherworld):
				self.otherworldmovement()
				movementpts = 0
			else:
				playerchoice(move to exit, spend movementpts on special cards, do nothing)
				if move => arkhammove
				if special cards: => special card
				if nothing: movementpts = 0
		gaincluetokens()
		"""
		print "Movement for:", investigator
		if investigator.delayed:
			investigator.delayed = False
			return
		else:
			self.gainMovement(investigator)
		while investigator.movementpoints > 0:
			print "Currentmoventpoints: ", investigator.movementpoints
			print "Currentlocation: ", investigator.location
			if isinstance(investigator.location, location.otherworld):
				investigator.movementpoints = 0
				self.otherworldmovement(investigator)
			else:	
				self.arkhammove(investigator, self.playerschoice([connection.location for connection in investigator.location.exits]))

			# this case only choose is to move, however player has more options. still needs some work


	def arkhammove(self, investigator, newlocation):
		"""
		if monsters in currenlocation:
			battlefield (monsters)
		if movementpts > 0:
			move
			if gate move to otherworld
		"""
		if len(investigator.location.monsters) > 0:
			self.Battlefield(investigator)
		if investigator.movementpoints > 0:
			investigator.location.depart(investigator)
			investigator.updatelocation(newlocation)
			investigator.location.arrive(investigator)
			investigator.movementpoints -= 1
			if len(investigator.location.monsters) > 0 and investigator.movementpoints == 0:
				self.Battlefield(investigator)

	def movetoarkham(self, investigator, newlocation):
		investigator.location.departright(investigator)
		investigator.updatelocation(newlocation)
		investigator.location.arrive(investigator)
		if len(investigator.location.monsters) > 0:
			self.Battlefield(investigator)


	def otherworldmovement(self, investigator):
		"""	
		if investigator in investigator.location.left:
			investigator.location.right = investigator.location.left.pop(investigator)
		else if investigator in investigator.location.right:
			if gate to otherworld:
				playerchoice(gate locations in arkham)
				gate explored by investigator
			else:
				lost in time and space
		"""
		if investigator in investigator.location.left:
			investigator.location.departleft(investigator)
			investigator.location.arriveright(investigator)
		elif investigator in investigator.location.right:
			print "Searching for a way back from", investigator.location
			self.movetoarkham(investigator, self.playerschoice([gate.arkhamlocation for gate in investigator.location.gates]))
			investigator.location.gate.explored.append(investigator)
			print investigator, "has arrived back in arkham,", investigator.location
		else:
			print "Error: otherworld movement fell through........"

	def gainMovement(self, investigator):
		"""player gains movementpoints equel to speed - Game(OA, environment)"""
		investigator.gainmovement(investigator.skills.getskill("Speed")) #+ game.OA.skills + mythos.skill + ...

	def specialcard(self):
		"""do special card stuff"""
	def gaincluetokens(self):
		"""add cluetokens of location to investigators stash"""




class ArkhamEncounter(Phase):

	def __init__(self, game):
		super(ArkhamEncounter, self).__init__()
		self.game = game
	def start(self, investigator):
		"""
		if nogate:
			Arkhamencouter()
		if gate && explored:
			if investigator has 5 cluetokens and eldersign
				playerchoice(elderseal or clueseal or closegate)
			else if invesigator has 5 cluetokens:
				playerchoice(clueseal or closegate)
			else closegate()
		# checking after every phase in mainloop.
		# if game.victory:  
		# 	game.endgameandfinalscore()
		"""
		if isinstance(investigator.location, location.otherworld):
			print investigator, " in other dimension, no arkhamencouter"
		else:
			print "Arkham Encouter for:", investigator
			if investigator.location.gate != None:
				if investigator in investigator.location.gate.explored:
					print "well I should be closing this gate..."
				else:
					investigator.location.gate.location.arriveleft(investigator)
					investigator.updatelocation(investigator.location.gate.location)
			elif investigator.location.gate == None:
				print "Arkham encounter thing at: ", investigator.location

	

	def Arkhamencouter():
		"""
		if in buildinglocation:
			playerchoice(locationability or encouterdeck)
		if in street:
			optional special street stuff
		(Monsters appering without a gate are either claimed as throphie or returen to the cup)
		"""
	def closeGate():
		"""
		if PlayerChoice(LoreCheck, FightCheck)
			investigator gain gatethrophie
			game.recallmonsters(dimension)
			return True
		return False
		"""
	def ElderSeal():
		"""
		remove doomtoken
		lose 1 stamina and 1 health
		Seals location
		investigator gain gatethrophie
		game.recallmonsters(dimension)
		"""
	def ClueSeal():
		"""
		if closegate():
			spend 5 cluetokens
			seal location
		"""


class OtherWorldEncounters(Phase):
	"""
	OtherWorldEncounters:
	- draw otherworld encouters till match of colors
	"""
	def __init__(self, game):
		super(OtherWorldEncounters, self).__init__()
		self.game = game
	def start(self, investigator):
		"""
		
		"""
		if isinstance(investigator.location, location.otherworld):
			print "Otherworld Encouter for:", investigator
		else:
			print investigator, " in Arkham, no Otherworld Encounter"

class Mythos(Phase):
	"""
	Mythos:
	Draw mythos card:
	Try open gate:
	if elder sign:
		pass
	if open gate:
		Monstersurge
	else: 
		doom track advances
		draw gate for location
		draw monster

	place cluetoken
	move monsters
	activate mythos ability
	"""
	def __init__(self, game):
		super(Mythos, self).__init__()
		self.game = game
	def start(self):
		""""""
		print "Mythos time..."
		Currentmythos = self.game.mythosdeck.drawCard()
		print Currentmythos
		print "Gatelocation: ", Currentmythos.gatelocation

		self.gatelocationstatus(Currentmythos.gatelocation)
		self.monstermove(whitedimension=Currentmythos.whitedimension, blackdimension=Currentmythos.blackdimension)

	def monstermove(self, whitedimension, blackdimension):
		# movementtypes = ['black', 'white', 'orange(aquatic)', 'blue(flying)', ]
		#  needs seperating special moves form basic move or something ;)
		for monster in self.game.monsteringame:
			print monster, "currently at", monster.location,
			if monster.dimension.subsetoff(whitedimension):
				monster.move('white')
				print "moved to", monster.location
			elif monster.dimension.subsetoff(blackdimension):
				monster.move('black')
				print "moved to", monster.location
			else:
				print	



	def gatelocationstatus(self, gatelocation):
		if gatelocation == None:
			print "No gate this turn..."
			return
		elif hasattr(self, 'self.seal'):
			if self.seal == True:
				print "An Elder sign prevent a gate from opening."
				return
		elif gatelocation.gate != None:
			self.monstersurge(gatelocation)
		elif gatelocation.gate == None:
			self.game.doomtrack += 1
			self.openingagate(gatelocation)
			gatelocation.cluetokens = 0
		else:
			print "Error: gatelocation status falls through"

	def openingagate(self, gatelocation):
		# no gates => final battle
		if len(self.game.gates) > 0:
			print "a gate opened at ", gatelocation
			gatelocation.opengate(self.game.gates.pop(0)) #places gate in gatelocation
			gatelocation.gate.arkhamopen(gatelocation) #sets arkham location in gate and open gate in otherworld
			if len(gatelocation.investigators) > 0:
				for investigator in gatelocation.investigators:
					print investigator, "at", gatelocation, "gets sucked into gate to", gatelocation.gate.location, "and is delayed."
					investigator.location.gate.location.arriveleft(investigator)
					investigator.updatelocation(investigator.location.gate.location)
					investigator.delayed = True
			self.spawnmonster(gatelocation)
		else:
			print "seems we're out of gates"

	def monstersurge(self, gatelocation):
		"""max(#player|#gates)*monsters appear form every gate. starting at gatelocation. 
		(so that number of monsters is even everywhere?)"""
		print "!! MONSTERSURGE"

	def spawnmonster(self, location):
		if len(self.game.monstercup):
			monster = self.game.monstercup.pop(0)
			self.game.monsteringame.append(monster)
			location.monsters.append(monster)
			monster.arrive(location)
			print location.monsters[-1], "has arrived at", location
		else:
			print "Monsterproduction has halted, please send for reenforcements."
		return




