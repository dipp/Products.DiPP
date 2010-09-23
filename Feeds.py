# -*- coding: utf-8 -*-
# ...
# File: Feeds.py
#
# German Free Software License (D-FSL)
#
# This Program may be used by anyone in accordance with the terms of the
# German Free Software License
# The License may be obtained under <http://www.d-fsl.org>.
#
# $Id: FedoraTool.py 2132 2010-06-04 07:08:42Z reimer $

from  elementtree.ElementTree import Element, SubElement
import elementtree.ElementTree as ET    
import datetime
import PyRSS2Gen
from DateTime import DateTime
from OFS.SimpleItem import SimpleItem
from AccessControl import ClassSecurityInfo
from Products.CMFCore.utils import UniqueObject, getToolByName

class Feeds(UniqueObject, SimpleItem):
    """ Wrapper for Bibutils """
    
    meta_type = 'Feeds'
    id = 'feeds'
    title = 'Provide RSS of of articles'
    toolicon = 'skins/dipp_images/fedora.png'
    security = ClassSecurityInfo()

   
    def indent(self, elem, level=0):
        """Pretty printing of the mods xml format"""

        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.indent(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i
   
    
    def rss(self):
        portal_url = getToolByName(self, 'portal_url')
        portal = portal_url.getPortalObject()
        title = portal.title
        articles   = self.portal_catalog(portal_type='FedoraArticle',sort_on='Date', review_state=['published'])
        description = portal.description
        items = []
        for article in articles:
            obj = article.getObject()            
            # PyRSS2Gen.RSSItem(title, link, description, author, categories, comments, enclosure, guid, pubDate, source)      
            try:
                author = obj.Contributors()[0]
            except:
                author = None
            item = PyRSS2Gen.RSSItem(
                title = obj.title,
                link = article.getURL(),
                description = obj.getAbstract(),
                categories = ['Development'],
                author = author,
                guid = PyRSS2Gen.Guid("http://nbn-resolving.org/urn/resolver.pl?"+obj.PID),
                #pubDate = obj.Date()
                pubDate = "2009-09-01T17:03:32Z"
            )
            items.append(item)
            

        feed = PyRSS2Gen.RSS2(
            title = title,
            link = portal.absolute_url(),
            description = description,
            lastBuildDate = datetime.datetime.now(),
            items = items)
        
        return feed.to_xml()
        
