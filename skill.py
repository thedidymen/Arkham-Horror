class check(object):
	"""docstring for check"""
	def __init__(self, skilldict):
		super(check, self).__init__()
		self.skilldict = skilldict
		self.exceptiondict = {}
	def addexception(exception, exceptiondict):
		"""add exception to exceptiondict in a dict of dict."""
	def giveskill(skill, **exception):
		"""returns value of skill. **exception will check if exception is in the exception dict and 
		will return alternate value if so"""
		





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
		
