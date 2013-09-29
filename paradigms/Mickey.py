import aedsdk
import time

class Mickey(aedsdk.Paradigm):
	
	def __init__(self):
		aedsdk.Paradigm.__init__(self)

	class LeverPress(aedsdk.Action):
		def __init__(self):
			pass
		
		def detect(self):
			print 'waiting for lever press'
		
		def respond(self):
			print 'do what on lever press'
	
	class Reward(aedsdk.Event):
		def __init__(self):
			self.valve = 0

		def perform(self):
			print 'reward delivered @ %f'%self.exp.tk.diff()
		
		def set_prop(self,name,val):
			if name=="valve":
				self.valve = int(val)
		
		def __str__(self):
			return "Reward { valve:"+str(self.valve)+" }"
		
	class Restart(aedsdk.Event):
		def __init__(self):
			pass
		
		def perform(self):
			self.exp.new_trial()
			print 'restart trial @ '%self.exp.tk.diff()
	
	class Wait(aedsdk.Interval):   
		def __init__(self, duration=0.0):
			aedsdk.Interval.__init__(self, duration)
			
		def on_LeverPress(self):
			print 'lever pressed'
			for act in self.events_LeverPress:
				act()
		
		def meanwhile(self):
			self.a_LeverPress.detect()
			
	class Tone(aedsdk.Interval):
		def __init__(self,duration=0.0):
			aedsdk.Interval.__init__(self, duration)
		
		def at_begin(self):
			aedsdk.Interval.at_begin(self)
			print 'tone play start @ '%self.exp.tk.diff()
		
		def at_end(self):
			aedsdk.Interval.at_end(self)
			print 'tone play end @ '%self.exp.tk.diff()
			
		def meanwhile(self): pass
	
	class Present(aedsdk.Interval):
		def __init__(self,duration=0.0):
			aedsdk.Interval.__init__(self, duration)
		
		def on_LeverPress(self):
			print 'give reward :) @ '%self.exp.tk.diff()
			for act in self.events_LeverPress:
				act()
				
		def meanwhile(self):
			self.a_LeverPress.detect()
	
	class Refrain(aedsdk.Interval):
		def __init__(self,duration=0.0):
			aedsdk.Interval.__init__(self, duration)
			self.reward = True
		
		def at_end(self):
			if self.reward:
				aedsdk.Interval.at_end(self)
				print 'reward given  @ '%self.exp.tk.diff()
			else:
				print 'reward not given  @ '%self.exp.tk.diff()
		
		def on_LeverPress(self):
			self.reward = False
			print 'oops pressed lever no reward at the end :(  @ '%self.exp.tk.diff()
			for act in self.events_LeverPress:
				act()
				
		def meanwhile(self):
			self.a_LeverPress.detect()

"""
	def test(self):
		self.matte = self.Wait(2.0)
		self.matte.at_begin()
		time.sleep(self.matte.duration)
		self.matte.at_end()
		#self.print_classes()
		self.bind_action_listeners()
		self.print_classes()
			
mouse = Mickey()
exp = aedsdk.exp.Experiment(mouse)
print exp._LeverPress
"""
