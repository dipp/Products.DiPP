## Script (Python) "fedoradocument_newversion"
##title=Edit content
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self

from Products.CMFCore.utils import getToolByName
REQUEST = context.REQUEST

translate = context.translate
article = context.getParentNode()

fedora = getToolByName(self, 'fedora')
dipp_tool = getToolByName(self, 'Utils')
dp = self.portal_properties.dipp_properties

PID  = REQUEST.form['PID']
DsID = REQUEST.form['DsID']
MIMEType = REQUEST.form['MIMEType']
LogMessage = REQUEST.form['LogMessage']
Label = REQUEST.form['Label']
path = context.getPhysicalPath() + ('getPrivateContent',)
Location = dipp_tool.get_location(path, REQUEST)

DsState = "A"
tempID = ""

fedora.modifyDatastreamByReference(REQUEST, PID, DsID, Label, LogMessage, Location, DsState, MIMEType, tempID)
fedora.setModified(article.PID)

# extract Table of contents from the article and save it for using in portlet
html = self.body()
if article.hasProperty('deepest_toc_level'):
    deepest_toc_level = article.deepest_toc_level
else:
    deepest_toc_level = dp.deepest_toc_level

toc = fedora.getTOC(html, levels = deepest_toc_level)

if not article.hasProperty('toc'):
    article.manage_addProperty(id='toc', value=toc, type='text')
else:
    article.manage_changeProperties({'toc':toc})

msg = "Neue Version in Fedora gespeichert! Es ist evtl. ein Reload nötig, um die neue Version in der Übersicht anzuzeigen!"
# msg = translate('new-datastream-version', domain='dipp')
context.plone_utils.addPortalMessage(msg)
return state.set(status='success')
