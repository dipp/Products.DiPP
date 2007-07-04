import os

#repository = here.portal_properties.repository

def listDir(pfad):
    try:
         return os.listdir(pfad)
    except:
        return 'Fehler beim Holen des Verzeichnisses'
