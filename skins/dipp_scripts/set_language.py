## Script (Python) "set_language"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self
##title=
##
request = container.REQUEST
RESPONSE =  request.RESPONSE

from Products.CMFCore.utils import getToolByName

FOLDER = ('',)
DEPTH = 10
TYPES = (
    "Fedora Article",
    "Fedora Document",
    "Fedora XML",
    "Fedora Hierarchie",
    "Fedora Multimedia",
    "Volume",
    "Issue"
    )
portal = getToolByName(self, 'portal_url').getPortalObject()
catalog = getToolByName(self, 'portal_catalog')

portal_path = portal.getPhysicalPath()
folder_path = portal_path + FOLDER
path = '/'.join(folder_path)
print  path
query = {'query':path, 'depth':DEPTH}
results = catalog.searchResults(Type=TYPES, Language='all', path=query)

print len(results)
for item in results:
    obj = item.getObject()
    obj.setLanguage('')
    obj.reindexObject()
    print item.Type, obj.Language(), item.getURL()

return printed
