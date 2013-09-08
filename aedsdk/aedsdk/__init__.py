import janus
import inspect
from abc import ABCMeta, abstractmethod, abstractproperty

class Interval:
	__metaclass__ = ABCMeta
	
	def __init__(self,duration):
		self._duration = duration
		self._prev = None
		self.events_end = []
		self.events_begin = []
	
	@property	
	def duration(self):
		return self._duration
	
	@duration.setter
	def duration(self, value):
		self._duration = value
		
	@property
	def prev(self):
		return self._prev
	
	@prev.setter
	def prev(self,value):
		self._prev = value

	def at_begin(self): 
		for act in self.events_begin:
			act()
	
	def at_end(self): 
		for act in self.events_end:
			act()
	
class Action:
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def detect(self): pass
	
	@abstractmethod
	def respond(self): pass
	
	def invoke(self):
		self.respond()
	
		
class Event:
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def perform(self): pass
	
	def invoke(self):
		self.perform()

class Paradigm(object):

		def __init__(self):
				self.atypes = []
				self.etypes = []
				self.itypes = []
				self.sort_classes()
				
				self.tk = janus.Timekeeper(-3)

		"""
		performed at the begining of an paradigm
		"""
		def bind_action_listeners(self): 
			action_names = []
			for aclass in self.atypes:
				action_names.append(['on_'+aclass.__name__,'events_'+aclass.__name__])
			# for each interval
			for iclass in self.itypes:
				for act_name in action_names:
					if hasattr(iclass,act_name[0]):
						self.__setattr__(act_name[1],[])
						print iclass.__name__+' has '+act_name
					else:
						print act_name+' not registered in '+iclass.__name__
			# > for each action
			# look for on_action
			pass
				
		def sort_classes(self):
				mystuff = self.__class__.__dict__
				good = True
				for key in mystuff:
						val = mystuff[key]
						if inspect.isclass(val):
								if issubclass(val,Interval):
										self.itypes.append(val)
								elif issubclass(val,Event):
										self.etypes.append(val)
								elif issubclass(val,Action):
										self.atypes.append(val)
								else:
										good = False
				return good
		
		def print_classes(self):
				print '\n listing actions'
				for a in self.atypes:
						print a
				print '\n listing events'
				for e in self.etypes:
						print e
				print '\n listing intervals'
				for i in self.itypes:
						print i
		
		