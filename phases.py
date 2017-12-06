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
	"""
	Movement:
	if delayed:
		delayed => False => end movement
	if in Arkham:
		if playes wish to spend movement points on tomes
		if monster:
			fight or evade
		else move
	if OtherWorld:
		if right:
			move to arkham
		if left:
			move right
	"""
	def __init__(self, Investigator):
		super(Movement, self).__init__()
		self.Investigator = Investigator
	def start():
		"""sets up all the if statements"""
	def StandUp():
		"""if investigator is delayed, undelayed the investigator and end movement"""
	def Spendmovementpoints():
		"""spend moventpoints on none movement, like tomes"""
	def UnspendMovementpoints():
		"""
		Present PlayerChoices(function) with all possible option for player: exits, trade, stop moving, activate special cards,
		if monster present with moving or stopping => BattleField(monsters) 
		if True => continue (investigator may have 0 movement points left)
		if false => investigator is insane or unconscius end of his/her turn.
		"""
	def exits():
		"""returns all possible exits for current location + stopping with moving"""
	def trade():
		"""returns possible investigators to trade with in current location"""
	def specialcards():
		"""returns items with spending movementpoits ability"""


class ArkhamEncounters(Phase):
	"""
	ArkhamEncounters:
	if gate:
		if explored:
			close gate
			optional: seal gate
		if not explored:
			move to OtherWorld left area
	if no gate:
		have encouter:
		form deck or location
	"""
	def __init__(self, Investigator):
		super(ArkhamEncounters, self).__init__()
		self.Investigator = Investigator

class OtherWorldEncounters(Phase):
	"""
	OtherWorldEncounters:
	- draw otherworld encouters till match of colors
	"""
	def __init__(self, Investigator):
		super(OtherWorldEncounters, self).__init__()
		self.Investigator = Investigator

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
		