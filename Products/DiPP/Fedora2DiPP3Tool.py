# -*- coding: utf-8 -*-
# The FedoraTool for adding and manipulating objects in Fedora
#
# German Free Software License (D-FSL)
#
# This Program may be used by anyone in accordance with the terms of the
# German Free Software License
# The License may be obtained under <http://www.d-fsl.org>.
#
# $Id$

__docformat__ = "restructuredtext"

from OFS.SimpleItem import SimpleItem
from OFS.Folder import Folder
from AccessControl import ClassSecurityInfo
from Products.CMFCore.utils import UniqueObject, getToolByName
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
try:
    from Products.CMFCore.permissions import ManagePortal
    from Products.CMFCore.permissions import View
except ImportError:
    from Products.CMFCore.CMFCorePermissions import ManagePortal
    from Products.CMFCore.CMFCorePermissions import View

from DateTime import DateTime
from time import mktime, strptime, strftime
from marshal import loads
from zlib import decompress
from urllib import unquote
from threading import Timer
from htmldiff import htmldiff
import httplib
import urlparse
import logging

from dipp.fedora2 import FedoraAccess
from dipp.fedora2 import FedoraManagement
from dipp.fedora2.config import ADDRESS, PORT
from dipp.dipp3 import ContentModel
from dipp.tools import openurl

from backissues import import_backissues
from config import view_permission, LANGUAGES, DEFAULT_METADATA

logger = logging.getLogger("DiPP")

