import csv
import time
from StringIO import StringIO
import dipp3.ContentModel
from dipp3.ContentModelService_services import *
from fedora2.FedoraManagement import *
from zLOG import LOG, ERROR, INFO

def import_backissues(self,request, file, journal, target, dryrun):

    request.RESPONSE.setHeader('Content-Type', 'text/plain;charset=utf-8;')
    JournalPID = journal.PID

    StorageType = "permanent"
    targetFormat = []

    articles = csv.DictReader(file, delimiter=",", quotechar="'")

    out = StringIO()
    print >> out, "DRYRUN:" + str(dryrun)
    print >> out, "TARGET:" + target
    print >> out, "URN:" + getContainer(self,target).absolute_url()

    for article in articles:
        
        print >> out, "\n*** Processing Article ***"        
        cModel = dipp3.ContentModel.ContentModel()
        request = setNewArticleRequest()          
        DCMetadata = request.new_in2()

        # BIBLIGRAPHIC CITATION
        print >> out, "\nBIBLIGRAPHIC CITATION"
        
        try:
            date = time.strptime(article['date'], "%Y-%m-%d")
            year = time.strftime("%Y",date)
        except ValueError, err:
            print >>out,  err
            year = "????"


        bib = {
            "journalIssueDate" : article['date'],
            "journalIssueNumber" : article['issue'],
            "journalTitle" : article['journaltitle'],
            "journalVolume" : article['vol'],
            "year" : year
        }

        bc = DCMetadata.new_bibliographicCitation()
        bc._journalIssueDate = bib['journalIssueDate']
        bc._journalIssueNumber = bib['journalIssueNumber']
        bc._journalTitle = bib['journalTitle']
        bc._journalVolume = bib['journalVolume']
        DCMetadata._bibliographicCitation.append(bc)

        print >>out, "%(journalTitle)s: Vol. %(journalVolume)s (%(journalIssueNumber)s) %(year)s [published %(journalIssueDate)s]" % bib

        # Section
        journal_section = article['journal_section']
        print >>out,"SECTION"
        print >>out, journal_section

        # Sprache
        lang = article['lang']
                
        # Title
        print >>out, "TITLE"
        title = article['title']
        x = DCMetadata.new_title()
        x._value = title
        x._lang = lang
        DCMetadata._title.append(x)

        print >>out, "%s (%s)" % (title, lang)
        
        
        
        # authors
        authors = article["authors"].rstrip(';').split(';')
        for author in authors:
            fullname = author.split(',')
            firstName = fullname[1].strip()
            lastName = fullname[0].strip()
            x = DCMetadata.new_creatorPerson()
            x._firstName = firstName
            x._lastName = lastName
            DCMetadata._creatorPerson.append(x)
            print >>out, firstName, lastName

        
        # abstract
        abstract = article['abstract']
        print >>out, "ABSTRACT"
        
        x = DCMetadata.new_DCTermsAbstract()
        x._value = abstract
        x._lang = lang
        DCMetadata._DCTermsAbstract.append(x)
        print >>out, abstract
        
        # keywords
        keywords = article['keywords'].rstrip(';').split(';')
        print >>out, "KEYWORDS"
        DCMetadata._subject = []
        for keyword in keywords:
            keyword = keyword.strip()
            DCMetadata._subject.append(keyword)
            print >>out, keyword
        
        # DDC
        ddcs = article['DDC'].rstrip(';').split(';')
        print >>out, "DDC"
        DCMetadata._DDC = []
        for ddc in ddcs:
            ddc = ddc.strip()
            DCMetadata._DDC.append(ddc)
            print >>out, ddc

        # LICENCE
        print >>out, "LICENCE"
        rights = article['Licence']
        print >>out, rights
        DCMetadata._rights = [rights]
        
        #URN
        print >>out, "URN"
        URN = article['URN']
        print >>out, URN
        DCMetadata._identifierURN = URN
        
        # Location
        Location = article['Location']
        print >>out, "LOCATION"
        print >>out, Location
        
        DCMetadata._pubType = ['article']
        DCMetadata._docType = ['text']
        language = []                            
        language.append(lang)                    
        DCMetadata.set_element_language(language)
        
        date = article['date']
        
        valid = time.mktime(time.strptime(date, "%Y-%m-%d"))
        DCMetadata._valid = valid
        DCMetadata._modified = valid 
        DCMetadata._created = valid 
        print >>out, valid
        
        ContainerPIDs = []
        container = getContainer(self,target)
        cPID = container.PID
        print >>out, "ContainerPID:", cPID
        ContainerPIDs.append(cPID)

        if not dryrun:
            PID = cModel.createNewArticle(ContainerPIDs, JournalPID, DCMetadata, Location, StorageType, targetFormat)
            LOG('DiPP', INFO, "Fetching Document from " + Location)
            LOG('DiPP', INFO, "Assigned PID:  " + PID)
            print >>out, "assigned PID:", PID

            newFedoraObject(self,out,container,PID,journal_section)

            #URN
            print >>out, "URN"
            URN = article['URN']
            DCMetadata._identifierURN = URN
            cModel.setQualifiedDCMetadata(PID,DCMetadata)
            print >>out, URN

            management = FedoraManagement()
            management.modifyObject(PID, "A", "1", "set Object active")

        else:
            print >>out, "Dryrun, not writing anything to fedora"
        
    return out.getvalue()

