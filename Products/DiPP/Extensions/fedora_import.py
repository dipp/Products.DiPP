from dipp.fedora2.FedoraAccess import *
from dipp.fedora2 import FedoraManagement
from StringIO import StringIO
import os

fedoramanagement = FedoraManagement.FedoraManagement()


# Batchimport eines Verzeichnisse mit Audiodateien nach Fedora und Plone
#
# im Artikelordner musse eine externe Methode wie folgt angelegt werden:
#
# Id: fedora_import (beliebig)
# Title: import from filesystem (beliebig)
# Module Name: DiPP.fedora_import
# Function Name: fedora_import

# Verzeichnis mit den mp3 Dateien 
FILESYSTEM_DIR = "/files/var/www/import/"

# URL, unter der das Verzeichnis abbrufbar ist
WEB_DIR = "http://alkyoneus.hbz-nrw.de/import/"

# PID des Fedoraobjekts, in das die Dateien als Datenströme 
# abgelegt werden sollen
PID = "content:21766"

def fedora_import(self):
    out = StringIO()
    MIMEType = "audio/mpeg"
    ControlGroup = "M"
    MDClass = ""
    MDType = ""
    DsState = "A"
    dirList = os.listdir(FILESYSTEM_DIR)
    for file_name in dirList:
        file = open(FILESYSTEM_DIR + file_name)
        Label = file_name
        Location = WEB_DIR + file_name
        DsID = fedoramanagement.addDatastream(PID,Label,MIMEType,Location,ControlGroup,MDClass,MDType,DsState)
        self.invokeFactory('FedoraMultimedia', id=file_name,File=file, title=file_name, PID=PID, DsID=DsID)
        audio = getattr(self, file_name)
        audio.manage_addProperty(id='layout', value="mmmp3_view", type='string')
        audio.reindexObject()
        print >> out,  Location, DsID
    
    return out.getvalue()
