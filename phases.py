class Phase(object):
	"""
	contains all the action needed through out each phase: 
	- skillchecks:
		will, fight, sneak, luck lore, speed, horrorcheck, combatcheck, ...
	- die roll

	"""
	def __init__(self):
		super(Phase, self).__init__()
	def die(numberofdie):
		"""returns list of die results"""
	def SumofSkills():
		"""Adds skill modifiers of all components of the game: event, AO, Environment, items, investigator...."""
	def Skillcheck(Skill, SumofSkills, numberofsucces, succes):
		"""
		skill => the skill to check for
		sumofskills => gives number of die for skill check
		numberofsucces => hits needed
		succes => what is a succes (format?) 
		"""
	def InvestigatorHeathCheck():
		"""
		checks if player is still conscious.
		Unconscious and insane => devoured
		Unconscious => to hospital
		Insane => Asylum
		Needs games hospitals and asylums
		PlayersChoice which
		returns True if healthy, False if deported to Hospital or Asylum
		"""

	def Battlefield(investigator, monsters, evaded=[], throphies=[]):
		"""
		For monster in Monsters
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

	def Horrorcheck(investigator, monster):
		"""
		Make a horrorcheck {will + monster horror rating, difficulty 1}
		investigatorheathcheck
		returns true if succesful
		"""

	def Evadecheck(investigator, monster):
		"""
		Makes Evadecheck {sneak + monster awareness, difficulty 1}
		returns true if succesful
		"""

	def Combatcheck(monster):
		"""
		makes Combat check  {fight + used weapons + monster combatrating (+game(AO, Environment), 
		difficulty: monster thoughtness}
		returns true if succesful
		playerschoice(used weapons(including spells))
		"""

	def fightorflight(investigator, monster, evaded=[], throphies=[]):
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


	def Monsterdamage(investigator, monster):
		"""
		deals monster damage to investigator(spendEssence).
		investigatorheathcheck
		"""


class Upkeep(Phase):
	"""
	Upkeep:
	- refresh exhausted cards
	- gain movementpoints
	- perform upkeep actions:
		-bank loans, blessed/cursed
	- adjust skills
	"""
	def __init__(self, Investigator):
		super(Upkeep, self).__init__()
		self.Investigator = Investigator
	def start():
		"""starts upkeep loop for this investigator"""
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
	def __init__(self, Investigator):
		super(Movement, self).__init__()
		self.Investigator = Investigator
	def start():
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
	def arkhammove():
		"""
		if monsters in currenlocation:
			battlefield (monsters)
			if movementpts > 0:
				move
				if gate move to otherworld
		"""
	def gainMovement():
		"""player gains movementpoints equel to speed - Game(OA, environment)"""
	def otherworldmovement():
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
	def specialcard():
		"""do special card stuff"""
	def gaincluetokens():
		"""add cluetokens of location to investigators stash"""
	def standup():
		"""
		investigator.delayed = False
		return
		"""




class ArkhamEncounters(Phase):

	def __init__(self, Investigator):
		super(ArkhamEncounters, self).__init__()
		self.Investigator = Investigator
	def start():
		"""
		if nogate:
			Arkhamencouter()
		if gate && explored:
			if investigator has 5 cluetokens and eldersign
				playerchoice(elderseal or clueseal or closegate)
			else if invesigator has 5 cluetokens:
				playerchoice(clueseal or closegate)
			else closegate()
		if game.victory:
			game.endgameandfinalscore()
		"""
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
	def __init__(self, Investigator):
		super(OtherWorldEncounters, self).__init__()
		self.Investigator = Investigator
	def start():
		"""
		
		"""

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
	def __init__(self, arg):
		super(Mythos, self).__init__()
		self.arg = arg
	def start():
		""""""