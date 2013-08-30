import lofty
import janus
import inspect

class Paradigm(object):

    def __init__(self):
        #bind interval start and stop and start functions
        self.atypes = []
        self.etypes = []
        self.itypes = []
        self.bind_action_listeners()
        
        self.tk = janus.Timekeeper(-3)

    def bind_action_listeners(self): pass
        
    def sort_classes(self):
        mystuff = self.__class__.__dict__
        good = True
        for key in mystuff:
            val = mystuff[key]
            if inspect.isclass(val):
                if issubclass(val,lofty.Interval):
                    self.itypes.append(val)
                elif issubclass(val,lofty.Event):
                    self.etypes.append(val)
                elif issubclass(val,lofty.Action):
                    self.atypes.append(val)
                else:
                    good = False
        return good
    
    def print_classes(self):
        print '\n listing actions'
        for a in self.atypes:
            print a
        print '\n listing events'
        for e in self.etypes:
            print e
        print '\n listing intervals'
        for i in self.itypes:
            print i
    
    