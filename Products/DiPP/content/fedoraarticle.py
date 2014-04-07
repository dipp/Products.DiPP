# -*- coding: utf-8 -*-
# The FedoraArticle ContentType
#
# German Free Software License (D-FSL)
#
# This Program may be used by anyone in accordance with the terms of the
# German Free Software License
# The License may be obtained under <http://www.d-fsl.org>.
#
# $Id$

import logging
from DateTime import DateTime
from textindexng.interfaces import IIndexableContent
from textindexng.content import IndexContentCollector as ICC
from zope.interface import implements, Interface
from AccessControl import ClassSecurityInfo

from Products.CMFCore.utils import getToolByName
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

try:
    from Products.LinguaPlone.public import *
    from Products.LinguaPlone import utils
except ImportError:
    from Products.Archetypes.public import *

try:
    from Products.CMFCore.permissions import ManagePortal, ManageProperties
    from Products.CMFCore.permissions import View
except ImportError:
    from Products.CMFCore.CMFCorePermissions import ManagePortal, ManageProperties
    from Products.CMFCore.CMFCorePermissions import View

from Products.DiPP.config import PROJECTNAME, COMMENT_SELECTION_TITLE_LENGTH, PDFA_PREFIX
from Products.DiPP.interfaces import IFedoraArticle
from Products.DiPP import Permissions

logger = logging.getLogger(__name__)

def dummy(obj, event):
    logger.info("edit event. not used yet")
        
FedoraArticleSchema = BaseSchema + Schema((
        StringField('PID',
                required=0,
                widget=StringWidget(
                    label='PID',
                    description='Persistent Identifier',
                    size='15',
                    visible={'edit':'invisible','view':'visible'}
                    ),
        ),
        TextField('abstract',
                widget=TextAreaWidget(
                    label='Abstract',
                    visible={'edit':'invisible','view':'invisible'}
                    ),
                searchable=True
        ),
        StringField('article_type',
                required=0,
                widget=StringWidget(
                    label='Textsorte',
                    description='Welche Textsorte läßt sich der Artikel zuordnen?'),
        ),
        StringField('pixel_domain',
                required=0,
                widget=StringWidget(
                    label='VG Kürzel',
                    description='Domain auf dem Zählserver: vgXX.met.vgwort.de, z.B. vg06',
                    size='4'),
                schemata="Metis"
        ),
        StringField('pixel_id',
                required=0,
                widget=StringWidget(
                    label='VGWort Public ID',
                    description='Der öffentliche Identifikationscode des Zählpixels',
                    size='40'),
                schemata="Metis"
        ),
        IntegerField('position',
            widget=IntegerWidget(label="The Postion of the article in a special issue."),
            storage=AttributeStorage(),
            default=0,
            required=1,
        ),
        StringField(
            name='comment_to',
            i18n_domain='dipp',
            widget=SelectionWidget(
                label='The commented article',
                label_msgid='label_comment_to_field',
                description='If this Article was submitted as a comment to an existing publication you can select it here to create a connection between the two.',
                description_msgid='help_comment_to_field',
            ),
            searchable=1,
            multiValued=0,
            vocabulary="getPublishedArticles"
        ),
        StringField('journal_section',
            widget=SelectionWidget(
                required=1,
                label='Section',
                description='Welcher Sektion läßt sich der Artikel zuordnen?'
            ),
            vocabulary=NamedVocabulary("journal-sections"),
            default='no-section',
            searchable=1,
            schemata='Bibliographic Data'
        ),
        StringField('subject_areas',
            widget=MultiSelectionWidget(
                required=0,
                label='Subject areas',
                description='Select one ore more appropiate subject areas.'
            ),
            vocabulary=NamedVocabulary("subject-areas"),
            searchable=1,
            schemata='Bibliographic Data'
        ),
        StringField('JournalTitle',
            required=0,
            widget=StringWidget(
                label='Journal title',
                label_msgid='label_journaltitle_field',
                description='The titel of this Journal.',
                description_msgid='help_journaltitle_field',
                visible={'edit':'invisible','view':'visible'}
            ),
            schemata='Bibliographic Data'
        ),
        StringField('Volume',
            required=0,
            widget=StringWidget(
                label='Volume',
                label_msgid='label_volume_field',
                description='An Volume to hold the Issues.',
                description_msgid='help_volume_field',
                visible={'edit':'invisible','view':'visible'}
            ),
            schemata='Bibliographic Data'
        ),
        StringField('URN',
            required=0,
            widget=StringWidget(
                label='URN',
                label_msgid='label_urn_field',
                description='The Uniform Resource Name of this article',
                description_msgid='help_urn_field',
                visible={'edit':'invisible','view':'visible'}
            ),
            schemata='Bibliographic Data'
        ),
        StringField('DOI',
            required=0,
            widget=StringWidget(
                label='DOI',
                label_msgid='label_doi_field',
                description='The Digital Object Identifier of this article',
                description_msgid='help_doi_field',
                visible={'edit':'invisible','view':'visible'}
            ),
            schemata='Bibliographic Data'
        ),
        StringField('Issue',
            required=0,
            widget=StringWidget(
                label='Issue',
                label_msgid='label_issue_field',
                description='An Issue to hold the Articles. Usally part of a volume',
                description_msgid='help_issue_field',
                visible={'edit':'invisible','view':'visible'}
            ),
            schemata='Bibliographic Data'
        ),
        DateTimeField('IssueDate',
            required=0,
            widget=CalendarWidget(
                label='Date',
                label_msgid='label_issuedate_field',
                description='The Date on which this issue is published.',
                description_msgid='help_issuedate_field',
                visible={'edit':'invisible','view':'visible'}
            ),
            schemata='Bibliographic Data'
        ),
        IntegerField('startpage',
            required=0,
            widget=StringWidget(
                label='First page',
                label_msgid='label_startpage_field',
                description='The first page of the article.',
                description_msgid='help_startpage_field',
                visible={'edit':'visible','view':'visible'}
            ),
            schemata='Bibliographic Data'
        ), 
        IntegerField('endpage',
            required=0,
            widget=StringWidget(
                label='Last page',
                label_msgid='label_endpage_field',
                description='The last page of the article.',
                description_msgid='help_endpage_field',
                visible={'edit':'visible','view':'visible'}
            ),
            schemata='Bibliographic Data'
        ), 
        LinesField('AvailableAbstracts',
            required=0,
            widget=LinesWidget(
                label='Available Abstracts',
                label_msgid='label_issue_field',
                description='Languages, in which abstracts are available',
                description_msgid='help_issue_field',
                visible={'edit':'invisible','view':'visible'}
            ),
            schemata='Bibliographic Data'
        ),
        LinesField('Authors',
            required=0,
            widget=LinesWidget(
                label='Authors',
                label_msgid='label_author_field',
                description='Authors of this article, one per line.-',
                description_msgid='help_author_field',
                visible={'edit':'invisible','view':'visible'}
            ),
            schemata='Bibliographic Data'
        ),
    ))


