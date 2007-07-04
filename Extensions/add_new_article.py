# -*- coding: utf-8 -*-
"""
 id: cleanUpTemp
 title: Install DiPP workflow *optional*
 module name: DiPP.cleanupTemp
 function name: cleanup

$Id: cleanupTemp.py,v 1.1.1.1 2005/10/31 14:50:27 dippadm Exp $
"""
import string

from Products.CMFCore.utils import getToolByName
from Products.CMFCore.DirectoryView import addDirectoryViews
from time import *
from fedora.FedoraAccess import *
from fedora.FedoraManagement import *
from dipp.ContentModel import ContentModel
from DateTime import DateTime
from StringIO import StringIO


def add_new_article(self, label, PID):
    out = StringIO()
    Folders = self.objectValues('Folder')
    now = DateTime()

    print >>out, now
        
    for Folder in Folders:
        try:
            ordner   = getattr(self,Folder.id)
            DiPP     = getattr(ordner,'DiPP')
            tmp      = getattr(DiPP,'tmp')
            if DiPP.gap_container == label:
                journal = DiPP
        except:
            pass
    print >>out, 'Journal: ', journal.title
    print >>out, 'label: ', journal.gap_container
    print >>out, 'PID: ', PID
    print >>out, 'tmp: ', tmp
    return out.getvalue()    
