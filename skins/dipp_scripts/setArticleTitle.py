## Script (Python) "checkForNewPIDs"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self
##title=
##

# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
request  = container.REQUEST
RESPONSE = request.RESPONSE

fedora = getToolByName(self, 'fedora')
results = context.portal_catalog.searchResults(
    Type = "Fedora Article"
)

print len(results), "Fedora Article"
for result in results:
    article = result.getObject()
    PID = article.PID
   
    #index_html
    try:
        x = getattr(article,'index_html')
        qdc = fedora.getQualifiedDCMetadata(PID)
        title = qdc['title'][0]['value']
        x.setTitle(title)
        print len(qdc['title']), x.PID, x.title, title
    except:
        print "No index_html at ", article.absolute_url()
    
    #toc_html
    try:
        x = getattr(article,'toc_html')
        title = "Table of Contents"
        x.setTitle(title)
        print  x.PID, x.title, title
    except:
        print "No toc_html at ", article.absolute_url()

    print ""

return printed
