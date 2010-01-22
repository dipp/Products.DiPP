# -*- coding: utf-8 -*-
#
# 
# 
# $Id: cleanupTemp.py,v 1.1.1.1 2005/10/31 14:50:27 dippadm Exp $
import string

from Products.CMFCore.utils import getToolByName
from Products.CMFCore.DirectoryView import addDirectoryViews
from time import *
from fedora2.FedoraAccess import *
from fedora2.FedoraManagement import *
from dipp2.ContentModel import ContentModel
from DateTime import DateTime
from StringIO import StringIO


EXCEPTIONS = ['']
LIMIT = 1

def getContainers(PID):
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
    management = FedoraManagement()
    management.purgeObject(PID,'deleted')

def cleanAll(self, out):
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
                                purgeObject(container)

                            purgeObject(PID)
                             
                           
                    except:
                        pass
                    #print >>out, "Object doesn't have a PID"
                print >>out, "%s articles, %s temporary, %s deleted" % (articles,temporary, deleted)
            
        except:
            #pass
            print "Hmmm, something went wrong"
        
def cleanOne(self,out,PID):

    containers = getContainers(PID)

    for container in containers:
        purgeObject(container)
        print >>out,  container, " deleted"

    purgeObject(PID)
    print >>out, PID," deleted"

def run(self,PID=None):
    out = StringIO()
    if PID:
        cleanOne(self,out,PID)
    else:
        cleanAll(self,out)
    return out.getvalue()
    
