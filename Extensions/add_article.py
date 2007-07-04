# -*- coding: utf-8 -*-
import os
from DateTime import DateTime
from Products.CMFCore.utils import getToolByName

type_name = {
	'html':'Document',
	'htm':'Document',
	'txt':'Document',
	'jpg':'Image',
	'png':'Image',
	'gif':'Image'
}
text_format = {
	'html':'html',
	'htm':'html',
	'sxt':'structured-text',
	'txt':'plain',
	'jpg':'',
	'png':'',
	'gif':''
}

# Standardbesitzer aller neu angelegten Dateien
besitzer = 'redak'

def add_article(self,REQUEST,RESPONSE):
    artikelDirs        = REQUEST['artikelUrl'].split('/')
    redakteur          = REQUEST['redakteur']
    autor              = REQUEST['autor']
    autorOK_required   = REQUEST['autorOK_required']
    gastHrsgOK_required= REQUEST['gastHrsgOK_required']
    titel              = REQUEST['titel']
    dateien            = REQUEST['dateien']
    deadline_date      = REQUEST['deadline_date']
    deadline_time      = REQUEST['deadline_time']
    deadline_next_date = REQUEST['deadline_next_date']
    deadline_next_time = REQUEST['deadline_next_time']
    #	alert              = REQUEST['alert']

    portal_url = getToolByName(self, 'portal_url')
    portal = portal_url.getPortalObject()
    self = portal        

    if autor=='none':   
        RESPONSE.redirect('%s/pub_add_instance_form' % self.absolute_url() +
						  '?portal_status_message=Bitte wählen Sie einen Autor!' + 
						  '&pfad=' + REQUEST['artikelUrl'])
    else:
		artikel = artikelDirs[-1] 
		ausgabe = artikelDirs[-2] 
		jahr    = artikelDirs[-3]
		msg = ""
		
		# 2-dimensionale Liste mit allen Dateiparametern
		files=[]
		for i in range(len(dateien)):
			path = dateien[i]
			tmp = path.split('/')
			dateiname = tmp[-1]
			dateicomp = dateiname.split('.')
			extension = dateicomp[1]
			type = type_name[extension]
			format = text_format[extension]
			content = open(path,'r').read()
			files.append({'path':path, 'name':dateiname, 'type_name':type, 'text_format':format, 'content':content})
			msg += "path: " + files[i]['path'] + "\n"
			msg += "  name: " + files[i]['name'] + "\n"
			msg += "  text_format: " + files[i]['text_format'] + "\n"
			msg += "  type_name: " + files[i]['type_name'] + "\n"
			#msg += "  text: " + files[i]['text'] + "\n"
	
		# Anlegen des Jahrgangsordners	
		try:
			jahrDir = getattr(self,jahr)
			msg += "jahrDir exists\n"
		except:
			self.invokeFactory('Folder',jahr)
			jahrDir = getattr(self,jahr)
		#	jahrDir.setStatus('published')
			msg += "jahrDir created\n"
		
		# Anlegen des Ausgabenordners
		try:
			ausgabeDir = getattr(jahrDir,ausgabe)
			msg += "ausgabeDir exists\n"
		except:
			jahrDir.invokeFactory('Folder',ausgabe)
			ausgabeDir = getattr(jahrDir,ausgabe)
			msg += "ausgabeDir created\n"
		
		# Anlegen des Artikelordners
		try:
			artikelDir = getattr(ausgabeDir,artikel)
			msg += "artikelDir exists\n"
			#errorMsg="Das Verzeichnis, bzw. der Artikel existiert bereits!"
			#RESPONSE.redirect('%s/pub_upload_form' % context.absolute_url() +
					#  '?portal_status_message=' + errorMsg )
	
		except:
			ausgabeDir.invokeFactory('Folder',artikel)
			artikelDir = getattr(ausgabeDir,artikel)
			artikelDir = getattr(ausgabeDir,artikel)
			artikelDir.setTitle(titel)
			makeOwnedBy(artikelDir,besitzer)
			msg += "artikelDir created\n"
			
			# Anlegen der Dateien		
	
			for i in range(len(files)):
				msg += "# " + str(i) + ": "
				if files[i]['type_name'] == 'Document':
					# die einzige HTML-Datei soll index_html sein und
					# den Titel des Artikels tragen
					artikelDir.invokeFactory('Document',
								'index_html',
								title=titel,
								text_format=files[i]['text_format'],
								text=files[i]['content'])
					makeOwnedBy(artikelDir.index_html,besitzer)
					msg+="doc\n"
				elif files[i]['type_name'] == 'Image':
					artikelDir.invokeFactory('Image',
								files[i]['name'],
								file=files[i]['content']
								)
					bild=getattr(artikelDir,files[i]['name'])
					makeOwnedBy(bild,besitzer)
					msg+="img\n"
				else:
					msg+="kein doc\n"
			#doc = getattr(artikelDir,'AAindex_html')
			#doc.setTitle(titel)
	
		msg += jahr + "-" + ausgabe + "-" + artikel
	
	# Weiterleitung, um Workflowinstanz anzulegen
		url  = 'pub_add_instance'
		url += '?redakteur=' + redakteur
		url += '&autor=' + autor
		url += '&autorOK_required=' + autorOK_required
		url += '&gastHrsgOK_required=' + gastHrsgOK_required
		url += '&titel=' + titel
		url += '&jahr=' + jahr
		url += '&ausgabe=' + ausgabe
		url += '&artikel=' + artikel
		url += '&deadline_date=' + deadline_date
		url += '&deadline_time=' + deadline_time
		url += '&deadline_next_date=' + deadline_next_date
		url += '&deadline_next_time=' + deadline_next_time
#		url += '&alert=' + alert
	
	#	return msg 
		RESPONSE.redirect(url)

def makeOwnedBy(obj, new_owner_id):
	new_owner_obj = obj.acl_users.getUser(new_owner_id)
	new_owner_obj = new_owner_obj.__of__(obj.acl_users)
	obj.changeOwnership(new_owner_obj)
	obj.manage_setLocalRoles(new_owner_id, ['Owner'])
	obj.reindexObject()
