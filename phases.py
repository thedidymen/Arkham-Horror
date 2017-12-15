import random as rnd

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
	def SumofSkills(self, ):
		"""Adds skill modifiers of all components of the game: event, AO, Environment, items, investigator...."""
	def Skillcheck(self, Skill, SumofSkills, numberofsucces, succes):
		"""
		skill => the skill to check for
		sumofskills => gives number of die for skill check
		numberofsucces => hits needed
		succes => what is a succes (format?) 
		"""
	def InvestigatorHeathCheck(self):
		"""
		checks if player is still conscious.
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
		pass

	def Horrorcheck(self, investigator, monster):
		"""
		Make a horrorcheck {will + monster horror rating, difficulty 1}
		investigatorheathcheck
		returns true if succesful
		"""

	def Evadecheck(self, investigator, monster):
		"""
		Makes Evadecheck {sneak + monster awareness, difficulty 1}
		returns true if succesful
		"""

	def Combatcheck(self, monster):
		"""
		makes Combat check  {fight + used weapons + monster combatrating (+game(AO, Environment), 
		difficulty: monster thoughtness}
		returns true if succesful
		playerschoice(used weapons(including spells))
		"""

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


	def Monsterdamage(self, investigator, monster):
		"""
		deals monster damage to investigator(spendEssence).
		investigatorheathcheck
		"""
	def playerschoice(self, choices):
		"""choices is a list, returns on of the objects in the list. later perhaps in own class."""
		if len(choices) >= 0:
			keuze = rnd.choice(choices)
			print keuze
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
			investigator.delayed = True
			return
		else:
			self.gainMovement(investigator)
		while investigator.movementpoints > 0:
			print "currentmoventpoints: ", investigator.movementpoints
			print "currentlocation: ", investigator.location
			# if isinstance(investigator.location, otherworld):
			# 	self.otherworldmovement()
			# 	investigator.gainmovement(0)
			# else:
			self.arkhammove(investigator, self.playerschoice(investigator.location.exits).location)
			# this case only choose is to move, however player has more options. still needs some work


	def arkhammove(self, investigator, newlocation):
		"""
		if monsters in currenlocation:
			battlefield (monsters)
		if movementpts > 0:
			move
			if gate move to otherworld
		"""
		if investigator.location.monsterinlocation():
			self.battlefield(investigator)
		if investigator.movementpoints > 0:	
			investigator.move(newlocation)
			if investigator.location.gateinlocation():
				# get sucked into the gate
				pass

	def gainMovement(self, investigator):
		"""player gains movementpoints equel to speed - Game(OA, environment)"""
		investigator.gainmovement(investigator.skills.getskill("Speed")) #+ game.OA.skills + mythos.skill + ...
	def otherworldmovement(self):
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
		print "otherworld movement"
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
		print "Arkham Encouter for:", investigator
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
		print "Otherworld Encouter for:", investigator

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