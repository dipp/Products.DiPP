## Script (Python) "recover"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self, pid
##title=
##

# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from StringIO import StringIO
request  = container.REQUEST
RESPONSE = request.RESPONSE

oftool = container.portal_openflow
portal_url = getToolByName(self, 'portal_url')
portal = portal_url.getPortalObject()
fedora = getToolByName(self, 'fedora')
label = fedora.label

out = StringIO()

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
        
        qdc = fedora.getQualifiedDCMetadata(PID)
        
        htmlfiles = 0
        for datastream in fedora.getDatastreams(PID=HTML_PID):
            if datastream['ID'][0:2] == 'DS':
                htmlfiles += 1
            
        for datastream in fedora.getDatastreams(PID=HTML_PID):
            if datastream['ID'][0:2] == 'DS':
                DsID = datastream['ID']
                id = datastream['label']
                label = datastream['label']
                if id == 'index_html':
                    id = 'fulltext'
                    title = qdc['title'][0]['value']
                    obj.manage_addProperty(id='default_page', value=id, type='string')
                elif id == 'toc_html':
                    title = 'Table of Contents' 
                else:
                    title = label
                stream = fedora.access(PID=HTML_PID,DsID=DsID,Date=None)['stream']
                MIMEType = fedora.access(PID=HTML_PID,DsID=DsID,Date=None)['MIMEType']
                obj.invokeFactory('FedoraDocument',id=id,title=title,PID=HTML_PID,DsID=DsID,body=stream,format=MIMEType)
                print >> out, "FedoraDocument: " + id
        
        for datastream in fedora.getDatastreams(PID=XML_PID):
            if datastream['ID'][0:2] == 'DS':
                DsID = datastream['ID']
                id = datastream['label']
                title = datastream['label']
                stream = fedora.access(PID=XML_PID,DsID=DsID,Date=None)['stream']
                MIMEType = fedora.access(PID=XML_PID,DsID=DsID,Date=None)['MIMEType']
                obj.invokeFactory('FedoraXML',id=id,title=title,PID=XML_PID,DsID=DsID,body=stream,format=MIMEType)
                print >> out, "FedoraXML: " + id

        for datastream in fedora.getDatastreams(PID=Multimedia_PID):
            if datastream['ID'][0:2] == 'DS':
                DsID = datastream['ID']
                id = datastream['label']
                title = datastream['label']
                obj.invokeFactory('FedoraMultimedia',id=id,title=title,PID=Multimedia_PID,DsID=DsID)
                print >> out, "FedoraMultimedia: " + id
        
        for datastream in fedora.getDatastreams(PID=Native_PID):
            if datastream['ID'][0:2] == 'DS':
                DsID = datastream['ID']
                id = datastream['label']
                title = datastream['label']
                obj.invokeFactory('FedoraMultimedia',id=id,title=title,PID=Native_PID,DsID=DsID)
                print >> out, "FedoraMultimedia: " + id
        
        for datastream in fedora.getDatastreams(PID=PDF_PID):
            if datastream['ID'][0:2] == 'DS':
                DsID = datastream['ID']
                id = datastream['label']
                title = datastream['label']
                obj.invokeFactory('FedoraMultimedia',id=id,title=title,PID=PDF_PID,DsID=DsID)
                print >> out, "FedoraMultimedia: " + id

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
    instance.manage_addProperty(id='nachrichten',   value=comment,      type='text')
    instance.manage_addProperty(id='deadline',      value=dl,           type='date')
    instance.manage_addProperty(id='deadline_next', value=dl,           type='date')
    instance.manage_addProperty(id='alert',         value="green",     type='string')
    oftool.startInstance(instance_id=instance_id)
    return instance_id
    

queries = []
queries.append((('pid', 'has', pid),))

for query in queries:
    new = fedora.search(query)

    if len(new) == 0:
        portal_status_message = request.get('portal_status_message','Es wurden keine neuen Artikel gefunden.')

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
                fedora.modifyObject(PID,'A',None,None)

return out.getvalue()
