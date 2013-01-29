# -*- coding: utf-8 -*-
# The Fedoradocument ContentType
#
# German Free Software License (D-FSL)
#
# This Program may be used by anyone in accordance with the terms of the
# German Free Software License
# The License may be obtained under <http://www.d-fsl.org>.
#
# $Id$

from AccessControl import ClassSecurityInfo
from zope.interface import implements

from Products.Archetypes.public import *
from Products.Archetypes.Marshall import PrimaryFieldMarshaller
from Products.CMFCore.permissions import View
from Products.CMFCore.utils import getToolByName

from Products.DiPP.config import PROJECTNAME
from Products.DiPP.interfaces import IFedoraDocument
from Products.DiPP import Permissions
        
FedoraDocumentSchema = BaseSchema + Schema((
        TextField('body',
                searchable=1,
                required=0,
                primary=1,
                allowable_content_types=('text/html',
                                   'text/structured',
                                   'text/plain',
                                   'text/xml'),
                widget=RichWidget(label='Body Content')
        ),
        StringField('PID',
                required=0,
                widget=StringWidget(
                    label='PID',
                    description='Persistent Identifier',
                    size='15',
                    visible=-1
                    ),
        ),
        StringField('DsID',
                required=0,
                widget=StringWidget(
                    label='DsID',
                    description='Datastream Identifier',
                    size='15',
                    visible=-1)
        ),
        StringField('MIMEType',
                required=0,
                widget=StringWidget(
                    label='MIMEType',
                    description='MIMEType of Object',
                    size='25',
                    visible={'edit':'invisible','view':'visible'}
                    )
        ),
    ),
    marshall=PrimaryFieldMarshaller(),
    )


class FedoraDocument(BaseContent):
    """store text files in the repository"""

    security = ClassSecurityInfo()
    implements(IFedoraDocument)
    
    schema = FedoraDocumentSchema
    
    _at_rename_after_creation = True
    
    security.declareProtected(Permissions.EDIT_CONTENTS_PERMISSION, 'make_working_copy')
    def make_working_copy(self, Date):
        """ take the datastream version of the given date and make it the working copy
        """
        fedora = getToolByName(self, 'fedora')
        content = fedora.access(self.PID, self.DsID, Date=Date)['stream']
        if content:
            self.setBody(content)
            return True
        else:
            return False

registerType(FedoraDocument,PROJECTNAME)
