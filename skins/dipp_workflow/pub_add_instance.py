## Script (Python) "pub_add_instance"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=redakteur, autor, titel, jahr, ausgabe, artikel, deadline_next_date, deadline_next_time, deadline_date, deadline_time, autorOK_required, gastHrsgOK_required
##title=
##
from DateTime import DateTime

request = container.REQUEST
RESPONSE =  request.RESPONSE

oftool = container.portal_openflow

if autor=='none':   
	RESPONSE.redirect('%s/pub_add_instance_form' % context.absolute_url() +
					  '?portal_status_message=Bitte wählen Sie einen Autor!')
else:
	process_id = 'Publishing'
	customer = redakteur
	comments ='Instanz wurde angelegt'
	priority = '3'
	title = jahr + "/" + ausgabe + "/" + artikel
	activation = 0
	formalOk = 'False'
	alert = 'green'

	if autorOK_required == 'True':
		autorOk = 'False'
	else:
		autorOk = 'True'

	if gastHrsgOK_required == 'True':
		gastHrsgOK = 'False'
	else:
		gastHrsgOK = 'True'
		
	nachrichten = "Instanz wurde angelegt"
	deadline      = DateTime(deadline_date + deadline_time)
	deadline_next = DateTime(deadline_next_date + deadline_next_time)

	instance_id = oftool.addInstance(process_id=process_id, 
									 customer=customer,
									 comments=comments,
									 priority=priority,
									 title=title,
									 activation=activation)
	instance = oftool[instance_id]
	instance.manage_addProperty(id='autor',         value=autor, type='string')
	instance.manage_addProperty(id='titel',         value=titel, type='string')
	instance.manage_addProperty(id='jahr',          value=jahr, type='string')
	instance.manage_addProperty(id='ausgabe',       value=ausgabe, type='string')
	instance.manage_addProperty(id='artikel',       value=artikel, type='string')
	instance.manage_addProperty(id='autorOK',       value=autorOk, type='boolean')
	instance.manage_addProperty(id='gastHrsgOK',    value=gastHrsgOK, type='boolean')
	instance.manage_addProperty(id='formalOK',      value=formalOk, type='boolean')
	instance.manage_addProperty(id='nachrichten',   value=nachrichten, type='text')
	instance.manage_addProperty(id='deadline',      value=deadline, type='date')
	instance.manage_addProperty(id='deadline_next', value=deadline_next, type='date')
	instance.manage_addProperty(id='alert',         value=alert, type='string')
	oftool.startInstance(instance_id=instance_id)
	activation='1'
#	context.history_insert(instInstance_id=instance_id,instProcess_id=process_id,instCustomer=customer,instComments=comments,instTitle=title,instActivation=activation,instPriority=priority)
#	context.history_insert(instId=instance_id,processId=process,instAutor=autor,instTitel=titel,instJahr=jahr,instAusgabe=ausgabe,instArtikel=artikel,instFormalOk=formalOk,instAutorOk=autorOk,instNachrichten=nachrichten)

	RESPONSE.redirect('%s/pub_confirmation' % context.absolute_url() +
					  '?portal_status_message=Artikel erfolgreich angelegt!')

#~ print gastHrsgOk, gastHrsgOK_required
#~ return printed