class FedoraArticle(BrowserDefaultMixin, OrderedBaseFolder):
    """Folderish Content Object containing all parts of an scholarly article.
    
    An article, which has gone through a peer review. Has to be added through the
    :ref:`editorial toolbox <editorial_toolbox>`
    
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BrowserDefaultMixin,'__implements__',()),) + (getattr(OrderedBaseFolder,'__implements__',()),)
    implements(IIndexableContent, IFedoraArticle)
    
    schema = FedoraArticleSchema
    
    security.declareProtected(ManagePortal, 'manage_fedora_form')
    manage_fedora_form = PageTemplateFile('../www/fedora_form.pt', globals())
    
    manage_options = OrderedBaseFolder.manage_options[0:1] + ({'label':'Fedora',
                       'action':'manage_fedora_form',
                       'help':('DiPP', 'fedora.stx')},
        ) + OrderedBaseFolder.manage_options[2:]

   
    def indexableContent(self, fields):
        """Get the binary datastream from fedora and return in to TextIndexNG.
        
        Only pdf Files should be indexed (via pdftotext) mimetype is checked in plone
        to keep the burdon of fedora when reindexing the portal_catalog.
        
        """
        icc = ICC()
        fedora = getToolByName(self, 'fedora')
        PID = self.PID
        authors = ", ".join(self.getAuthors())
        title = self.Title()
        searchable = authors + title
        language = self.language
        # indexing authors
        logger.info("fetching %s for indexing (%s)" % (PID, language))
        icc.addContent('SearchableText',unicode(searchable), language)
        icc.addContent('Title',unicode(title), language)
        # indexing pdf
        PDF_PID = self.getFulltextPdf().get('PID',None)
        PDF_DsID = self.getFulltextPdf().get('DsID', None)
        MIMEType = "application/pdf" 
        if PDF_PID and PDF_DsID: 
            data =  fedora.accessMultiMediaByFedoraURL(PDF_PID,PDF_DsID,None)
            stream = data['stream']
            logger.info("PDF with %s/%s" % (PDF_PID, PDF_DsID))
            icc.addBinary('SearchableText', 
                          stream,
                          MIMEType,
                          'iso-8859-15',
                          language)
        return icc

    security.declareProtected(Permissions.EDIT_CONTENTS_PERMISSION, 'syncMetadata')
    def syncMetadata(self):
        """Sync the Metadata stored in Plone and Fedora.
        
        Most Metadata are kept only in Fedora but some are also stored in Plones
        catalog in order to have tkhem available in searches. This method should
        be called each time the metadata are modified
        
        """
        fedora = getToolByName(self, 'fedora')
        qdc = fedora.getQualifiedDCMetadata(self.PID)
        logger.info("Synchronizing Metadata of article %s at %s" % (self.PID, self.absolute_url() ))
        
        creatorPersons = qdc['creatorPerson']
        contributors = []
        for creatorPerson in creatorPersons:
            firstName = creatorPerson['firstName'] 
            lastName = creatorPerson['lastName'] 
            author = "%s, %s" % (lastName, firstName)
            contributors.append(author)
        self.setContributors(contributors)
        self.setAuthors(contributors)
        
        self.setSubject(qdc['subject'])
        self.setRights(qdc['rights'][0])
        self.setIssue(qdc['bibliographicCitation'][0]['journalIssueNumber'])
        self.setVolume(qdc['bibliographicCitation'][0]['journalVolume'])
        self.setJournalTitle(qdc['bibliographicCitation'][0]['journalTitle'])
        date = qdc['bibliographicCitation'][0]['journalIssueDate']
        self.setEffectiveDate(date)
        self.setIssueDate(date)
        self.setURN(qdc['identifierURN'])
        self.setDOI(qdc['identifierDOI'])
       
        # list with available abstract languages ist stored on article object. The calculation
        # on the fly would be to expensive, since for issue pages each single Article would
        # have to be fetched from fedora. Bad for the performance
        available_abstracts = []
        for abstract in qdc['DCTermsAbstract']:
            if abstract['value'].strip() != '':
                available_abstracts.append(abstract['lang'])
        self.setAvailableAbstracts(available_abstracts)
        self.setAbstract(qdc['DCTermsAbstract'][0]['value'].strip())
            
        self.reindexObject()
    
    def getPublishedArticles(self):
        """Return a tuple of published articles
        
        The catalog is searched for all FedoraArticles except the temporary ones.
        A List of PID, title tupels is returned.
        
        """ 
        results = self.portal_catalog.searchResults(Type='Fedora Article', sort_on='getPID', sort_order="reverse")
        articles = (('','None'),)
        words = COMMENT_SELECTION_TITLE_LENGTH
        
        for result in results:
            try:
                PID = result.getPID
                title = result.Title
            except:
                logger.info("articles should have Title and PID. We should never see this...")
                continue
            
            chopped_title = title.split()
            if len(chopped_title) > words:
                title = " ".join(chopped_title[0:words]) + "..."
            
            if not PID.startswith('temp') and not PID == self.PID:
                articles += ((PID,"%s | %s" % (PID, title)),)
            pass
        
        return articles



    def getFulltextPdfs(self):
        """Return the URL, PID and DsID  of the articles fulltext pdf
         
        The first listed pdf file which is declared al alternative format is taken. 
        if not found, return none. If Metis data are given, the according link is generated
        this is used by the document action for the pdf icon.
        
        """
        path = '/'.join(self.getPhysicalPath())
        pixel_domain =self.pixel_domain
        pixel_id = self.pixel_id
        result = self.portal_catalog(Type='Fedora Multimedia', path=path, getMMType='alternative_format', sort_on='getObjPositionInParent')
        
        pdfs = {}
        fulltext = None
        for pos, item in enumerate(result):
            obj = item.getObject()
            mimetype = obj.get_content_type()
            id = obj.getId()
            if mimetype in ('application/pdf', 'application/octet-stream'):
                if id.startswith(PDFA_PREFIX):
                    base_id = id[len(PDFA_PREFIX):]
                    type = 'pdfa'
                else:
                    base_id = id
                    type = 'pdf'
                    if not fulltext:
                        fulltext = id
                    

                size = self.getObjSize(obj)
                directURL = obj.absolute_url()
                state = item.review_state
                if pixel_domain and pixel_id:
                    url = "http://%s.met.vgwort.de/na/%s?l=%s" % (pixel_domain, pixel_id, directURL)
                else:
                    url = directURL
                    
                if not pdfs.has_key(base_id):
                    pdfs[base_id] = {'pdf':None,'pdfa':None}
                pdfs[base_id][type] = {'url':url, 'size':size, 'state':state}
        if fulltext:
            pdfs['fulltext'] = pdfs.pop(fulltext)     
        return pdfs

    def getFulltextPdf(self):
        """return the URL of the fulltext pdf or empty dictionary"""

        fulltext = self.getFulltextPdfs().get('fulltext',None)
        if fulltext:
            return fulltext['pdf']
        else:
            return {}
    
    def linkTranslations(self,PID):
        """not sure, if this is still in use"""
        articles = self.portal_catalog(Type='Fedora Article', getPID=PID)
        logger.info(PID)
        logger.info(len(articles))
        lang = self.Language()
        path = self.getPhysicalPath()
        todo = []
        translation = [(path,lang)]
        for article in articles:
            obj = article.getObject()
            lang = obj.Language()
            path = obj.getPhysicalPath()
            translation.append((path, lang))
            todo.append(translation)
        logger.info(todo)
        #utils.linkTranslations(self,todo)

        
    
registerType(FedoraArticle,PROJECTNAME)
