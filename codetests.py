import sysaid as sa

def timed_loop_test():
  T = sa.Toki()
  for i in range(0,1999):
    print i
  b = T.diff(-6)
  print "loop runtime=%f %s"%(b[0],b[1])

timed_loop_test()
