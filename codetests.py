import sysaid as sa
import time

def timed_loop_test():
  print 'starting function sleep for 49 secs'
  T = sa.Toki()
  '''
  sum =0
  for i in range(0,1999):
    sum = sum+ i
  '''
  time.sleep(49)
  b = T.diffNow(unit='milli')
  # print "%f \t %f"%(T.get('runtime','milli'),T.get('runtime','micro'))
  print "loop runtime=%f %s seconds "%(b,'micro')
  

timed_loop_test()
