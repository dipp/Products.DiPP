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

items = self.getFolderListingFolderContents(suppressHiddenFiles=1) 
articles = []

for item in items:
    if item.portal_type == "FedoraArticle":
        articles.append(item)

toc = []
for article in articles:
    qdc = ftool.getQualifiedDCMetadata(article.PID)
    titles = qdc['title']
    authors = qdc['creatorPerson']
    url = article.absolute_url
    toc.append({'titles':titles,'authors':authors,'url':url})

return toc
