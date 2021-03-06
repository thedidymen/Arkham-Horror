class Dimension(object):
	"""docstring for Dimension"""
	def __init__(self, circle=False, triangle=False, cresentmoon=False, hexagon=False, square=False, diamond=False, star=False, slash=False, plus=False):
		# [circle, triangle, cresentmoon, hexagon, square, diamond, star, slash, plus]
		# [False, False, False, False, False, False, False, False, False]
		super(Dimension, self).__init__()
		self.dimensions = {
		    "Circle" : circle,
		    "Triangle" : triangle, 
		    "Cresent Moon" : cresentmoon, 
		    "Hexagon" : hexagon, 
		    "Square" : square, 
		    "Diamond" : diamond, 
		    "Star" : star, 
		    "Slash" : slash, 
		    "Plus" : plus
		}
	def __repr__(self):
		return ", ".join([key for key, value in self.dimensions.items() if value == True])
	def subsetoff(self, otherdimension):
		"""Returns True if current dimension is subset of otherdimension."""
		activedimensions = [key for key, value in self.dimensions.items() if value == True]
		flag = True
		for activedimension in activedimensions:
			if not otherdimension.dimensions[activedimension]:
				flag = False
		return flag



class check(object):
	"""docstring for check, its basicly a dict, so is the class necessary?  """
	def __init__(self, will=0, fight=0, speed=0, sneak=0, lore=0, luck=0, horrorcheck=0, evadecheck=0, combatcheck=0):
		super(check, self).__init__()
		self.skilldict = {
			"Will": will, 
			"Fight": fight, 
			"Speed": speed, 
			"Sneak": sneak, 
			"Lore": lore, 
			"Luck": luck, 
			"Horrorcheck": horrorcheck, 
			"Evadecheck": evadecheck, 
			"Combatcheck": combatcheck
			}
	def getskill(self, skill):
		"""returns value of skill. """
		return self.skilldict[skill]
		

class Investigatorskilltable(object):
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
	skil = check(will=1, fight=3)
	print skil.skilldict
	fth = Dimension(triangle = True, star = True)
	print fth