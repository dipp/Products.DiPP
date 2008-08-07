## Controller Python Script "submitemail"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=self,section='', surname='', email="",  comment="", file='', licence=''
##title=
##
import base64
from Products.CMFCore.utils import getToolByName
request  = container.REQUEST
RESPONSE = request.RESPONSE

portal_url = getToolByName(self, 'portal_url')
fedora = getToolByName(self, 'fedora')
portal = portal_url.getPortalObject()
mhost = context.MailHost

site_properties = context.portal_properties.site_properties
props = self.portal_properties.dipp_properties

if hasattr(props, 'big_brother'):
    bcc = self.portal_properties.dipp_properties.big_brother
else:
    bcc = ""

try:
    upload = getattr(portal,'upload_folder')
except:
    portal.invokeFactory('Folder','upload_folder')
    upload = getattr(portal,'upload_folder')

if hasattr(self, "sections"):
    sections = self.sections()
else:
    sections = {}

section_name = sections[section]['name']

title = file.filename.split("\\")[-1]
extension = title.split('.')[-1]
tempID = fedora.getTempID(request) + '.' + extension
upload.invokeFactory(id=tempID, type_name='File', file=file, title=title)
obj = getattr(upload,tempID)
url = obj.absolute_url()

obj.manage_permission('View',('Owner','Manager',),acquire=0)
journal = site_properties.title

try:
    recipient = sections[section]['mail']
    if recipient == "":
        recipient = self.portal_properties.email_from_address
        
except:
    recipient = self.portal_properties.email_from_address


message = """
From: %(surname)s <%(email)s>
To: %(recipient)s
Bcc: %(bcc)s
Content-Type: text/plain; charset=UTF-8;
X-DiPP-Journal: %(journal)s
Subject: New Submission to  %(journal)s

name: %(surname)s
email: %(email)s
licence: %(licence)s
section: %(section)s
url: %(url)s
%(comment)s
"""

msg = message % {
    'surname':surname,
    'email':email,
    'section':section_name,
    'recipient':recipient,
    'bcc':bcc,
    'licence':licence,
    'url':url,
    'comment':comment,
    'journal':journal
    }

mhost.send(msg)

#print msg
#return printed
return state
