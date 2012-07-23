# -*- coding: utf-8 -*-
# The FedoraXML ContentType
#
# German Free Software License (D-FSL)
#
# This Program may be used by anyone in accordance with the terms of the
# German Free Software License
# The License may be obtained under <http://www.d-fsl.org>.
#
# $Id$

from zope.interface import implements, Interface
from Products.Archetypes.public import *
from Products.Archetypes.Marshall import PrimaryFieldMarshaller
from Products.DiPP.config import PROJECTNAME
from Products.DiPP.interfaces import IFedoraXML
from Products.DiPP import Permissions

FedoraXMLSchema = BaseSchema + Schema((
        TextField('body',
                searchable=1,
                required=0,
                primary=1,
                allowable_content_types=('text/xml'),
                widget=TextAreaWidget(label='Body Content')
        ),
        StringField('PID',
                required=1,
                widget=StringWidget(
                    label='PID',
                    description='Persistent Identifier',
                    size='15',
                    visible=-1
                ),
        ),
        StringField('DsID',
                required=1,
                widget=StringWidget(
                    label='DsID',
                    description='Datastream Identifier',
                    size='15',
                    visible=-1)
        ),
        StringField('MIMEType',
                required=0,
                widget=StringWidget(label='MIMEType',description='MIMEType of Object',size='25')
        ),
    ),
    marshall=PrimaryFieldMarshaller(),
    )

class FedoraXML(BaseContent):
    """stores the DocBOOK XML Files"""
    
    implements(IFedoraXML)
    
    schema = FedoraXMLSchema

registerType(FedoraXML,PROJECTNAME)
