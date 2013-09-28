'''
Created on Sep 7, 2013

@author: alice
'''
from xml.etree import ElementTree as elle

import conf
'''
from sys import path
path.append(conf.setting['program_path'])

def from_import(name):
	m = __import__(name)
	for n in name.split(".")[1:]:
		m = getattr(m, n)
	return m
'''
def import_mod_file(filename):
	import os
	import sys
	directory, module_name = os.path.split(filename)
	module_name = os.path.splitext(module_name)[0]
	path = list(sys.path)
	sys.path.append(directory)
	module = None
	try:
		module = __import__(module_name)
	finally:
		sys.path[:] = path # restore
	return module

class Experiment(object):
	def __init__(self):
		self.paradigm = None
		self.intervals = []
		self.events = []	
		self.name = ''
		self.created_on = ''
		self.trial_duration = 0

	def print_details(self):
		print '%s : %s'%(self.name,self.paradigm)
		print '\t created on: %s'%self.created_on
		
		print '\n Events'
		for e in self.events:
			print e
		
		print '\n Intervals'
		for i in self.intervals:
			print i

	def xml_load(self,filename):
		# TODO: validate against xsd first
		tree = elle.parse(filename)
		root = tree.getroot()
		read_success = True
		
		# set paradigm
		paradigm_mod_name = root.get('paradigm')
		parad = import_mod_file(conf.setting['paradigms_path']+'/'+paradigm_mod_name+'.py')
		if parad!=None:
			self.paradigm = eval('parad.'+paradigm_mod_name+'()')
			self.paradigm.bind_action_listeners()
		else:
			raise NameError('failed to import '+paradigm_mod_name)
			return False
		
		# get meta data
		self.name = root.find('info/name').text
		self.created_on = root.find('info/date').text
		
		# assume found in xsd validation
		self.trial_duration = root.find('trialDuration').text
		
		# load events
		events_list = root.findall('events/*')
		for ev in events_list:
			ev_obj = self.paradigm.instantiate_name(ev.tag)
			ev_index = int(ev.get('id'))
			ev_props = ev.findall('self')
			ev_obj.name = ev.get('name')
			for p in ev_props:
				ev_obj.set_prop(p.get('name'),p.get('value'))
			self.events.insert(ev_index, ev_obj)
		
		# load intervals
		intervals_list = root.findall('intervals/*')
		for iv in intervals_list:
			iv_index = int(iv.get('id'))
			iv_duration = iv.find('duration').get('value')
			iv_obj = self.paradigm.instantiate_name(iv.tag)
			iv_obj.duration = float(iv_duration)
			iv_obj.name = iv.get('name')
			
			iv_chains = iv.findall('eventChains/*')
			for chain in iv_chains:
				if chain.tag=='timeEvents':
					pass
				elif chain.tag=='actionEvents':
					sim_act = chain.get('on')
					call_name = 'events_'+sim_act
					events_chain = []
					if hasattr(iv_obj,call_name):
						print 'found '+call_name
						events_chain = iv_obj.__getattr__(call_name)
					for evee in chain.findall('event'):
						event_id = int(evee.get('id'))
						try:
							event_ref = self.events[event_id]
							events_chain.append(event_ref)
							print 'found event %d'%event_id
						except LookupError:
							print '%d not found'%event_id
							read_success = False
					iv_obj.__setattr__(call_name,events_chain)
					print events_chain
			self.intervals.insert(iv_index,iv_obj)
		
		return read_success
	