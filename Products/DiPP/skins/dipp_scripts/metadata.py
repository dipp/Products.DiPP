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
pdf = self.getFulltextPdf()

def fallback(target_format):
    context.plone_utils.addPortalMessage(translate('no_supported_metadata_format', default="'${fmt}' is kein unterstütztes Format.", mapping={u'fmt':target_format}, domain='dipp'))
    response.redirect('%s/citation' % context.absolute_url())

def set_headers(id, mime, ext):
    mt = "%s;charset=utf-8" % mime
    cd = 'attachment; filename=%s.%s' % (id, ext)
    response.setHeader("Content-type", mt)
    response.setHeader("Content-Transfer-Encoding", "8bit")
    response.setHeader('Content-Disposition', cd)

try:
    issn = self.issn
except:
    issn = self.portal_properties.metadata_properties.issn

context.plone_log(issn)

supported = dict((type, (name, mime, extension)) for (name, type, mime, extension) in bibtool.formats())
context.plone_log(traverse_subpath)

try:
    target_format = request.traverse_subpath[0]
except IndexError:
    target_format = None
    fallback(target_format)

if target_format in supported.keys():
    qdc = fedora.getQualifiedDCMetadata(PID)
    bc = qdc['bibliographicCitation'][0]
    year = DateTime(bc["journalIssueDate"]).strftime('%Y')
    id = qdc['creatorPerson'][0]["lastName"].lower() + str(year)
    
    citation = bibtool.convert(qdc, PID, target_format)
    ext = supported[target_format][2]
    mime = supported[target_format][1]
    
    set_headers(id, mime, ext)
    return citation

elif  target_format == "datacite" and self.DOI:
    doi = self.DOI
    citation = bibtool.datacite_xml(PID,issn=issn,publisher=publisher,pdf=pdf)
    set_headers(doi.replace('/','_'), 'text/xml', 'xml')
    return citation

elif target_format == "doaj":
    urn = self.URN
    citation = bibtool.doaj_xml(PID,issn=issn,publisher=publisher,pdf=pdf)
    set_headers(urn.replace('/','_'), 'text/xml', 'xml')
    return citation
else:
    fallback(target_format)

