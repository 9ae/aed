import sdk
import time

class Mickey(sdk.Paradigm):
    
    def __init__(self):
        sdk.Paradigm.__init__(self)
   
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
        
    class Wait(sdk.lofty.Interval):   
        def __init__(self, duration):
            sdk.lofty.Interval.__init__(self, duration)
            self._big_bro = None
        
        @property    
        def duration(self):
            return self._duration
        
        @duration.setter
        def duration(self, value):
            self._duration = value
          
        @property
        def big_bro(self):
            return self._big_bro
        
        @big_bro.setter
        def big_bro(self,value):
            self._big_bro = value
            
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