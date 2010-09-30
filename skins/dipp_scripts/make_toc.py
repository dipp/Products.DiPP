## Script (Python) "make_toc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self
##title=
##

from Products.CMFCore.utils import getToolByName
request     = container.REQUEST
RESPONSE    = request.RESPONSE

ftool = getToolByName(context, 'fedora')
path ='/'.join(self.getPhysicalPath());
items = self.portal_catalog(path=path,portal_type=('FedoraArticle','FedoraHierarchie'))
articles = []

for item in items:
    if item.portal_type == "FedoraArticle":
        articles.append(item.getObject())

toc = []
for article in articles:
    qdc = ftool.getQualifiedDCMetadata(article.PID)
    titles = qdc['title']
    authors = qdc['creatorPerson']
    url = article.absolute_url
    toc.append({'titles':titles,'authors':authors,'url':url})

return toc
