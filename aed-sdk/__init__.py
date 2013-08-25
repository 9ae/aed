import lofty

class Paradigm(object):

  def __init__(self):
    #bind interval start and stop and start functions
    self.bind_action_listeners()
  
  def bind_action_listeners(self):
    """
    for each interval type, look for onActionName functions
    and register them to action listeners
    """
    pass