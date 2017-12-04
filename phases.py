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
	def Battlefield(monsters):
		"""
		NEEDS WORK!!!!
		takes all monsters of a location, if all monster are evade you can keep moving
		PlayerChoice(function) which monster first
		PlayerChoice(function) Combat or Evade
		evade:
			true: next monster
			false: combat
		combat: 
			true: fightorflight(evaded)
			false: remove monster from location and return false
		"""
	def Evade(monster):
		"""returns true if pass, 
		if fail does monsterdamage and returns false"""
	def Combat(monster):
		"""handles combat with a monster... (does it need an investigator? perhaps for mythos phase)
		=> movement point = 0
		=> horrorcheck 
			return true if sane
			return false if insane
		"""
	def fightorflight(evaded):
		"""PlayerChoice(function) Fight() or Flight()"""
	def fight():
		"""
		combat check:
			pass: monsterthrophie
			fail: Monsterdamage => FightorFlight()
		"""
	def flight():
		"""
		Evadecheck:
			Pass: return evade true for monster
			fail: monsterdamage => fightorflight
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
		