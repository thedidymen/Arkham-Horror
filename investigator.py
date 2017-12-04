from types import *


class Investigator(object):
	"""This class contains all possible action of an investigator within the game 
	of Arkham Horror."""
	def __init__(self, forename, surename, occupation, stamina, sanity, focus, items, allies, skills, money, cluetokens, location):
		super(Investigator, self).__init__()
		self.forename = forename
		self.surename = surename
		self.occupation = occupation
		self.stamina = SpendableEssence("Stamina", stamina, stamina)
		self.sanity = SpendableEssence("Sanity", sanity, sanity)
		self.focus = SpendableEssence("Focus", focus, focus)
		self.hands = SpendableEssence("Hands", 2, 2)
		self.items = items
		self.allies = allies
		self.skills = skills
		self.money = money
		self.cluetokens = cluetokens
		self.location = location
		self.monsterthrophies = []
		self.gatethrophies = []
		self.specials = []
	def __repr__(self):
		return "Investigator: " + self.forname + " " + self.surname
	def move(newLocation):
		"""moves to new location"""
	def changemoney(change):
		"""adds or reduces amount of money, money cannot get negative"""
	def changecluetokens(change):
		"""adds or reduces amount of cluetokens, cluetokens cannot get negative"""
	def spendFocus(change):
		"""spend focus up to the max focus"""
	def gainFocus(change):
		"""Gain focus to the max (depending on environment?)"""
	def gainItems(item):
		"""add item to item-list"""
	def loseItem(item):
		"""pop item from list, returns item?"""



class SpendableEssence(object):
	"""takes Name (string), Essence(number), MaxEssence(number). the current essence can not be lower than 
	1 or higher than MaxEssence"""
	def __init__(self, Name, Essence, MaxEssence):
		super(SpendableEssence, self).__init__()
		assert type(Essence) is IntType, "Essence is not an integer: %r" % id
		assert type(MaxEssence) is IntType, "MaxEssence is not an integer: %r" % id
		assert type(Name) is StringType, "Name is not a string: %r" % Name

		self.Name = Name
		if Essence <= MaxEssence and Essence >= 1:
			self.Essence = Essence
			self.MaxEssence = MaxEssence
		else:
			raise ValueError("Essence cannot be higher than MaxEssence or lower than 1")
	def __repr__(self):
		return self.Name + "[" + str(self.Essence) + "/" + str(self.MaxEssence) + "]"
	def SpendEssence(change):
		"""Gain or lose Essence between 1 and max. returns True if succes or maxed out, False if drops to zero or lower. If somehow, 
		stamina and sanity drops too, or below zero, player is devoured. """

class Skills(object):
	"""will take a dict {"Skill": int} with starting value and a dict with skill 
	pairs (key for up, value for down"""
	def __init__(self, ):
		super (Skills, self).__init__()
		self.currentSkill = {"Will": 0, "Fight": 0, "Speed": 0, "Sneak": 0, "Lore": 0, "Luck": 0}
		self.skilltable = {
			"Will" : [0,0,0,0], 
			"Fight" : [0,0,0,0],
			"Speed" : [0,0,0,0],
			"Sneak" : [0,0,0,0],
			"Lore" : [0,0,0,0],
			"Luck" : [0,0,0,0]
			}
		self.skillpairs = {"Speed" : "Sneak", "Fight" : "Will", "Lore" : "Luck"}
	def buildingskillrow(pair, startingvalues):
		"""adds two entries to skilltable with list of values (1 up and 1 down) 
		and sets up skillpairs"""
	def buildingtable():
		"""run buildingskillrow 3 times for making table compleet"""
	def settingcurrentskill():
		"""sets starting values for currentskill"""
	def focusingskills(pair, steps):
		"""changes currentskill for pair with steps according skilltable. keeps boundries"""
		
		

		

if __name__ == '__main__':
	def testInvestigator():
		print "testing Investigator"
		i = Investigator("Duke", "Pete", "Drifter", 5, 5, 1, [], [], [], 10, 2, "River Docks")
		print [i, i]
		print i

	def testSpendableEssence():
		print "testing SpendableEssence"

		#stamina = SpendableEssence("Stamina", "6", 5)

		try: 
			stamina = SpendableEssence("Stamina", 6, 5)
		except:
			print "pass: Essence higher than MaxEssence"
		try:
			stamina = SpendableEssence("Stamina", 0, 5)
		except:
			print "pass: Essence lower than 1"
		try:
			stamina = SpendableEssence("Stamina", 5, 5)
		except:
			print "fail: Essence in regular range"
		print stamina

	testInvestigator()
	testSpendableEssence()

		