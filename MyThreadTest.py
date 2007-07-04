import threading

class MyThreadTest ( threading.Thread):
    
    def __init__ (self, Supplementary_PID, fedora, obj):
        
        self.Supplementary_PID = Supplementary_PID
        self.fedora = fedora
        self.obj = obj
        threading.Thread.__init__(self)
        
    def run (self):
        
        for datastream in self.fedora.getDatastreams(PID=self.Supplementary_PID):
            if datastream['ID'][0:2] == 'DS':
                DsID = datastream['ID']
                id = datastream['label']
                title = datastream['label']
                if datastream['MIMEType'] in ['text/html']:
                    self.obj.invokeFactory('FedoraDocument',id=id,title=title,PID=self.Supplementary_PID,DsID=DsID,body=self.fedora.access(PID=self.Supplementary_PID,DsID=DsID,Date=None)['stream'])
        
        
#MyThreadTest( "My Name is", "Jochen").start()