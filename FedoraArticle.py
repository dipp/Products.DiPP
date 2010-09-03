# -*- coding: utf-8 -*-
from Products.Archetypes.public import *
from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from config import PROJECTNAME
from AccessControl import ClassSecurityInfo
import Permissions
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from Products.CMFCore.utils import getToolByName
from zLOG import LOG, ERROR, INFO
try:
    from Products.CMFCore.permissions import ManagePortal
    from Products.CMFCore.permissions import View
except ImportError:
    from Products.CMFCore.CMFCorePermissions import ManagePortal
    from Products.CMFCore.CMFCorePermissions import View

class FedoraArticle(BrowserDefaultMixin, OrderedBaseFolder):
    """An article, which has gone through a peer review. Please add through the EDITORIAL TOOLBOX"""
    
    security = ClassSecurityInfo()
    __implements__ = (getattr(BrowserDefaultMixin,'__implements__',()),) + (getattr(OrderedBaseFolder,'__implements__',()),)

    manage_fedora_form = PageTemplateFile('www/fedora_form.pt', globals())
    security.declareProtected(ManagePortal, 'manage_fedora_form')

    manage_options = ({'label':'Fedora',
                       'action':'manage_fedora_form',
                       'help':('DiPP', 'fedora.stx')},
        ) + OrderedBaseFolder.manage_options

    schema = BaseSchema + Schema((
        StringField('PID',
                required=0,
                widget=StringWidget(
                    label='PID',
                    description='Persistent Identifier',
                    size='15',
                    visible={'edit':'invisible','view':'visible'}
                    ),
                index='FieldIndex:brains:schema'
        ),
        StringField('article_type',
                required=0,
                widget=StringWidget(
                    label='Textsorte',
                    description='Welche Textsorte läßt sich der Artikel zuordnen?'),
                index='FieldIndex:brains'
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
            index="FieldIndex:brains"
        ),
        StringField(
            name='comment_to',
            widget=SelectionWidget(
                label="Comment to",
                description="This Article is a comment to another article",
            ),
            searchable=1,
            index="FieldIndex:brains",
            multiValued=0,
            vocabulary="getPublishedArticles"
            #vocabulary=('as','asasd')
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
            index="FieldIndex:brains",
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
            index='FieldIndex:brains',
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
            index='FieldIndex:brains',
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
            index='FieldIndex:brains',
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
            index='FieldIndex:brains',
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
            index='FieldIndex:brains',
            schemata='Bibliographic Data'
        ),
    ))

    #archetype_name = "Peer reviewed article"
    archetype_description = "An article, which has gone through a peer review. Please add through the EDITORIAL TOOLBOX"
    allowed_content_types = ('FedoraDocument','FedoraMultimedia','FedoraXML')
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ('base_view', 'metadata_view', 'mixed_view', 'splash_screen')
    filter_content_types= 1
    content_icon = 'fedoraarticle_icon.gif'
    actions = (
          
        { "id": "view",
          "name": "View",
          "action": "string:${folder_url}/",
          "permissions": (Permissions.VIEW_CONTENTS_PERMISSION,),
          "category":"folder",
          },
        
        { "id": "qdc",
          "name": "Metadata",
          "action": "string:${folder_url}/fedoraarticle_metadata_form",
          "permissions": (Permissions.EDIT_CONTENTS_PERMISSION,),
          "category":"folder",
          },
          
        { "id": "citation",
          "name": "Citation and Metadata",
          "action": "string:${object_url}/metadata",
          "permissions": (Permissions.VIEW_CONTENTS_PERMISSION,),
          "category":"document_actions",
          },
        { "id": "fulltextpdf",
          "name": "Get the fulltext as pdf.",
          "action": "python:object.getFulltextPdf()",
          "condition": "python:object.getFulltextPdf()",
          "permissions": (Permissions.VIEW_CONTENTS_PERMISSION,),
          "category":"document_actions",
          },
    )
    
    security.declareProtected(Permissions.EDIT_CONTENTS_PERMISSION, 'syncMetadata')
    def syncMetadata(self):
        """keep Metadata of Plone and Fedora synchron"""
        fedora = getToolByName(self, 'fedora')
        if not self.PID.startswith('temp:'):
            qdc = fedora.getQualifiedDCMetadata(self.PID)
            LOG ('DIPP', INFO, "Synchronizing Metadata of article %s at %s" % (self.PID, self.absolute_url() ))
            
            creatorPersons = qdc['creatorPerson']
            contributors = []
            for creatorPerson in creatorPersons:
                firstName = creatorPerson['firstName'] 
                lastName = creatorPerson['lastName'] 
                author = "%s, %s" % (lastName, firstName)
                contributors.append(author)
            self.setContributors(contributors)
            
            self.setSubject(qdc['subject'])
            self.setRights(qdc['rights'][0])
            self.setIssue(qdc['bibliographicCitation'][0]['journalIssueNumber'])
            self.setVolume(qdc['bibliographicCitation'][0]['journalVolume'])
            self.setJournalTitle(qdc['bibliographicCitation'][0]['journalTitle'])
           
            # list with available abstract languages ist stored on article object. The calculation
            # on the fly would be to expensive, since for issue pages each single Article would
            # have to be fetched from fedora. Bad for the performance
            available_abstracts = []
            for abstract in qdc['DCTermsAbstract']:
                if abstract['value'].strip() != '':
                    available_abstracts.append(abstract['lang'])
            self.setAvailableAbstracts(available_abstracts)
        else:
            LOG ('DIPP', INFO, "Skipping synchronization of Metadata for temp. article %s at %s" % (self.PID, self.absolute_url() ))
            
        self.reindexObject()
    
    def getPublishedArticles(self):
        """build a Vocabulary with PIDs and Title of all FedoraArticles of the journal
           temporary articles are excluded""" 

        results = self.portal_catalog.searchResults(Type='Fedora Article')
        articles = (('','None'),)
        for result in results:
            try:
                PID = result.getPID
                title = result.Title
                if not PID.startswith('temp'):
                    articles += ((PID,title),)
            except:
                pass
        
        return articles


    def getFulltextPdf(self):
        """return the first listed pdf file which is declared als alternative format
        if not found, return none. this is used by the document action for the pdf icon
        """
        path = '/'.join(self.getPhysicalPath())
        result = self.portal_catalog(Type='Fedora Multimedia', path=path, getMMType='alternative_format', sort_on='getObjPositionInParent')
        x = []
        for item in result:
            obj = item.getObject()
            mimetype = obj.get_content_type()
            if mimetype == 'application/pdf':
                x.append(item)
        if len(x) > 0:
            return x[0].getURL()
        else:
            return False
         

        
    
registerType(FedoraArticle,PROJECTNAME)
