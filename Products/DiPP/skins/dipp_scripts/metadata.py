## Script (Python) "metadata"
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
from Products.CMFDefault.utils import toUnicode

request  = container.REQUEST
response = request.RESPONSE

fedora = getToolByName(self, "fedora")
bibtool = getToolByName(self, 'bibtool')
translate = context.translate

PID = self.PID

publisher = self.portal_properties.metadata_properties.publisher

try:
    issn = self.issn
except:
    issn = self.portal_properties.metadata_properties.issn

context.plone_log(issn)

supported = dict((type, (name, mime, extension)) for (name, type, mime, extension) in bibtool.formats())

try:
    target_format = request.traverse_subpath[0]
except IndexError:
    target_format = ""

if len(request.traverse_subpath) == 0 or target_format not in supported.keys():
    context.plone_utils.addPortalMessage(translate('no_supported_metadata_format', default="'${fmt}' is kein unterstütztes Format.", mapping={u'fmt':target_format}, domain='dipp'))
    response.redirect('%s/citation' % context.absolute_url())
#elif target_format not in supported.keys():
#    response.setStatus("404", reason="Not found", lock=None)
else:
    qdc = fedora.getQualifiedDCMetadata(PID)
    bc = qdc['bibliographicCitation'][0]
    year = DateTime(bc["journalIssueDate"]).strftime('%Y')
    id = qdc['creatorPerson'][0]["lastName"].lower() + str(year)
    
    citation = bibtool.convert(qdc, PID, target_format)
    ext = supported[target_format][2]
    
    mime = supported[target_format][1]
    
    mt = "%s;charset=utf-8" % mime
    response.setHeader("Content-type", mt)
    response.setHeader("Content-Transfer-Encoding", "8bit")
    
    cd = 'attachment; filename=%s.%s' % (id, ext)
    response.setHeader('Content-Disposition', cd)
    
    return citation

