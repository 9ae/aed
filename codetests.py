import sysaid as sa

def timed_loop_test():
	T = sa.Toki()
	sum =0
	for i in range(0,1999):
		sum = sum+ i
	b = T.diffNow('runtime')
	print "%f \t %f"%(T.get('runtime','milli'),T.get('runtime','micro'))
  # print "%d :loop runtime=%f %s seconds "%(sum,b,unit)
	
for j in range(0,100):
	timed_loop_test()
