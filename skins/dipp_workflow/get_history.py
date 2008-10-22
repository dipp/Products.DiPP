## Script (Python) "get_history"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=instance_id
##title=
##
## Warnings:
##  Prints, but never reads 'printed' variable.
##
request = container.REQUEST
RESPONSE =  request.RESPONSE
oftool = container.portal_openflow

instance = getattr(oftool,instance_id)
history = {}
history['instance'] = {'process_id':instance.process_id,
						'customer':instance.customer,
						'comments':instance.comments,
						'id':instance.id,
						'creation_time':instance.creation_time,
						'title':instance.title,
						'priority':instance.priority,
						'begin_process_id':instance.begin_process_id,
						'begin_activity_id':instance.begin_activity_id,
						'status':instance.status,
						'old_status':instance.old_status,
						'initiation_log':instance.initiation_log,
						'running_log':instance.running_log,
						'activation_log':instance.activation_log,
						'completion_log':instance.completion_log,
						'suspension_log':instance.suspension_log,
						'termination_log':instance.termination_log,
						'initiation_time':instance.initiation_time,
						'running_time':instance.running_time,
						'active_time':instance.active_time,
						'suspended_time':instance.suspended_time,
						'deadline':instance.deadline}

j=0

for key in history['instance'].keys():
	print key,": ", history['instance'][key]
	j+=1


history['workitems'] =[]
i=0
while i!=-1 :
	try:
		workitem = getattr(instance,str(i))
		try:
			comments = context.ext.get_comments(instance_id=workitem.instance_id,workitem_id=workitem.id)
		except:
			comments = ""
		history['workitems'].append({'id':workitem.id,
						'title':workitem.title,
						'activity_id':workitem.activity_id,
						'process_id':workitem.process_id,
						'instance_id':workitem.instance_id,
						'workitems_from':workitem.workitems_from,
						'workitems_to':workitem.workitems_to,
						'status':workitem.status,
						'event_log':workitem.event_log,
						'actor':workitem.actor,
						'graph_level':workitem.graph_level,
						'priority':workitem.priority,
						'blocked':workitem.blocked,
						'forwarded':workitem.forwarded,
						'push_roles':workitem.push_roles,
						'pull_roles':workitem.pull_roles,
						'inactivation_log':workitem.inactivation_log,
						'activation_log':workitem.activation_log,
						'completion_log':workitem.completion_log,
						'suspension_log':workitem.suspension_log,
						'fallout_log':workitem.fallout_log,
						'inactive_time':workitem.inactive_time,
						'active_time':workitem.active_time,
						'suspended_time':workitem.suspended_time,
						'fallout_time':workitem.fallout_time,
						'comments':comments})
		print i,"--------------\n"
		j=0
		print len(history['workitems'][i])," vars"
		for key in history['workitems'][i].keys():
			print key,": ", history['workitems'][i][key]
			j+=1
		i+=1
	except:
		i=-1
	

#print history.keys()
#return printed

return history
