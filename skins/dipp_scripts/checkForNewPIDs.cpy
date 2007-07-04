## Script (Python) "checkForNewPIDs"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self,new_pid
##title=
##

# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
#from Products.DiPP import MyThreadTest
#from Products.DiPP.MyThreadTest import MyThreadTest
request  = container.REQUEST
RESPONSE = request.RESPONSE

oftool = container.portal_openflow
portal_url = getToolByName(self, 'portal_url')
portal = portal_url.getPortalObject()
fedora = getToolByName(self, 'fedora')
#myThread = getToolByName(self, 'mythread')
GAP_CONTAINER = self.portal_properties.gap_container
#CRON = request.form['cron']

'''
besitzer = 'redak'

def makeOwnedBy(obj, new_owner_id):
    new_owner_obj = obj.acl_users.getUser(new_owner_id)
    new_owner_obj = new_owner_obj.__of__(obj.acl_users)
    obj.changeOwnership(new_owner_obj)
    obj.manage_setLocalRoles(new_owner_id, ['Owner'])
    obj.reindexObject()
'''

def newFedoraObject(id,title,PID,cModel):
    """
        erstellen von FedoraArticle oder FedoraHierarchie
        in einem temp. Verzeichnis. Im ersten workflowschritt wird verschoben 
    """
    try:
        tempDir = getattr(portal,'tmp')
    except:
        portal.invokeFactory('Folder','tmp')
        tempDir = getattr(portal,'tmp')
        
    if cModel == "DiPP:article":
        # anlegen des Artikel-Ordners
        tempDir.invokeFactory('FedoraArticle',id=id,title=title,PID=PID)
        obj = getattr(tempDir,id)
        obj.manage_addProperty(id="tmp", value=True, type='boolean')
        url = str(obj.absolute_url())
        
        HTML_PID = fedora.getContentModel(PID=PID,Type='HTML')
        Multimedia_PID = fedora.getContentModel(PID=PID,Type='Multimedia')
        Native_PID = fedora.getContentModel(PID=PID,Type='Native')
        XML_PID = fedora.getContentModel(PID=PID,Type='XML')
        PDF_PID = fedora.getContentModel(PID=PID,Type='PDF')
        Other_PID = fedora.getContentModel(PID=PID,Type='Other')
        Supplementary_PID = fedora.getContentModel(PID=PID,Type='Supplementary')
        
            
        
        htmlfiles = 0
        for datastream in fedora.getDatastreams(PID=HTML_PID):
            if datastream['ID'][0:2] == 'DS':
                htmlfiles += 1
            
        for datastream in fedora.getDatastreams(PID=HTML_PID):
            if datastream['ID'][0:2] == 'DS':
                DsID = datastream['ID']
                id = datastream['label'].replace('.','_')
                title = datastream['label']
                obj.invokeFactory('FedoraDocument',id=id,title=title,PID=HTML_PID,DsID=DsID,body=fedora.access(PID=HTML_PID,DsID=DsID,Date=None)['stream'])
        try:
            obj.invokeFactory('dipa_entry',id='index_html',title='Metadata')
        except:
            pass
        
        for datastream in fedora.getDatastreams(PID=XML_PID):
            if datastream['ID'][0:2] == 'DS':
                DsID = datastream['ID']
                id = datastream['label'].replace('.','_')
                title = datastream['label']
                obj.invokeFactory('FedoraDocument',id=id,title=title,PID=XML_PID,DsID=DsID,body=fedora.access(PID=XML_PID,DsID=DsID,Date=None)['stream'],text_format="xml")

        for datastream in fedora.getDatastreams(PID=Multimedia_PID):
            if datastream['ID'][0:2] == 'DS':
            #elif datastream['MIMEType'] in ['image/jpeg','image/jpg','image/gif']:
                DsID = datastream['ID']
                id = datastream['label']
                title = datastream['label']
                obj.invokeFactory('FedoraMultimedia',id=id,title=title,PID=Multimedia_PID,DsID=DsID)
        
        for datastream in fedora.getDatastreams(PID=Native_PID):
            if datastream['ID'][0:2] == 'DS':
                DsID = datastream['ID']
                id = datastream['label']
                title = datastream['label']
                obj.invokeFactory('FedoraMultimedia',id=id,title=title,PID=Native_PID,DsID=DsID)
        
        for datastream in fedora.getDatastreams(PID=PDF_PID):
            if datastream['ID'][0:2] == 'DS':
            #elif datastream['MIMEType'] in ['image/jpeg','image/jpg','image/gif']:
                DsID = datastream['ID']
                id = datastream['label']
                title = datastream['label']
                obj.invokeFactory('FedoraMultimedia',id=id,title=title,PID=PDF_PID,DsID=DsID)

        #MyThreadTest(Supplementary_PID, fedora, obj).start()
        #st = 'newFedoraObject myThreadTest was called'
        #context.plone_log(st)
        #myThread( Supplementary_PID, fedora).start()                
        #fedora.lazyIndex(Supplementary_PID, fedora, obj)
        #for datastream in fedora.getDatastreams(PID=Supplementary_PID):
        #    if datastream['ID'][0:2] == 'DS':
        #        DsID = datastream['ID']
        #        id = datastream['label']
        #        title = datastream['label']
        #        if datastream['MIMEType'] in ['text/html']:
        #            obj.invokeFactory('FedoraDocument',id=id,title=title,PID=Supplementary_PID,DsID=DsID,body=fedora.access(PID=Supplementary_PID,DsID=DsID,Date=None)['stream'])
        
    elif cModel == "DiPP:container":
        tempDir.invokeFactory('FedoraHierarchie',id=id,title=title,PID=PID)
        obj = getattr(tempDir,id)
        obj.manage_addProperty(id="tmp", value=True, type='boolean')
        # index Datei anlegen
        #description ="""Dies ist eine Standardseite für hierarchische Elemente einer Zeitschrift."""
        description = ""
        obj.invokeFactory('Document',id='index_html',title=title,description=description,text_format="html")
        url = str(obj.absolute_url())
    return url
   
