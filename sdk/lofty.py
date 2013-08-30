"""
All abstract classes
"""

from abc import ABCMeta, abstractmethod, abstractproperty
class Interval:
	__metaclass__ = ABCMeta
	
	def __init__(self,duration):
		self._duration = duration
	
	@abstractproperty
	def	duration(self): pass
	
	@abstractproperty
	def prev(self): pass
	
	@abstractmethod
	def at_begin(self): pass
	
	@abstractmethod
	def at_end(self): pass
	
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
	
