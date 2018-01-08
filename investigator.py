from types import *
from skill import *


class Investigator(object):
	"""This class contains all possible action of an investigator within the game 
	of Arkham Horror."""
	def __init__(self, forename, surname, occupation, stamina, sanity, focus, location, items=[], allies=[], skills=[], money=0, cluetokens=0):
		super(Investigator, self).__init__()
		self.forename = forename
		self.surname = surname
		self.occupation = occupation
		self.stamina = SpendableEssence("Stamina", stamina, stamina)
		self.sanity = SpendableEssence("Sanity", sanity, sanity)
		self.focus = SpendableEssence("Focus", focus, focus)
		self.hands = SpendableEssence("Hands", 2, 2)
		self.delayed = False
		self.items = items
		self.allies = allies
		self.skills = check(speed = 3, fight = 3, combatcheck = 3, will = 3) # temp value for speed, to get movement up and running
		self.movementpoints = 0
		self.money = money
		self.cluetokens = cluetokens
		self.location = location
		self.monsterthrophies = []
		self.gatethrophies = []
		self.specials = []
	def __repr__(self):
		return "Investigator: " + self.forename + " " + self.surname
	def updatelocation(self, newlocation):
		"""Pop investigator from current location, and moves self to newlocation, updates self.location. 
		Does a self move for the start of the game"""
		self.location = newlocation
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
	def gainmovement(self, pts):
		"""sets movement to pts. taks pts as interger. """
		self.movementpoints = pts


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

	Investigatordata = [
			["Agnes", "Baker", "Waitress", "Velma's Diner", 5, 5, 2]
			["\"Ashcan\"", "Pete", "Drifter", "River Docks", 4, 6, 1]
			["Jenny", "Barnes", "Dilettante", "Train Station", 6, 4, 1]
			["Harvey", "Walters", "Professor", "Administration Building", 7, 3, 2]
		]