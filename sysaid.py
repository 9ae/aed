def find_os():
	import platform
	plat = platform.system()
	if plat=='Windows':
		return 0
	elif plat=='Linux':
		return 1
	elif platform=='Darwin':
		return 2
	else:
		return -1

def time_now():
	import time
	my_os = find_os()
	if my_os==0:
		# gets time in seconds as float
		return time.clock()	
	elif my_os==1 or my_os==2:
		#gets time in seconds
		return time.time()

def dt_now():
	from datetime import datetime
	dt = datetime.now()
	return dt.microsecond

from datetime import datetime
class Toki:

	def __init__(self):
		self.startTime = datetime.now()
		self.timelog = {}

	def inUnit(self,time_diff,unit):
		if unit=='micro':
			return (time_diff.days * 24 * 60 * 60 + time_diff.seconds) * 10e6 + time_diff.microseconds
		elif unit=='milli':
			return (time_diff.days * 24 * 60 * 60 + time_diff.seconds) * 1000 + time_diff.microseconds / 1000.0
		else:
			return (time_diff.days * 24 * 60 * 60 + time_diff.seconds)

	def diff(self, since, record=None, unit='sec'):
		time_diff = datetime.now() - since
		if(record!=None):
			if isinstance(record, str):
				self.timelog[record] = time_diff
			else:
				print 'record must be a string'
		return self.inUnit(time_diff,unit)

	def diffNow(self, record=None, unit='sec'):
		return self.diff(self.startTime, record=record, unit=unit)

	def get(self,recordName,unit=None):
		if(unit==None):
			return self.timelog[recordName]
		else:
			return self.inUnit(self.timelog[recordName],unit)