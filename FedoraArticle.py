# -*- coding: utf-8 -*-
from Products.Archetypes.public import *
from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from config import PROJECTNAME
from AccessControl import ClassSecurityInfo
import Permissions
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from Products.CMFCore.utils import getToolByName
from zLOG import LOG, ERROR, INFO

class FedoraArticle(BrowserDefaultMixin, OrderedBaseFolder):
    """An article, which has gone through a peer review. Please add through the EDITORIAL TOOLBOX"""
    
    security = ClassSecurityInfo()
    __implements__ = (getattr(BrowserDefaultMixin,'__implements__',()),) + (getattr(OrderedBaseFolder,'__implements__',()),)

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
        LinesField('AvailableAbstracts',
            required=0,
            widget=LinesWidget(
                label='Available Abstracts',
                label_msgid='label_issue_field',
                description='Languages, in which abstracts are available',
                description_msgid='help_issue_field',
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
          "name": "Dublin Core",
          "action": "string:${folder_url}/fedoraarticle_qdc",
          "permissions": (Permissions.EDIT_CONTENTS_PERMISSION,),
          "category":"folder",
          },
    )
    
    security.declareProtected(Permissions.EDIT_CONTENTS_PERMISSION, 'syncMetadata')
    def syncMetadata(self):
        """keep Metadata of Plone and Fedora synchron"""
        fedora = getToolByName(self, 'fedora')
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
        
        available_abstracts = []
        for abstract in qdc['DCTermsAbstract']:
            available_abstracts.append(abstract['lang'])
        self.setAvailableAbstracts(available_abstracts)
        
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
         

        
    
registerType(FedoraArticle,PROJECTNAME)
