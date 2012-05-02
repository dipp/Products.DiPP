from fedora2.FedoraAccess import *
from fedora2.FedoraManagement import *
import os

management = FedoraManagement()


def fedora_import(self):
    WEB_DIR = "http://www.afrikanistik-online.de/download/"
    FILESYSTEM_DIR = "/themisfiles/var/www/afrika/download/"
    PID = "content:13451"
    MIMEType = "audio/mpeg"
    ControlGroup = "M"
    MDClass = ""
    MDType = ""
    DsState = "A"
    dirList = os.listdir(FILESYSTEM_DIR)

    for file_name in dirList:
        #if file_name == "WoohAli.mp3":
        file = open(FILESYSTEM_DIR + file_name)
        Label = file_name
        Location = WEB_DIR + file_name
        DsID = management.addDatastream(PID,Label,MIMEType,Location,ControlGroup,MDClass,MDType,DsState)._response
        self.invokeFactory('FedoraMultimedia', id=file_name,File=file, title=file_name, PID=PID, DsID=DsID)
        print DsID, file_name

