## Script (Python) "doaj"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self
##title=
##

request = container.REQUEST
RESPONSE = request.RESPONSE
sub_path = traverse_subpath
translate = context.translate

from Products.CMFCore.utils import getToolByName

path = '/'.join(self.getPhysicalPath())
catalog = getToolByName(self, 'portal_catalog')
bibtool = getToolByName(self, 'bibtool')

results = catalog(portal_type=('FedoraArticle'), Language='all', path=path,sort_on='getPID', sort_order='reverse')

pids = []

for result in results:
    pids.append(result.getPID)

(skipped, xml) = bibtool.doaj_xml(pids)
self.plone_log("Skipped PIDs" + str(skipped))
if len(sub_path) == 0:
    if len(skipped) > 0:
        portal_status_message = "skipped: " + str(skipped)
        context.plone_utils.addPortalMessage(portal_status_message)
    return xml

elif len(sub_path) == 1 and sub_path[0] == 'download':
    print xml
    RESPONSE.headers['Content-disposition'] = 'attachment; filename=doaj.xml'
    RESPONSE.headers['Content-type'] = 'text/xml; charset="utf-8'
    return printed
