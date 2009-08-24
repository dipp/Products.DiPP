##Script (Python) ""
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self, aPID, aIsChildOf, aIsParentOf, aCModel, aCreator, aTitle, aSubject, aRights
##title=
##

from Products.PythonScripts.standard import html_quote
from Products.CMFCore.utils import getToolByName

oftool = container.portal_openflow
portal_url = getToolByName(self, 'portal_url')
portal = portal_url.getPortalObject()

def newArticle(id,title,PID,subject,rights):
    """
      code from checkForNewPIDs-Script
    """
    try:
       tempDir = getattr(portal,'tmp')
    except:
       portal.invokeFactory('Folder','tmp')
       tempDir = getattr(portal,'tmp')
    
    try:
        docobj = tempDir.invokeFactory('FedoraArticle',id=id,title=title,PID=PID)
        document = getattr(tempDir, id)
        document.manage_addProperty(id="tmp", value=True, type='boolean')
        document.syncMetadata()
    except:
        raise Exception, "could not create Article Object"
    return document.absolute_url()

def newInstance(PID,creator,title,cModel,isChildOf,isParentOf):
    id = aPID.split(":")[-1]
    autorOK = False    
    gastHrsgOK = False    
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

"""
main
"""
if aPID.split(':')[0] != 'temp':
    #                    newObjects += 1
    id = newInstance(aPID,aCreator,aTitle,aCModel,aIsChildOf,aIsParentOf) 
    url = newArticle(id,aTitle,aPID,aSubject,aRights)
    instance,workitem = oftool.getInstanceAndWorkitem(id,'0')
    instance.manage_changeProperties({'url':url})
else:
    id = aPID.replace(':','_')
    url = newArticle(id,aTitle,aPID,aSubject,aRights)
    #    url = newFedoraObject(id,title,PID,cModel)

return id

