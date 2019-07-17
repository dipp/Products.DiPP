## Script (Python) "pub_modify_instance"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self
##title=
##
# -*- coding: utf-8 -*-
from DateTime import DateTime
from Products.CMFCore.utils import getToolByName

fedora = getToolByName(self, 'fedora')
bibtool = getToolByName(self, 'bibtool')
mhost = context.MailHost
translate = context.translate


mail_skeleton = """
Content-Type: text/plain; charset="UTF-8"
From: %(from_name)s <%(from_address)s>
To: %(recipient)s
Subject: %(journal)s: %(subject)s

%(body)s

"""


def finish():
    instance.manage_changeProperties({'alert': 'green'})
    oftool.completeWorkitem(instance_id=instance_id, workitem_id=workitem_id)
    context.plone_utils.addPortalMessage(msg)
    RESPONSE.redirect('%s/worklist' % context.absolute_url())


def getCitation(PID):
    limit = 1
    qdc = fedora.getQualifiedDCMetadata(PID)
    articles = container.portal_catalog(portal_type='FedoraArticle', getPID=PID, sort_limit=limit)[:limit]
    for article in articles:
        item = article.getObject()
        section = item.getJournal_section()
        citation = bibtool.recommended_citation(PID, qdc)
    return citation


request = container.REQUEST
RESPONSE = request.RESPONSE
oftool = container.portal_openflow
mtool = context.portal_membership
portal_url = getToolByName(self, 'portal_url')
portal = portal_url.getPortalObject()

instance_id = request.form['instance_id']
workitem_id = request.form['workitem_id']
process_id = request.form['process_id']
activity_id = request.form['activity_id']
actor = request.form['actor']
instance, workitem = oftool.getInstanceAndWorkitem(instance_id, workitem_id)


# gibt es Kommentare
try:
    message = request.form['message']
    # if workitem.actor != None:
    #   von = workitem.actor
    # else:
    #   von = actor
    von = actor
    nachrichten = "von: " + von + "\n"
    nachrichten += message + "\n"
    nachrichten += "======================================\n"
    nachrichten += workitem.nachrichten + "\n"
except:
    nachrichten = workitem.nachrichten

#wurden Artikeldaten geaendert
autor = request.form.get('autor', workitem.autor)
PID = request.form.get('PID', workitem.PID)
isChildOf = request.form.get('isChildOf', workitem.isChildOf)
isParentOf = request.form.get('isParentOf', workitem.isParentOf)
url = request.form.get('url', workitem.url)
type = request.form.get('type', workitem.type)
hierarchie = request.form.get('hierarchie', workitem.hierarchie)
formalOK = request.form.get('formalOK', workitem.formalOK)
autorOK = request.form.get('autorOK', workitem.autorOK)
gastHrsgOK = request.form.get('gastHrsgOK', workitem.gastHrsgOK)
next_actor = request.form.get('next_actor', actor)
newId = request.form.get('newId', instance_id)

# wurde eine deadline gesetzt
try:
    deadline_next_date = request.form['deadline_next_date']
    deadline_next_time = request.form['deadline_next_time']
    deadline_next = DateTime(deadline_next_date + deadline_next_time)
except:
    deadline_next = workitem.deadline_next

try:
    deadline_date = request.form['deadline_date']
    deadline_time = request.form['deadline_time']
    deadline = DateTime(deadline_date + deadline_time)
except:
    deadline = workitem.deadline

try:
    autorOK_required = request.form['autorOK_required']
except:
    autorOK_required = True

try:
    gastHrsg = request.form['gastHrsg']
except:
    pass
# abarbeiten der einzelnen Aktivitaeten


# INITIALISIERUNG

if activity_id == 'initialize':
    if autorOK_required == False:
        autorOK = True

    if autor == "0":
        autorOK = True

    if gastHrsg == "0":
        gastHrsgOK = True

    moveObjectPID = PID
    sourceObjectPID = workitem.isChildOf[0]
    folders = container.portal_catalog(portal_type=('FedoraHierarchie', 'Issue', 'Volume'), Language='all')
    tempDir = getattr(portal, 'tmp')
    cut = tempDir.manage_cutObjects(instance_id)         # ausschneiden

    for folder in folders:                               # Zielorder suchen
        if folder.getObject().PID == isChildOf:
            destination = folder.getObject()             # Zielordner gefunden
            language = folder.Language
            destObjectPID = destination.PID
    destination.manage_pasteObjects(cut)                 # einfügen

    destination.manage_renameObject(instance_id, newId)  # umbenennen
    obj = getattr(destination, newId)
    obj.manage_changeProperties({'tmp': 0})
    obj.setLanguage(language)                            # sprache des Zielordners
    url = obj.absolute_url()                             # neue URL zurückgeben
    hierarchie = "/".join(url.split("/")[3:-1])          # verkürzte URL zur Darstellung in der worklist
    instance.manage_changeProperties({'nachrichten': nachrichten,
                                      'deadline': deadline,
                                      'url': url,
                                      'autor': autor,
                                      'autorOK': autorOK,
                                      # 'autorOK': True,
                                      'gastHrsgOK': gastHrsgOK,
                                      'hierarchie': hierarchie,
                                      'deadline_next': deadline_next})

    if url.startswith('https'):
        url = url.replace('https', 'http', 1)

    fedora.setURL(PID, url)
    fedora.moveObject(moveObjectPID, sourceObjectPID, destObjectPID)
    msg = "Der Artikel ist nun initialisiert und kann weiter bearbeitet werden."
    finish()

