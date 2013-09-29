'''
Created on Sep 7, 2013

@author: alice
'''

import exp
import executioner as exe
'''
mod = exp.import_mod_file('paradigms/Mickey.py')
print mod
'''
e = exp.Experiment()
e.xml_load('experiments/simpletest.xml')
# e.print_details()

Ex = exe.Executioner()
Ex.run(e)