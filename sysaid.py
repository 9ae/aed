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

  def diff(self, unit=1):
    time_diff = datetime.now() - self.startTime
    if unit==-6:
      return [time_diff.microseconds, 'microseonds']
    elif unit==-3:
      return [float(time_diff.microseconds)/1000.0, 'milliseconds']
    else:
      return [time_diff.seconds,'seconds']