# BEARBEITEN
if activity_id == 'bearbeiten':
    instance.manage_changeProperties({'nachrichten': nachrichten,
                                      'deadline_next': deadline_next})
    msg = "Weitergeleitet zur Begutachtung durch den Herausgeber!"
    finish()

# BEGUTACHTEN
elif activity_id == 'begutachten':
    instance.manage_changeProperties({'nachrichten': nachrichten,
                                      'deadline_next': deadline_next,
                                      'formalOK': formalOK})
    msg = "Begutachtung abgeschlossen!"
    finish()

# ANSCHREIBEN
elif activity_id == 'anschreiben':
    PID = workitem.PID
    results = container.portal_catalog(portal_type='FedoraArticle', Language='all', getPID=PID)
    if len(results) == 1:
        article = results[0].getObject()
        roles = ['Autor']
        article.manage_addLocalRoles(autor, roles)
        context.plone_log("Role '%s' assigned to '%s' for %s at %s" % (' '.join(roles), autor, PID, article.absolute_url()))

    member = mtool.getMemberById(autor)
    fullname = member.getProperty('fullname', '')
    subject = "Imprimatur erforderlich"
    journal = self.portal_properties.title()
    recipient = member.getProperty('email', '')
    # member = context.ext.getMember(autor)
    # to_address  = member['mail']
    from_address = self.portal_properties.email_from_address
    from_name = self.portal_properties.email_from_name

    text = mail_skeleton % {
        'from_name': from_name,
        'from_address': from_address,
        'recipient': recipient,
        'journal': journal,
        'subject': subject,
        'body': message
    }
    mhost.send(text.encode("utf-8"))

    instance.manage_changeProperties({'nachrichten': nachrichten,
                                      'deadline_next': deadline_next})

    msg = "Der Autor wurde benachrichtigt!"
    finish()

#IMPREMATUR
elif activity_id == 'imprimatur':
    instance.manage_changeProperties({'autorOK': autorOK,
                                      'nachrichten': nachrichten,
                                      'deadline_next': deadline_next})
    msg = "Zurück zum Herausgeber zur erneuten Begutachtung"
    finish()

#SEGEN DES GASTHERAUSGEBER
elif activity_id == 'absegnen':
    instance.manage_changeProperties({'gastHrsgOK': gastHrsgOK,
                                      'nachrichten': nachrichten})
    msg = "Zurück zum Herausgeber zur erneuten Begutachtung"
    finish()

# FREISCHALTEN
elif activity_id == 'freischalten':
    instance.manage_changeProperties({'nachrichten': nachrichten})
    if type != 'DiPP:container':
        fedora.setPublishingState(PID, 1, 1)
    msg = "Der Artikel wurde veröffentlicht!"
    subject = "Neue Veröffentlichung"
    from_address = self.portal_properties.email_from_address
    from_name = self.portal_properties.email_from_name
    recipients = self.portal_properties.dipp_properties.alertEmailAddresses
    text = self.portal_properties.dipp_properties.alertEmailText
    journal = self.portal_properties.title()
    citation = getCitation(PID)
    # citation = "ohne spitze klammers"
    body = text % {'url': url, 'journal': journal, 'citation': citation}

    for recipient in recipients:
        text = mail_skeleton % {
            'from_name': from_name,
            'from_address': from_address,
            'recipient': recipient,
            'journal': journal,
            'subject': subject,
            'body': body
        }
        context.plone_log(text)
        mhost.send(text.encode("utf-8"))
    finish()


#PUSHWORKITEM
elif activity_id == 'pushworkitem':
    instance.manage_changeProperties({'nachrichten': nachrichten, 'deadline_next': deadline_next})
    msg = "Der Artikel wurde " + next_actor + " zugewiesen"
    """
    url  = context.absolute_url()
    url += "/portal_openflow/assignWorkitem"
    url += "?instance_id=" + instance_id
    url += "&portal_status_message=" + msg
    url += "&workitem_id=" + workitem_id
    url += "&process_id=" + process_id
    url += "&actor=" + next_actor
    """

    oftool.assignWorkitem(instance_id=instance_id, workitem_id=workitem_id, actor=next_actor)

    context.plone_utils.addPortalMessage(msg)
    RESPONSE.redirect('%s/all_worklists' % context.absolute_url())

else:
	pass
