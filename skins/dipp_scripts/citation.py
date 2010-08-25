## Script (Python) "citation"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self, target_format, PID
##title=
##

# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
request  = container.REQUEST
response = request.RESPONSE

fedora = getToolByName(self, "fedora")
bibtool = getToolByName(self, "bibtool")

qdc = fedora.getQualifiedDCMetadata(PID)

bc = qdc['bibliographicCitation'][0]
year = DateTime(bc["journalIssueDate"]).strftime('%Y')
id = qdc['creatorPerson'][0]["lastName"].lower() + str(year)

formats = {
    "end":{"MIMEType":"application/x-endnote-refer","Extension":"enw"},
    "bib":{"MIMEType":"application/x-bibtex","Extension":"tex"},
    "ris":{"MIMEType":"application/x-research-info-systems","Extension":"ris"},
    "xml":{"MIMEType":"text/xml","Extension":"xml"}
}

ext = formats[target_format]["Extension"]
mime = formats[target_format]["MIMEType"]
citation = bibtool.convert(qdc, PID, target_format)

mt = "%s;charset=utf-8" % mime
response.setHeader("Content-type", mt)
response.setHeader("Content-Transfer-Encoding", "8bit")

cd = 'attachment; filename=%s.%s' % (id, ext)
response.setHeader('Content-Disposition', cd)

return citation
