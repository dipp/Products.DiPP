## Script (Python) "short_history"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=

request = container.REQUEST
RESPONSE =  request.RESPONSE
oftool = container.portal_openflow

instances = {}
instances['complete']=[]
instances['running']=[]
instances['terminated']=[]

for instance in oftool.objectValues(['Instance']):
    #autor = mtool.getMemberById(instance.autor).fullname
    try:
        autor = context.ext.getMember(instance.autor)['cn']
    except:
        autor = 'n/a'
    titel = instance.titel
    id = instance.id
    if instance.status == 'complete':
        instances['complete'].append({'autor':autor,'titel':titel,'id':id})
    elif instance.status == 'running' or instance.status == 'active':
        instances['running'].append({'autor':autor,'titel':titel,'id':id})
    elif instance.status == 'terminated':
        instances['terminated'].append({'autor':autor,'titel':titel,'id':id})
    else:
        pass
    #print instance.id, instance.status
    #print instances

return instances
#return printed
