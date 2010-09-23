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
feed = getToolByName(self, 'dippfeeds')
ptool = getToolByName(self, 'portal_properties')
stool = getToolByName(self, 'portal_syndication')
catalog = getToolByName(self, 'portal_catalog')
portal     = portal_url.getPortalObject()


b_size = stool.getMaxItems()

if len(request.traverse_subpath) < 1:
    msg = "No valid Feed"
    RESPONSE.redirect('%s/feeds' % context.absolute_url() + '?portal_status_message=' + msg)
else:

    articles  = catalog(portal_type='FedoraArticle',sort_on='Date', review_state=['published'])
    email = portal.email_from_address
    name = portal.email_from_name
    editor = "%s (%s)" % (email, name) 
    options = {}

    options['channel_info'] = { 'base': '2004-12-13T12:00:00Z',
                            'description': context.Description(),
                            'frequency': stool.getUpdateFrequency(),
                            'period': stool.getUpdatePeriod(),
                            'title': context.Title(),
                            'url': context.absolute_url(),
                            'managingEditor':editor}
    items = []
    for article in articles:
        item = article.getObject()
        items.append( { 'date': item.modified().HTML4(),
                        'listCreators': item.Contributors(),
                        'publisher': item.Publisher(),
                        'rights': item.Rights(),
                        'title': item.Title(),
                        'description': item.getAbstract(),
                        'category':item.getJournal_section(),
                        'url': item.absolute_url() } )

    options['listItemInfos'] = tuple(items)

    options = toUnicode( options, ptool.getProperty('default_charset', None) )
    return context.feed_template(**options)

