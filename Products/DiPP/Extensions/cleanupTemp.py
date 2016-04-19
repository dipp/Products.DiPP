# -*- coding: utf-8 -*-
#
# This skript deletes temporary files in Plone, i.e. Testkonversions, which are
# stored in the tmp-folder of a Journalistance. An external Method has to be
# placed in the ZMI of the Zopeinstanz (not Ploninstance!) with following
# settings:
#
# Id:            cronCleanup
# Title:         delete temporary files
# Module Name:   DiPP.cleanupTemp
# Function Name: run
#
# It can be run manually from the test Tab of the external Method or ideally on
# regular basis by a cron job, e.g. at 2:00 each night:
# 
# 0 2 * * * /usr/bin/wget -O - http://localhost:9080/cronCleanup
# 
# Only one script is needed per Zopeinstance since it find all installed
# Journals.
#
# $Id$

import string

from Products.CMFCore.utils import getToolByName
from Products.CMFCore.DirectoryView import addDirectoryViews
from time import *
from dipp.fedora2.FedoraAccess import *
from dipp.fedora2.FedoraManagement import *
from dipp.dipp3.ContentModel import ContentModel
from DateTime import DateTime
from StringIO import StringIO

# when on journal should be excluded from regular cleaning, the id of the
# mountpoint can be put in this list:
EXCEPTIONS = ['']

# maximum age of a testkonversion (in days)
LIMIT = 1

def getContainers(PID):
    """return a list with the PIDs of the content Containers """
    
    cModel = ContentModel()
    response =cModel.getContentModel(PID)
    list = []
    list.append(response._objectHTML)
    list.append(response._objectMultimedia)
    list.append(response._objectNative)
    list.append(response._objectOther)
    list.append(response._objectPDF)
    list.append(response._objectXML)
    list.append(response._objectOther)
    return list

def purgeObject(PID):
    """permanently delete an object from the fedora repository"""
    
    management = FedoraManagement()
    management.purgeObject(PID,'deleted')

def cleanAll(self, out):
    """loop through all journals and delete all temp Articles older than LIMIT"""
    
    Folders = self.objectValues('Folder')
    print Folders
    now = DateTime()

    print >>out, now
        
    for Folder in Folders:
        print >>out, Folder.id 
        try:
            ordner   = getattr(self,Folder.id)
            DiPP     = getattr(ordner,'DiPP')
            tmp      = getattr(DiPP,'tmp')
        except:
            EXCEPTIONS.append(Folder.id)
            
        try:        
            if Folder.id in EXCEPTIONS:
                print >>out, '\n***',DiPP.title, '***'
                print >>out, '\n    skipped'
                
            else:
                print >>out, '\n***',DiPP.title, '***'
                results = DiPP.portal_catalog.searchResults(
                    Type = "Fedora Article",
                )
                articles  = 0
                temporary = 0
                deleted   = 0
                for result in results:
                    obj = result.getObject()
                    try:
                        PID     = obj.PID
                        storage = PID.split(':')[0]
                        articles += 1
                        age = now - DateTime(obj.CreationDate())
                        
                        if storage == 'temp':
                            temporary += 1
                        if storage == 'temp' and age > LIMIT:
                            deleted += 1
                            id = obj.id
                            
                            obj.getParentNode().manage_delObjects([obj.id])
                            containers = getContainers(PID)
                        
                            for container in containers:
                                # purgeObject(container)
                                print >>out, "purge container"
                            #purgeObject(PID)
                            print >>out, "purge object"
                             
                           
                    except:
                        pass
                    #print >>out, "Object doesn't have a PID"
                print >>out, "%s articles, %s temporary, %s deleted" % (articles,temporary, deleted)
            
        except:
            #pass
            print "Hmmm, something went wrong"
        
def cleanOne(self,out,PID):
    """just delete the article object and it content containers of a given PID"""

    containers = getContainers(PID)

    for container in containers:
        purgeObject(container)
        print >>out,  container, " deleted"

    purgeObject(PID)
    print >>out, PID," deleted"

def run(self,PID=None):
    """if a PID is given, delete just this article, otherwise all"""
    
    out = StringIO()
    if PID:
        cleanOne(self,out,PID)
    else:
        cleanAll(self,out)
    return out.getvalue()
    
