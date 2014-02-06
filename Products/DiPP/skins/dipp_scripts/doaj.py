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
bibtool = getToolByName(self, 'bibtool')

pid = self.PID
doi = self.DOI
main_issn = self.portal_properties.metadata_properties.issn

try:
    issn = self.issn
except:
    issn =  main_issn

publisher = self.portal_properties.metadata_properties.publisher
pdf = self.getFulltextPdf()
xml = bibtool.doaj_xml(pid,issn=issn,publisher=publisher,pdf=pdf)
RESPONSE.headers['Content-disposition'] = 'attachment; filename=%s.xml' % pid.replace(':','_')
RESPONSE.headers['Content-type'] = 'text/xml; charset="utf-8'
return xml
