"""
All abstract classes
"""

from abc import ABCMeta, abstractmethod, abstractproperty
class Interval:
	__metaclass__ = ABCMeta
	
	@abstractproperty
	def	duration(self): pass
	
	@abstractproperty
	def big_bro(self): pass
	
	@abstractmethod
	def at_begin(self): pass
	
	@abstractmethod
	def at_end(self): pass
	
	def type_name(self):
		return type(self).__name__

class Action:
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def detect(self): pass
	
	@abstractmethod
	def respond(self): pass
	
	def invoke(self):
		self.respond()
	
	def type_name(self):
		return type(self).__name__
		
class Event:
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def pre_perform(self): pass
	
	@abstractmethod
	def perform(self): pass
	
	@abstractmethod
	def post_perform(self): pass
	
	def invoke(self):
		self.respond()
	
	def type_name(self):
		return type(self).__name__