class Fedora(UniqueObject, Folder):
    """Tool to add and modify Data in the Fedora Repository """

    meta_type = 'Fedora2DiPP3'
    id = 'fedora'
    title = 'Interact with the repository Fedora 2 und DiPP3'
    toolicon = 'skins/dipp_images/fedora.png'
    security = ClassSecurityInfo()
    
    fedoraaccess = FedoraAccess.FedoraAccess()
    fedoramanagement = FedoraManagement.FedoraManagement()
    
    manage_search_form = PageTemplateFile('www/search_form.pt', globals())
    security.declareProtected(view_permission, 'manage_search_form')

    manage_deleteObjectForm = PageTemplateFile('www/deleteobject_form.pt', globals())
    security.declareProtected(view_permission, 'manage_deleteObjectForm')

    manage_backissues_form = PageTemplateFile('www/backissues_form.pt', globals())
    security.declareProtected(view_permission, 'manage_backissues_form')
                
    manage_config_form = PageTemplateFile('www/config_form.pt', globals())
    security.declareProtected(view_permission, 'manage_config_form')
    
    manage_maintenance_form = PageTemplateFile('www/maintenance_form.pt', globals())
    security.declareProtected(view_permission, 'manage_maintenance_form')
    
    manage_urn_form = PageTemplateFile('www/urn_form.pt', globals())
    security.declareProtected(view_permission, 'manage_urn_form')
    
    manage_metadata_form = PageTemplateFile('www/metadata_form.pt', globals())
    security.declareProtected(view_permission, 'manage_metadata_form')
    
    manage_options = ({'label':'Search',
                       'action':'manage_search_form',
                       'help':('PloneFedora2', 'search.stx')},
                      {'label':'Configure',
                       'action':'manage_config_form',
                       'help':('PloneFedora2', 'search.stx')},
                      {'label':'Metadata',
                       'action':'manage_metadata_form',
                       'help':('PloneFedora2', 'metadata.stx')},
                      {'label':'Maintenance',
                       'action':'manage_maintenance_form',
                       'help':('PloneFedora2', 'search.stx')},
                      {'label':'URN',
                       'action':'manage_urn_form',
                       'help':('PloneFedora2', 'search.stx')},
                      {'label':'Backissues',
                       'action':'manage_backissues_form',
                       'help':('PloneFedora2', 'backissues.stx')},
        ) + Folder.manage_options

    def __init__(self):
        self.PID = "" 
        self.label = "" 
        self.metadata = {}
        for metadata in self.getQualifiedDCMetadata(PID=None).keys():
            self.metadata[metadata] = {'required':True,'visible':True,'default':''}
        
        for metadate, visible, required, default in DEFAULT_METADATA:
            self.metadata[metadate]['visible'] = visible
            self.metadata[metadate]['required'] = required
            self.metadata[metadate]['default'] = default
        
    security.declareProtected(ManagePortal, 'manage_setFedoraSettings')
    def manage_setFedoraSettings(self, PID, label, REQUEST):
        """ZMI method to store the configuration of the fedora tool."""
        self.PID = PID
        self.label = label
        manage_tabs_message = "Saved"
        logger.info("saved Fedora Configuration")
        return self.manage_config_form(REQUEST, management_view='Configure', manage_tabs_message=manage_tabs_message)

    def getServerConfiguration(self):
        """return server ip an port of the configured fedora repository"""
        return (ADDRESS, PORT)        


    security.declareProtected(ManagePortal, 'manage_save_metadata')
    def manage_save_metadata(self, REQUEST):
        """Save default metadata as attributes of the fedora tool."""
        md = self.metadata
        for metadata in self.getQualifiedDCMetadata(PID=None).keys():
            metadata_form_dict = REQUEST.form.get(metadata, None)
            metadata_to_save = (('required',False), ('visible',False), ( 'default',''))
            for key, value in metadata_to_save:
                new_value = metadata_form_dict.get(key,value)
                old_value = self.metadata[metadata][key]
                if new_value != old_value:
                    md[metadata][key] = new_value
                    logger.info("Modified: %s: changed %s from %s  to %s" % (metadata, str(key), str(old_value), str(new_value)))
        self.metadata = md
        manage_tabs_message = "Saved Metadata"
        return self.manage_metadata_form(REQUEST, management_view='Metadata', manage_tabs_message=manage_tabs_message)
    
        
    def getFedoraArticles(self):
        """find all FedoraArticles in Plone and return a list of PIDs."""
        portal_url = getToolByName(self, 'portal_url')
        portal = portal_url.getPortalObject()
        PIDs = []
        results = portal.portal_catalog.searchResults(portal_type='FedoraArticle')
        for article in results:
            try:
                obj = article.getObject()
                PIDs.append(obj.PID)
            except:
                pass
        return PIDs
        
    def manage_search(self, field, comparison, value, REQUEST=None):
        """search the repository"""
        query = []
        
        for i in range(len(field)):
            if not field[i] == '0':
                query.append((field[i],comparison[i], value[i]))
        query = tuple(query)
        return self.search(query)
        
    def manage_deleteObjects(self, REQUEST, LogMessage, PIDs = []):
        """delete Objects in Fedora"""
        #manage_tabs_message = "%d Objects deleted" % len(PIDs)
        deleted = 0
        skipped = 0
        for PID in PIDs:
            try:
                self.purgeObject(PID, LogMessage)
                deleted += 1
            except:
                skipped += 1

        manage_tabs_message = "%d Objects total, %d deleted, %d skipped" % (len(PIDs), deleted, skipped)
        return self.manage_search_form(REQUEST, management_view='Configure', manage_tabs_message=manage_tabs_message)

    def manage_getContentContainer(self, PID):
        """ return the PIDs of the Fedoraopjects which contain the html, xml,...
        """
        cModel = ContentModel.ContentModel()
        response =cModel.getContentModel(PID)
        PIDs = (response._objectHTML,
            response._objectMultimedia,
            response._objectNative,
            response._objectOther,
            response._objectPDF,
            response._objectXML,
            response._objectSupplementary,
            response._objectOther)
        return PIDs


    def purgeObject(self, PID, LogMessage):
        """purge object
        """
        Force = False
        self.fedoramanagement.purgeObject(PID, LogMessage, Force)
        
    def manage_batchingest(self, file, target, dryrun=False, REQUEST=None):
        """batchingest of old issues"""
        portal_url = getToolByName(self, 'portal_url')
        journal = portal_url.getPortalObject()
        articles = import_backissues(self,REQUEST, file, journal, target, dryrun)
        REQUEST.set('articles',articles) 
        return articles
        
    def setURL(self, PID, identifierURL):
        """modify the URL in the qdc after moving in Plone
        """
        cModel = ContentModel.ContentModel()
        DCMetadata = cModel.getQualifiedDCMetadata(PID)
        DCMetadata._identifierURL = identifierURL
        cModel.setQualifiedDCMetadata(PID,DCMetadata)
        return DCMetadata
        
    def setModified(self, PID):
        """change the modify date after editing the article
           or any part of it
        """
        cModel = ContentModel.ContentModel()
        DCMetadata = cModel.getQualifiedDCMetadata(PID)
        today = DateTime().strftime("%Y-%m-%d")
        modified = mktime(strptime(today, "%Y-%m-%d"))
        DCMetadata._modified = modified
        cModel.setQualifiedDCMetadata(PID,DCMetadata)
        return DCMetadata

    def getDatastreams(self, PID):
        """
        """
        response = self.fedoramanagement.getDatastreams(PID)

        liste = []
        for i in range(len(response)):
            liste.append({'ID':response[i]._ID,
                          'label':response[i]._label,
                          'createDate':DateTime(response[i]._createDate),
                          'createDateTupel':response[i]._createDate,
                          'controlGroup':response[i]._controlGroup,
                          'state':response[i]._state,
                          'size':response[i]._size,
                          'MIMEType':response[i]._MIMEType})
        return liste


    def modifyObject(self, PID, State, Label, LogMessage):
        """change the state of an object
        """
        Label= None
        LogMessage = None
        self.fedoramanagement.modifyObject(PID, State, Label, LogMessage)


    def accessMultiMediaByFedoraURL(self, PID, DsID, Date):
        """alternative method to retrieve objects from the Fedora
        Repository. It uses the FedoraURL directly insteht the Wbservice
        via ZSI, which fails with larger Objects
        """

        parts = ['fedora','get']
        parts.append(PID)
        parts.append(DsID)
        if Date:
            parts.append(Date)

        path = '/'.join(parts)
        netloc = ':'.join((ADDRESS,PORT))
        conn = httplib.HTTPConnection(netloc)
        URL = urlparse.urlunparse(('http',netloc,path,'','',''))
        logger.info("fetch %s from repository" % URL)
        conn.request("GET", URL)
        r = conn.getresponse()
        data = {'MIMEType':r.getheader('content-type'),
                'stream':r.read()}
        return data
        
    def accessMultiMedia(self, PID, DsID, Date):
        """return the MIMEType and content of a datastream
        """
        if Date:
            Date = eval(Date) 
        response = self.fedoraaccess.getDissemination(PID, DsID, Date)
        
        data = {'MIMEType':response._MIMEType,
                'stream':response._stream}
        return data
        
    def accessByFedoraURL(self, PID, DsID, Date):
        """alternative method to retrieve objects from the Fedora
        Repository. It uses the FedoraURL directly insteht the Wbservice
        via ZSI, which fails with larger Objects
        """
        parts = ['fedora','get']
        parts.append(PID)
        parts.append(DsID)
        if Date:
            parts.append(Date)

        path = '/'.join(parts)
        netloc = ':'.join((ADDRESS, PORT))
        conn = httplib.HTTPConnection(netloc)
        URL = urlparse.urlunparse(('http',netloc,path,'','',''))
        logger.debug(URL)
        conn.request("GET", URL)
        r = conn.getresponse()
        data = {'MIMEType':r.getheader('content-type'),
                'stream':r.read()}
        return data

    def access(self, PID, DsID, Date):
        """return the MIMEType and content of a datastream
        """

        response = self.fedoraaccess.getDissemination(PID, DsID, Date)
        
        liste = {'MIMEType':response._MIMEType,
                 'stream':response._stream}
        return liste

    def search(self, query):
        """ return a list with metadata of an object
        """
        response = self.fedoraaccess.findObject(query)
        liste = []
        if len(response) > 0:
            for i in range(len(response)):
                title    = response[i]._title[0].encode()
                try:
                    creator = response[i]._creator[0].encode()
                except:
                    creator = "n/a"
                    
                try:
                    relations = response[i]._relation
                    isChildOf = []
                    isParentOf = []
                    for relation in relations:
                        pair = relation.split()
                        if pair[0] == "isChildOf":
                            isChildOf.append(pair[1])
                        elif pair[0] == "isParentOf":
                            isParentOf.append(pair[1])
                        else:
                            pass
                        
                except:
                    isParentOf = "n/a"
                    isChildOf = "n/a"
                    
                liste.append({'PID':response[i]._pid,
                              'description':response[i]._description,
                              'cModel':response[i]._cModel,
                              'state':response[i]._state,
                              'publisher':response[i]._publisher,
                              'cDate':response[i]._cDate,
                              'title':title,
                              #'title':response[i]._pid.replace(':','_'),
                              'isParentOf':isParentOf,
                              'isChildOf':isChildOf,
                              'creator':creator})

        return liste

    def getContentModel(self, PID, Type):
        """ return the PID of a content object
        """
        cModel = ContentModel.ContentModel()
        response =cModel.getContentModel(PID)
        if Type == "HTML":
            return response._objectHTML
        elif Type == "Multimedia":
            return response._objectMultimedia
        elif Type == "Native":
            return response._objectNative
        elif Type == "Other":
            return response._objectOther
        elif Type == "PDF":
            return response._objectPDF
        elif Type == "XML":
            return response._objectXML
        elif Type == "Supplementary":
            return response._objectSupplementary
        else:
            return response._objectOther
    
    def modifyDatastreamByReference(self, REQUEST, PID, DsID, DsLabel, LogMessage, Location, DsState, MIMEType, tempID):
        self.fedoramanagement.modifyDatastreamByReference(PID, DsID, DsLabel, LogMessage, Location, DsState, MIMEType)
        return Location


    def makeDCMetadataObject(self, params):
        """return a Metadata object"""
        
        if params.has_key('PID'):
            PID = params['PID']
            cModel = ContentModel.ContentModel()
            DCMetadata = cModel.getQualifiedDCMetadata(PID)
        else:  
            DCMetadata = ContentModel.setQualifiedDublinCoreRequest().new_in1()

        # Titel   
        DCMetadata._title = []
        for i in range(len(params['title_value'])):
            x = DCMetadata.new_title()
            x._value =  params['title_value'][i]
            x._lang =  params['title_lang'][i]
            DCMetadata._title.append(x)

        # alternativer Titel
        DCMetadata._alternative = []
        for alternative in params['alternative']:
            x = DCMetadata.new_alternative()
            x._value =  alternative['value']
            x._lang  =  alternative['lang']
            DCMetadata._alternative.append(x)
        
        # abstract
        DCMetadata._DCTermsAbstract = []
        for abstract in params['DCTermsAbstract']:
            x = DCMetadata.new_DCTermsAbstract()
            x._value =  abstract['value']
            x._lang  =  abstract['lang']
            DCMetadata._DCTermsAbstract.append(x)

        # creatorPerson
        DCMetadata._creatorPerson = []
        for author in params['creatorPerson']:
            x = DCMetadata.new_creatorPerson()
            x._PNDIdentNumber      = author.get('PNDIdentNumber','')
            x._academicTitle       = author.get('academicTitle','')
            x._emailAddress        = author.get('emailAddress','')
            x._firstName           = author.get('firstName','')
            x._lastName            = author.get('lastName','')
            x._organization        = author.get('organization','')
            x._postalAddress       = author.get('postalAddress','')
            DCMetadata._creatorPerson.append(x)

        # creatorCorporated
        DCMetadata._creatorCorporated = []
        for corp in params['creatorCorporated']:
            x = DCMetadata.new_creatorCorporated()
            x._GKDIdentNumber      = corp['GKDIdentNumber']
            x._emailAddress        = corp['emailAddress']
            x._institutionelAuthor = corp['institutionelAuthor']
            x._organization        = corp['organization']
            x._postalAddress       = corp['postalAddress']
            DCMetadata._creatorCorporated.append(x)

        # contributor
        DCMetadata._contributor = []
        for contrib in params['contributor']:
            x = DCMetadata.new_contributor()
            x._PNDIdentNumber      = contrib['PNDIdentNumber']
            x._academicTitle       = contrib['academicTitle']
            x._emailAddress        = contrib['emailAddress']
            x._firstName           = contrib['firstName']
            x._lastName            = contrib['lastName']
            x._organization        = contrib['organization']
            x._postalAddress       = contrib['postalAddress']
            x._role                = contrib['role']
            DCMetadata._contributor.append(x)

        # DDC Sachgruppen
        DCMetadata._DDC = []
        DDCs = params['DDC']
        for DDC in DDCs:
            DCMetadata._DDC.append(DDC)

        #subject
        subject = []
        try:
            subjects = params['subject']
            for aSubject in subjects:
                if aSubject != "":
                    subject.append(aSubject)
        except:
            pass 
        DCMetadata._subject=subject

        #subjectClassified
        DCMetadata._subjectClassified = []
        for subjectClassified in params['subjectClassified']:
            x = DCMetadata.new_subjectClassified()
            x._classificationIdent = subjectClassified.get('classificationIdent','')
            x._classificationSystem = subjectClassified.get('classificationSystem','')
            x._subjectClassified = subjectClassified.get('subjectClassified','')
            DCMetadata._subjectClassified.append(x)
        
     
        #language
        DCMetadata._language = []
        try:
            languages = params['language']
            for language in languages:
                DCMetadata._language.append(language)
        except:
            DCMetadata._language.append("")
        
        #publisher
        try:
            publishers = params['publisher']
            DCMetadata._publisher = []
            for publisher in publishers:
                DCMetadata._publisher.append(publisher)
        except:
            pass

        try:
            created = params['created']
            DCMetadata._created = []
            x = mktime(strptime(created, "%Y-%m-%d"))
            DCMetadata._created = x
            
            modified = params['modified']
            DCMetadata._modified = []
            x = mktime(strptime(modified, "%Y-%m-%d"))
            DCMetadata._modified = x
            
            valid = params['valid']
            DCMetadata._valid = []
            x = mktime(strptime(valid, "%Y-%m-%d"))
            DCMetadata._valid = x
        except:
            pass
        
        # Dates of Publishinghistory
        
        dateSubmitted = params.get('dateSubmitted','').strip()
        if dateSubmitted != "":
            try:
                DCMetadata._dateSubmitted = mktime(strptime(dateSubmitted, "%Y-%m-%d"))
            except:
                pass
                
        dateAccepted = params.get('dateAccepted','').strip()
        if dateAccepted != "":
            try:
                DCMetadata._dateAccepted = mktime(strptime(dateAccepted, "%Y-%m-%d"))
            except:
                pass
        
        dateCopyrighted = params.get('dateCopyrighted','').strip()
        if dateCopyrighted != "":
            try:
                DCMetadata._dateCopyrighted = mktime(strptime(dateCopyrighted, "%Y-%m-%d"))
            except:
                pass

        #bibliographicCitation
        DCMetadata._bibliographicCitation = []
        bc = params['bibliographicCitation'][0]
        x = DCMetadata.new_bibliographicCitation()
        x._journalIssueDate = bc['journalIssueDate']
        x._journalIssueNumber = bc['journalIssueNumber']
        x._journalTitle = bc['journalTitle'] 
        x._journalVolume = bc['journalVolume']
        DCMetadata._bibliographicCitation.append(x)
     
        #rights
        DCMetadata._rights=[]
        try:
            rights = params['rights']
            for x in rights:
                DCMetadata._rights.append(x)
                
        except:
            pass
        
        #ISSN
        try:
            DCMetadata._identifierISSN = params['identifierISSN']
        except:
            pass
        #URL
        try:
            DCMetadata._identifierURL = params['identifierURL']
        except:
            pass

        #DOI
        try:
            DCMetadata._identifierDOI = params['identifierDOI']
        except:
            pass

        #pubType
        try:
            DCMetadata._pubType = []
            pubType = params['pubType'][0]
            DCMetadata._pubType.append(pubType)
        except:
            pass

        #docType
        try:
            DCMetadata._docType =[]
            docType = params['docType'][0]
            DCMetadata._docType.append(docType)
        except:
            pass

        #articleType
        DCMetadata._articleType = []
        try:
            articleType = params['articleType']
            DCMetadata._articleType.append(articleType)
        except:
            pass
        
        return DCMetadata


    def getQualifiedDCMetadata(self,PID):
        if PID != None:
            cModel = ContentModel.ContentModel()
            response =cModel.getQualifiedDCMetadata(PID)

            creatorPerson = []
            if len(response._creatorPerson) != 0:
                for ACreatorPerson in response._creatorPerson:
                    creatorPerson.append({
                        'GKDIdentNumber':ACreatorPerson._GKDIdentNumber,
                        'PNDIdentNumber':ACreatorPerson._PNDIdentNumber,
                        'academicTitle':ACreatorPerson._academicTitle,
                        'emailAddress':ACreatorPerson._emailAddress,
                        'firstName':ACreatorPerson._firstName,
                        'institutionelAuthor':ACreatorPerson._institutionelAuthor,
                        'lastName':ACreatorPerson._lastName,
                        'organization':ACreatorPerson._organization,
                        'postalAddress':ACreatorPerson._postalAddress,
                        'role':ACreatorPerson._role
                    })
            else:
                creatorPerson.append({
                    'GKDIdentNumber':'',
                    'PNDIdentNumber':'',
                    'academicTitle':'',
                    'emailAddress':'',
                    'firstName':'',
                    'institutionelAuthor':'',
                    'lastName':'',
                    'organization':'',
                    'postalAddress':'',
                    'role':''
                })

            creatorCorporated = []
            if len(response._creatorCorporated) != 0:
                for ACreatorCorporated in response._creatorCorporated:
                    creatorCorporated.append({
                        'GKDIdentNumber':ACreatorCorporated._GKDIdentNumber,
                        'emailAddress':ACreatorCorporated._emailAddress,
                        'institutionelAuthor':ACreatorCorporated._institutionelAuthor,
                        'organization':ACreatorCorporated._organization,
                        'postalAddress':ACreatorCorporated._postalAddress
                    })
            else:
                creatorCorporated.append({
                    'GKDIdentNumber':'',
                    'emailAddress':'',
                    'institutionelAuthor':'',
                    'organization':'',
                    'postalAddress':''
                })

            contributor = []
            if len(response._contributor) != 0:
                for aContributor in response._contributor:
                    contributor.append({
                        'GKDIdentNumber':aContributor._GKDIdentNumber,
                        'PNDIdentNumber':aContributor._PNDIdentNumber,
                        'academicTitle':aContributor._academicTitle,
                        'emailAddress':aContributor._emailAddress,
                        'firstName':aContributor._firstName,
                        'institutionelAuthor':aContributor._institutionelAuthor,
                        'lastName':aContributor._lastName,
                        'organization':aContributor._organization,
                        'postalAddress':aContributor._postalAddress,
                        'role':aContributor._role
                    })
            else:
                contributor.append({
                    'GKDIdentNumber':'',
                    'PNDIdentNumber':'',
                    'academicTitle':'',
                    'emailAddress':'',
                    'firstName':'',
                    'institutionelAuthor':'',
                    'lastName':'',
                    'organization':'',
                    'postalAddress':'',
                    'role':''
                })

            title=[]
            if len(response._title) != 0:
                for aTitle in response._title:
                    title.append({'lang':aTitle._lang,'value':aTitle._value})
            else:
                title.append({'lang':'','value':''})
                

            alternative = []
            if len(response._alternative) > 0:
                for aAlternative in response._alternative:
                    alternative.append({
                        'lang':aAlternative._lang,
                        'value':aAlternative._value
                    })
            else:
                alternative.append({
                    'lang':'',
                    'value':''
                })

            DCTermsAbstract=[]
            if len(response._DCTermsAbstract)!=0:
                for x in response._DCTermsAbstract:
                    DCTermsAbstract.append({'lang':x._lang,'value':x._value})
            else:
                DCTermsAbstract.append({'lang':'','value':''})
                
            
            DDC = []
            if response._DDC != None and len(response._DDC) > 0:
                for aDDC in response._DDC:
                    DDC.append(aDDC)
            else:
                DDC.append('')

            identifierISSN = response._identifierISSN
            identifierURL = response._identifierURL
            identifierURN = response._identifierURN
            identifierDOI = response._identifierDOI

            language = []
            if response._language != None:
                for aLanguage in response._language:
                    language.append(aLanguage)
            else:
                language.append('')

            publisher = []
            if response._publisher != None:
                for aPublisher in response._publisher:
                    publisher.append(aPublisher)
            else:
                publisher.append('')

            pubType = []
            if response._pubType != None:
                for aPubType in response._pubType:
                    pubType.append(aPubType)
            else:
                pubType.append('')

            docType = []
            if response._docType != None:
                for aDocType in response._docType:
                    docType.append(aDocType)
            else:
                docType.append('')
            
            subject = []
            if response._subject != None:
                for aSubject in response._subject:
                    #subject += aSubject + "\n"
                    subject.append(aSubject)
            else:
                pass #subject.append('')

            subjectClassified = []
            if len(response._subjectClassified)!=0:
                for aSubjectClassified in response._subjectClassified:
                    subjectClassified.append({
                        'classificationIdent':aSubjectClassified._classificationIdent,
                        'classificationSystem':aSubjectClassified._classificationSystem,
                        'subjectClassified':aSubjectClassified._subjectClassified
                    })
            else:
                subjectClassified.append({
                    'classificationIdent':'',
                    'classificationSystem':'',
                    'subjectClassified':''
                })

            try:
                # date ist stored as tuple given by mktime
                # not sure why it is like that. Only date, not time ist saved
                created = strftime("%Y-%m-%d",response._created[0:6] + (0,1,-1))
                modified = strftime("%Y-%m-%d",response._modified[0:6] + (0,1,-1))
                valid = strftime("%Y-%m-%d",response._valid[0:6] + (0,1,-1))
            except:
                created = None
                modified = None
                valid = None
            
            try:
                dateSubmitted =  strftime("%Y-%m-%d",response._dateSubmitted[0:6] + (0,1,-1))
                dateCopyrighted =  strftime("%Y-%m-%d",response._dateCopyrighted[0:6] + (0,1,-1))
                dateAccepted=  strftime("%Y-%m-%d",response._dateAccepted[0:6] + (0,1,-1))
            except:
                dateSubmitted = None
                dateCopyrighted = None
                dateAccepted = None

            bibliographicCitation = []
            try:
                bibliographicCitation.append({
                    'journalIssueDate':   response._bibliographicCitation[0]._journalIssueDate,
                    'journalIssueNumber': response._bibliographicCitation[0]._journalIssueNumber,
                    'journalTitle':       response._bibliographicCitation[0]._journalTitle,
                    'journalVolume':      response._bibliographicCitation[0]._journalVolume
                })
            except:
                bibliographicCitation.append({
                    'journalIssueDate':'',
                    'journalIssueNumber':'',
                    'journalTitle':'',
                    'journalVolume':''
                })
            
            rights = []
            if response._rights != None:
                for right in response._rights:
                    rights.append(right)
            else:
                rights.append('')

        else:
            DDC = []
            DDC.append('')
            identifierISSN = ""
            identifierURL = ""
            identifierURN = ""
            identifierDOI = ""
            language = []
            language.append('')
            title = []
            title.append({'lang':'','value':''})
            alternative = []
            alternative.append({'lang':'','value':''})
            DCTermsAbstract = []
            DCTermsAbstract.append({'lang':'','value':''})
            creatorPerson = []
            creatorPerson.append({
                'GKDIdentNumber':'',
                'PNDIdentNumber':'',
                'academicTitle':'',
                'emailAddress':'',
                'firstName':'',
                'institutionelAuthor':'',
                'lastName':'',
                'organization':'',
                'postalAddress':'',
                'role':''
            })
            creatorCorporated = []
            creatorCorporated.append({
                'GKDIdentNumber':'',
                'emailAddress':'',
                'institutionelAuthor':'',
                'organization':'',
                'postalAddress':''
            })
            contributor = []
            contributor.append({
                'GKDIdentNumber':'',
                'PNDIdentNumber':'',
                'academicTitle':'',
                'emailAddress':'',
                'firstName':'',
                'institutionelAuthor':'',
                'lastName':'',
                'organization':'',
                'postalAddress':'',
                'role':''
            })
            subject = ''
            subjectClassified = []
            subjectClassified.append({
                'classificationIdent':'',
                'classificationSystem':'',
                'subjectClassified':''
            })
            dateSubmitted = ""
            dateCopyrighted = ""
            dateAccepted = ""
            created = ""
            modified = ""
            valid = ""
            pubType = []
            pubType.append('')
            docType = []
            docType.append('')
            publisher =[]
            publisher.append('')
            bibliographicCitation = []
            bibliographicCitation.append({
                'journalIssueDate':'',
                'journalIssueNumber':'',
                'journalTitle':'',
                'journalVolume':''
            })
            rights = []
            rights.append('')

        qdc = {
            'DDC':DDC,
            'identifierISSN':identifierISSN,
            'identifierURL':identifierURL,
            'identifierURN':identifierURN,
            'identifierDOI':identifierDOI,
            'language':language,
            'title':title,
            'alternative':alternative,
            'DCTermsAbstract':DCTermsAbstract,
            'creatorPerson':creatorPerson,
            'creatorCorporated':creatorCorporated,
            'contributor':contributor,
            'subject':subject,
            'subjectClassified':subjectClassified,
            'dateSubmitted':dateSubmitted,
            'dateCopyrighted':dateCopyrighted,
            'dateAccepted':dateAccepted,
            'created':created,
            'modified':modified,
            'valid':valid,
            'pubType':pubType,
            'docType':docType,
            'publisher':publisher,
            'bibliographicCitation':bibliographicCitation,
            'rights':rights
        }
        return qdc

    def setQualifiedDCMetadata(self, params):
        """ set the qualified Dublin Core Metadata of an object"""
        
        cModel = ContentModel.ContentModel()
        DCMetadata = ContentModel.setQualifiedDublinCoreRequest().new_in1()
        PID = params['PID']
        DCMetadata = self.makeDCMetadataObject(params)
        cModel.setQualifiedDCMetadata(PID,DCMetadata)
        return DCMetadata

    def createNewArticle(self, ContainerPID, JournalPID, params, Location):
        """creates a new article object for DiPP"""
    
        cModel = ContentModel.ContentModel()
        today = DateTime().strftime("%Y-%m-%d")
        params['created'] = today
        params['modified'] = today
        params['valid'] = today
        DCMetadata = self.makeDCMetadataObject(params)
        ContainerPIDs = []
        ContainerPIDs.append(ContainerPID)
        StorageType  = params['storageType']
        #Location = Location + "/getPrivateContent"
        if params['targetFormat'] == ['']:
            targetFormat = []
        else:
            targetFormat = params['targetFormat']
        
        response = cModel.createNewArticle(ContainerPIDs, JournalPID, DCMetadata, Location, StorageType, targetFormat)
        return response
    
    def createNewEntry(self, ContainerPID, JournalPID, params, Location):
        """creates a new entry object for DiPA"""
    
        cModel = ContentModel.ContentModel()
        DCMetadata = self.makeDCMetadataObject(params)
        ContainerPIDs = []
        ContainerPIDs.append(ContainerPID)
        StorageType  = "permanent"
        targetFormat = []
        response = cModel.createNewArticle(ContainerPIDs, JournalPID, DCMetadata, Location, StorageType, targetFormat)
        return response

    def setPublishingState(self, PID, State, Published):
        """change the state of a digital object in fedora"""

        cModel = ContentModel.ContentModel()
        State     = State
        Published = Published
        cModel.setPublishingState(PID, State, Published)
        msg = 'PID: %s/ State: %d/ Published: %d' % (PID, State, Published)
        logger.info(msg)

    
    def createNewContainer(self, JournalPID, MetaType, Title, ChunkURL, AbsoluteURL):
        cModel = ContentModel.ContentModel()
        response = cModel.createNewContainer(JournalPID, MetaType, Title, ChunkURL, AbsoluteURL)
        return response

    def moveObject(self,moveObjectPID, sourceObjectPID, destObjectPID):
        cModel = ContentModel.ContentModel()
        cModel.moveObject(moveObjectPID, sourceObjectPID, destObjectPID)
        msg  = "Object %s moved from %s to %s" % (moveObjectPID, sourceObjectPID, destObjectPID)
        logger.info(msg)

    
    def moveObjects(self,clipboard,dest):
        """
        when moving objects in the folder_contents view of plone
        keep it in sync with fedora
        """
        cModel = ContentModel.ContentModel()
        raw = loads(decompress(unquote(clipboard)))[1]
        for x in raw:
            try:
                url = '/'.join(x)
                obj = self.restrictedTraverse(url)
                aMoveObjectPID = obj.PID
                aSourceObjectPID = obj.getParentNode().PID
                aDestObjectPID = dest
                cModel.moveObject(aMoveObjectPID, aSourceObjectPID, aDestObjectPID)
                msg  = "Object " +  aMoveObjectPID
                msg += " moved from " + aSourceObjectPID
                msg += " to " + aDestObjectPID
                logger.info(msg)
            except:
                pass
    
    def addDatastream(self,REQUEST,PID,Label,MIMEType,Location,ControlGroup,MDClass,MDType,DsState):
        DSID =  self.fedoramanagement.addDatastream(PID,Label,MIMEType,Location,ControlGroup,MDClass,MDType,DsState)
        logger.info("added Datastrem %s to object %s" % (DSID, PID))
        return DSID
    
    def getDatastreamHistory(self,PID,DsID):
        response = self.fedoramanagement.getDatastreamHistory(PID, DsID)
        liste = []
        for i in range(len(response)):
            params  = "PID=" + PID
            params += "&DsID=" + DsID
            #params += "&Date=" + strftime("%Y-%m-%d %H:%M",response[i]._createDate)
            params += "&Date=" + str(response[i]._createDate)
            liste.append({'ID':response[i]._ID,
                          'versionID':response[i]._versionID,
                          'label':response[i]._label,
                          'state':response[i]._state,
                          #'createDate':DateTime(response[i]._createDate),
                          'createDate':response[i]._createDate,
                          'params':params,
                          'MIMEType':response[i]._MIMEType})
        
        return liste

    def getopenurl(self,qdc,journalname_abbr,issn):
        """return the metadata as openurl to use for COinS"""
        creators = qdc['creatorPerson']
        authors = ()
        for creator in creators:
            authors += ((creator['lastName'], creator['firstName']),)
        titles = qdc['title']
        bibliographicCitation = qdc['bibliographicCitation'][0]
        x = openurl.OpenURL()
        x.atitle = titles[0]['value']
        x.jtitle = bibliographicCitation['journalTitle']
        x.stitle = journalname_abbr
        x.volume = bibliographicCitation['journalVolume']
        x.issue = bibliographicCitation['journalIssueNumber']
        x.date = bibliographicCitation['journalIssueDate']
        x.authors = authors
        x.urn = qdc['identifierURN']
        x.doi = qdc['identifierDOI']
        x.url = qdc['identifierURL']
        x.issn = issn
        return x.geturl()

    def getTempID(self,REQUEST):
        '''temporary ID for intermediate saving of new datastreams'''
        id = str(REQUEST.AUTHENTICATED_USER) + str(DateTime().timeTime())
        return id
            
    def pwd(self, cookie):
        raw = loads(decompress(unquote(cookie)))[1]
        return raw



    def dumpClipboard(self, REQUEST):

        cp = REQUEST['__cp']
        raw = loads(decompress(unquote(cp)))[1]
        urls = []
        for url in raw:
            urls.append('/'.join(url))
        return raw 
        
    def lazyIndex(self, pid, fedora, obj):
        params = []
        params.append(pid)
        params.append(fedora)
        params.append(obj)
        t = Timer(10.0, self.index, params)
        t.start() 

    def index (self, Supplementary_PID, fedora, obj):
        
        for datastream in self.fedora.getDatastreams(PID=Supplementary_PID):
            if datastream['ID'][0:2] == 'DS':
                DsID = datastream['ID']
                id = datastream['label']
                title = datastream['label']
                if datastream['MIMEType'] in ['text/html']:
                    obj.invokeFactory('FedoraDocument',id=id,title=title,PID=Supplementary_PID,DsID=DsID,body=fedora.access(PID=Supplementary_PID,DsID=DsID,Date=None)['stream'])

    def getLanguages(self):
        """return a dictionary with languages codes"""
        return LANGUAGES

    def diffDatastreamVersions(self, PID, DsID, version1date, version2date):
        """return the difference between two versions of a datastream"""
        
        source1 = self.accessByFedoraURL(PID, DsID, version1date)["stream"]
        source2 = self.accessByFedoraURL(PID, DsID, version2date)["stream"]
        return htmldiff(source1,source2)
