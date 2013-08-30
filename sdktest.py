import sdk
import time

class Mickey(sdk.Paradigm):
	
	def __init__(self):
		sdk.Paradigm.__init__(self)
		self.sequence = []
		self.sequence_point = 0
		
		self.time_passed_experiment = 0.0
		self.time_passed_trial = 0.0

	class LeverPress(sdk.lofty.Action):
		def __init__(self):
			pass
		
		def detect(self):
			print 'waiting for lever press'
		
		def respond(self):
			print 'do what on lever press'
	
	class Reward(sdk.lofty.Event):
		def __init__(self):
			self.valves = [True, False, False, False]

		def perform(self):
			print 'reward delivered'
		
	class Restart(sdk.lofty.Event):
		def __init__(self):
			pass
		
		def perform(self):
			self.sequence_point = 0
			print 'restart trial'
	
	class Wait(sdk.lofty.Interval):   
		def __init__(self, duration):
			sdk.lofty.Interval.__init__(self, duration)
			self._prev = None
		
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
			print 'entered wait interval 0.0'
			
		def at_end(self):
			print 'exited wait interval %f'%self.duration

	def test(self):
		"""
		self.matte = self.Wait(2.0)
		self.matte.at_begin()
		time.sleep(self.matte.duration)
		self.matte.at_end()
		"""
		self.sort_classes()
		self.print_classes()
			
mouse = Mickey()
mouse.test()