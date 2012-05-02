## Script (Python) "feeds"
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
RESPONSE = request.RESPONSE

portal_url = getToolByName(self, 'portal_url')
ptool = getToolByName(self, 'portal_properties')
stool = getToolByName(self, 'portal_syndication')
bibtool = getToolByName(self, 'bibtool')
catalog = getToolByName(self, 'portal_catalog')
avtm = getToolByName(self, 'portal_vocabularies')
portal     = portal_url.getPortalObject()

limit = stool.getMaxItems()

journalsections = avtm.getVocabularyByName('journal-sections')
section_dict = journalsections.getVocabularyDict(journalsections)
types = ('articles','events')

try:
    type = request.traverse_subpath[0]
except IndexError:
    type = ""

try:
    section = request.traverse_subpath[1]
except IndexError:
    section = ""

section_name = section_dict.get(section,"All articles")

if len(request.traverse_subpath) == 0 or type not in types:
    msg = "No valid Feed"
    RESPONSE.redirect('%s/feeds' % context.absolute_url() + '?portal_status_message=' + msg)

elif type == "articles":

    articles  = catalog(
                    portal_type='FedoraArticle',
                    review_state=['published'],
                    getJournal_section=section,
                    sort_on='Date',
                    sort_order='reverse',
                    sort_limit=limit
                )[:limit]

    email = portal.email_from_address
    name = portal.email_from_name
    editor = "%s (%s)" % (email, name) 
    title = "%s - %s" % (portal.Title(),section_name)
    description = portal.Description(),
    options = {}
    
    options['image_info'] = {'title':title,
                             'link':portal.absolute_url(),
                             'url':portal.absolute_url() + '/logo.gif'}
    
    options['channel_info'] = { 'base': '2004-12-13T12:00:00Z',
                            'description':description,
                            'frequency': stool.getUpdateFrequency(),
                            'period': stool.getUpdatePeriod(),
                            'title': title,
                            'url': context.absolute_url(),
                            'managingEditor':editor}
    items = []
    for article in articles:
        item = article.getObject()

        section = item.getJournal_section()
        if section != 'no-section':
            category = section_dict.get(section, None)
        else:
            category = None
        citation = bibtool.short_citation(item)
        abstract = item.getAbstract()
        description = "%s: %s" % (citation, abstract)
        items.append( { 'date':item.effective().HTML4(),
                        'listCreators': item.Contributors(),
                        'publisher': item.Publisher(),
                        'rights': item.Rights(),
                        'title': item.Title(),
                        'description': description,
                        'category':category,
                        'url': item.absolute_url() } )

    options['listItemInfos'] = tuple(items)

    options = toUnicode( options, ptool.getProperty('default_charset', None) )
    return context.feed_template(**options)

