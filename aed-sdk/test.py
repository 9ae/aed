#test function as objects
import re
from inspect import isfunction
class hagumi(object):

    def __init__(self):
        self.actions = []
  
    def execute_all(self):
        print 'Hello I am a %s'%(type(self).__name__)
        for act in self.actions:
            act(self)
  
    def hello(self):
        print 'hello you should not see me'
  
    def on_hit(self):
        print 'why did you hit me?'
  
    def on_kiss(self):
        print 'now a kiss is so much better'
  
    def bye(self):
        print 'if this works out we shall never have to say goodbye'
    
    def register_actions(self):
        mystuff = self.__class__.__dict__
        for prop in mystuff:
            val = mystuff[prop]
            if isfunction(val) and re.match('on_',prop):
                self.actions.append(val);
                print 'added '+prop+' to actions list'
            
      
hagu = hagumi()
hagu.register_actions()
hagu.execute_all()