def newInstance(PID,creator,title,cModel,isChildOf,isParentOf):

    if cModel == "DiPP:article":
        id = PID.split(":")[-1]
        autorOK = False    
        gastHrsgOK = False    
        formalOK = False    
    else:
        id = title
        autorOK = True
        gastHrsgOK = True
        formalOK = False    

    dl = self.portal_properties.deadline_no
    comment = "New digital object found in Fedora!"
    instance_id = oftool.addInstance(process_id='Publishing',
                                     customer='auto',
                                     comments='added new instance',
                                     priority='3',
                                     title=id,
                                     activation=0)
    instance = oftool[instance_id]
    instance.manage_addProperty(id='PID',           value=PID,          type='string')
    instance.manage_addProperty(id='isChildOf',     value=isChildOf,    type='lines')
    instance.manage_addProperty(id='isParentOf',    value=isParentOf,   type='lines')
    instance.manage_addProperty(id='type',          value=cModel,       type='string') 
    instance.manage_addProperty(id='url',           value="",           type='string')
    instance.manage_addProperty(id='autor',         value=creator,      type='string')
    instance.manage_addProperty(id='gastHrsg',      value="",           type='string')
    instance.manage_addProperty(id='titel',         value=title,        type='string')
    instance.manage_addProperty(id='hierarchie',    value="n/a",        type='string')
    instance.manage_addProperty(id='autorOK',       value=autorOK,      type='boolean')
    instance.manage_addProperty(id='gastHrsgOK',    value=gastHrsgOK,   type='boolean')
    instance.manage_addProperty(id='formalOK',      value=formalOK,     type='boolean')
#    instance.manage_addProperty(id='licenceAgree',  value=False,        type='boolean')
    instance.manage_addProperty(id='nachrichten',   value=comment,      type='text')
    instance.manage_addProperty(id='deadline',      value=dl,           type='date')
    instance.manage_addProperty(id='deadline_next', value=dl,           type='date')
    instance.manage_addProperty(id='alert',         value="green",     type='string')
    oftool.startInstance(instance_id=instance_id)
    return instance_id
    
# new_pid = 1: wenn über cronjob abgerufen. In all_worklists explizit auf 1 gesetzt

queries = []
if new_pid == "1":
    queries.append((('state','has','I'),('label','has',GAP_CONTAINER),('description','has','dipp-converted'),))
    queries.append((('state','has','I'),('label','has',GAP_CONTAINER),('description','has','1'),))
else:
    queries.append((('pid','has',new_pid),))

for query in queries:
    new = fedora.search(query)

    if len(new) == 0:
        portal_status_message = request.get('portal_status_message','Es wurden keine neuen Artikel gefunden.')
        #portal_status_message = 'Es wurden keine neuen Artikel gefunden.'

    else:
        
        newObjects = 0    
        tempObjects = 0    
        for obj in new:
            PID = obj['PID']
            creator = obj['creator']
            title = obj['title']
            cModel = obj['cModel']
            isChildOf   = obj['isChildOf']
            isParentOf  = obj['isParentOf']
            description  = obj['description']
            context.plone_log(description)

            if cModel in ['DiPP:container','DiPP:article']:
                newObjects += 1
                if PID.split(':')[0] != 'temp':
                    newObjects += 1
                    id = newInstance(PID,creator,title,cModel,isChildOf,isParentOf) 
                    url = newFedoraObject(id,title,PID,cModel)
                    instance,workitem = oftool.getInstanceAndWorkitem(id,'0')
                    instance.manage_changeProperties({'url':url})
                else:
                    tempObjects += 1
                    id = PID.replace(':','_')
                    url = newFedoraObject(id,title,PID,cModel)
                #context.fedoraModifyObject(PID,'A',None,None)
                fedora.modifyObject(PID,'A',None,None)

            portal_status_message = "Es wurden " + str(newObjects) + " neue(r) Artikel gefunden, davon " + str(tempObjects) + " temporäre(r) Artikel"

request.RESPONSE.redirect(request.HTTP_REFERER + "?portal_status_message=" + portal_status_message)
