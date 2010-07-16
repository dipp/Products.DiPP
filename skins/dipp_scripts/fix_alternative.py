## Script (Python) "URLcheck"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self, fix=0
##title=
##

# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
request  = container.REQUEST
RESPONSE = request.RESPONSE

"""this script loops through all article looking for pdf files. if only one is found is is axpected to be 
the alternative format of the fulltext and set to 'alternative_format' This is needed for the new mechanism
to display the pdf icon and the listing of alternative formats.
"""
portal_url = getToolByName(self, 'portal_url')
portal     = portal_url.getPortalObject()
articles   = container.portal_catalog(portal_type='FedoraArticle', sort_on='getPID')
print 'fix:', fix

for article in articles:
    obj       = article.getObject()
    path = '/'.join(obj.getPhysicalPath())
    PID       = obj.PID
    title       = obj.title_or_id()
    print PID,"|", path, "|", title
    #result = self.portal_catalog(Type='Fedora Multimedia', path=path, getMMType='alternative_format', sort_on='getObjPositionInParent')
    result = self.portal_catalog(Type='Fedora Multimedia', path=path, sort_on='getObjPositionInParent')
    
    for item in result:
        obj = item.getObject()
        mimetype = obj.get_content_type()
        type = obj.getMMType()
        if mimetype == 'application/pdf':
            print "  -", obj.id, type
return printed
