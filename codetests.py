import sysaid as sa

def timed_loop_test():
	a = sa.time_now()
	for i in range(0,1999):
		print i
	b = sa.time_now()
	print "loop runtime=%f"%(b-a)

timed_loop_test()