def getContainer(self, target):
    results = self.portal_catalog(portal_type='FedoraHierarchie', getPID=target)
    obj = results[0].getObject()
    return obj

def newFedoraObject(self,out,parent,PID, journal_section):
    """
        erstellen von FedoraArticle oder FedoraHierarchie
        in einem temp. Verzeichnis. Im ersten workflowschritt wird verschoben 
    """
    qdc = self.getQualifiedDCMetadata(PID)
    id = PID.split(':')[1]
    title = qdc['title'][0]['value']
    
    parent.invokeFactory('FedoraArticle',id=id,title=title,PID=PID)
    obj = getattr(parent,id)
    obj.manage_addProperty(id="tmp", value=False, type='boolean')
    
    #HTML_PID = self.getContentModel(PID=PID,Type='HTML')
    #Multimedia_PID = self.getContentModel(PID=PID,Type='Multimedia')
    #Native_PID = self.getContentModel(PID=PID,Type='Native')
    #XML_PID = self.getContentModel(PID=PID,Type='XML')
    #Other_PID = self.getContentModel(PID=PID,Type='Other')
    #Supplementary_PID = self.getContentModel(PID=PID,Type='Supplementary')
    
    
    """

    htmlfiles = 0
    for datastream in self.getDatastreams(PID=HTML_PID):
        if datastream['ID'][0:2] == 'DS':
            htmlfiles += 1
    
      
        
    for datastream in self.getDatastreams(PID=HTML_PID):
        if datastream['ID'][0:2] == 'DS':
            DsID = datastream['ID']
            id = datastream['label']
            label = datastream['label']
            if id == 'index_html':
                id = 'fulltext'
                title = title
                obj.manage_addProperty(id='default_page', value=id, type='string')
            elif id == 'toc_html':
                title = 'Table of Contents' 
            else:
                title = label
            stream = self.access(PID=HTML_PID,DsID=DsID,Date=None)['stream']
            MIMEType = self.access(PID=HTML_PID,DsID=DsID,Date=None)['MIMEType']
            obj.invokeFactory('FedoraDocument',id=id,title=title,PID=HTML_PID,DsID=DsID,body=stream,format=MIMEType)
            print >> out, "FedoraDocument: " + id
    
    for datastream in self.getDatastreams(PID=XML_PID):
        if datastream['ID'][0:2] == 'DS':
            DsID = datastream['ID']
            id = datastream['label']
            title = datastream['label']
            stream = self.access(PID=XML_PID,DsID=DsID,Date=None)['stream']
            MIMEType = self.access(PID=XML_PID,DsID=DsID,Date=None)['MIMEType']
            obj.invokeFactory('FedoraXML',id=id,title=title,PID=XML_PID,DsID=DsID,body=stream,format=MIMEType)
            print >> out, "FedoraXML: " + id
            
    for datastream in self.getDatastreams(PID=Multimedia_PID):
        if datastream['ID'][0:2] == 'DS':
            DsID = datastream['ID']
            id = datastream['label']
            title = datastream['label']
            obj.invokeFactory('FedoraMultimedia',id=id,title=title,PID=Multimedia_PID,DsID=DsID)
            print >> out, "FedoraMultimedia: " + id
            
    for datastream in self.getDatastreams(PID=Native_PID):
        if datastream['ID'][0:2] == 'DS':
            DsID = datastream['ID']
            id = datastream['label']
            title = datastream['label']
            obj.invokeFactory('FedoraMultimedia',id=id,title=title,PID=Native_PID,DsID=DsID)
            print >> out, "FedoraMultimedia: " + id
    
    """
    
    PDF_PID = self.getContentModel(PID=PID,Type='PDF')
    LOG('DiPP', INFO, "PDF_PID: " + PDF_PID)      
    
    datastreams = self.getDatastreams(PID=PDF_PID)
    
    print >> out,  datastreams
    for datastream in datastreams:
        if datastream['ID'].startswith('DS'):
            DsID = datastream['ID']
            id = datastream['label']
            title = datastream['label']
            #try:
            obj.invokeFactory('FedoraMultimedia',id=id,title=title,PID=PDF_PID,DsID=DsID)
            #    print >> out, "FedoraMultimedia: " + id
            #except:
            #    print >> out, "Skipped %s. ID already exists. " % id
    
    
    obj.manage_addProperty(id='layout', value='splash_screen', type='string')
    obj.setJournal_section(journal_section)
    obj.syncMetadata()
