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
		return time.clock()
	elif my_os==1 or my_os==2:
		return time.time()
