from time import *
import smtplib
import logging
from DateTime import DateTime
from OFS.SimpleItem import SimpleItem
from AccessControl import ClassSecurityInfo
from Products.CMFCore.utils import UniqueObject, getToolByName

logger = logging.getLogger("DiPP")


class Deadlines(UniqueObject, SimpleItem):
    """Deadline calculations."""

    meta_type = 'Deadlines'
    id = 'deadlines'
    title = 'Calculation of deadlines'
    security = ClassSecurityInfo()

    def deadline_date(self, max):
        '''max: deadline des Artikels'''
        portal_url = getToolByName(self, 'portal_url')
        portal = portal_url.getPortalObject()
        dprops = portal.portal_properties.dipp_properties

        liste = []
        now = DateTime()
        if max == dprops.deadline_no:
            delta = dprops.deadline_max
        else:
            delta = max - now
        for i in range(0, delta):
            date = now + i
            if date.dow() == 0:
                klasse = 'sonntag'
            elif date.dow() == 6:
                klasse = 'samstag'
            else:
                klasse = 'wochentag'
            liste.append({'value': date, 'class': klasse})
        return liste

    def deadline_time(selected):
        liste = []
        for i in range(24):
            if i == selected:
                select = "selected"
            else:
                select = ""
            liste.append({'H': i, 'M': '00', 'selected': select})
        return liste

    def deadline_delay(self, date):
        """Delay."""
        portal_url = getToolByName(self, 'portal_url')
        portal = portal_url.getPortalObject()
        dprops = portal.portal_properties.dipp_properties

        red = dprops.deadline_red
        yellow = dprops.deadline_yellow
        days = date - DateTime()
        delay = {}

        delay['days'] = str(int(days))
        hours = DateTime((days - int(days)) * 24 * 60 * 60)
        delay['hours'] = hours
        if days <= red:
            alert = "red"
        elif red < days < yellow:
            alert = "yellow"
        else:
            alert = "green"
        delay['class'] = alert
        return delay

    def reminder(self):
        """Send reminder emails during the publishing workflow."""
        logger.info("Sending reminder emails")
        portal_url = getToolByName(self, 'portal_url')
        portal = portal_url.getPortalObject()
        dprops = portal.portal_properties.dipp_properties

        oftool = self.portal_openflow
        mtool = self.portal_membership

        red = dprops.deadline_red
        yellow = dprops.deadline_yellow

        try:
            mailhost = getattr(self, self.portal_url.superValues('Mail Host')[0].id)
        except:
            raise AttributeError, "Cannot find a Mail Host object"

        fromEmail = "DiPP-Admin <" + self.portal_properties.email_from_address + ">"
        workitems = oftool.Catalog(meta_type='Workitem', sort_on='creation_time')

        # send a copy of the reminder to following recipients
        copy_of_reminder = dprops.copy_of_reminder

        if copy_of_reminder[0] != '':
            cc = []
            for user in copy_of_reminder:
                member = self.ext.getMember(user)
                email = member['mail']
                fullname = member['cn']
                cc.append(fullname + " <" + email + ">")
            print cc
        else:
            cc = None

        i = 0  # number of sent mails
        for item in workitems:
            wi = item.getObject()
            if wi.status != 'complete' and wi.actor != '':
                member = self.ext.getMember(wi.actor)
                autor = self.ext.getMember(wi.autor)
                instance, workitem = oftool.getInstanceAndWorkitem(wi.instance_id, wi.id)
                instance_id = wi.instance_id
                workitem_id = wi.id

                if member != None:
                    email = member['cn'] + " <" + member['mail'] + ">"
                    lang = member['preferredLanguage']
                else:
                    email = "no email"
                days = workitem.deadline_next - DateTime()

                alert = instance.alert
                sendmail = 'False'

                if red < days < yellow and alert != "yellow":
                    sendmail = "True"
                    i += 1
                    alert = "yellow"
                    mailbody = findMailtemplate(self, alert, lang)
                elif days <= red and alert != "red":
                    sendmail = "True"
                    i += 1
                    alert = "red"
                    mailbody = findMailtemplate(self, alert, lang)
                else:
                    alert = alert
                    mailbody = ""
                print "instance: ", workitem.instance_id
                print "sendmail: ", sendmail
                print "alert:    ", alert
                print "days:     ", days, "red", red, "yellow", yellow
                print "---------------------"

                if sendmail == 'True':
                    message = "Sehr geehrte(r) " + member['cn'] + ",\n"
                    message += mailbody
                    message += "\n\n"
                    message += self.article_info(instance_id, workitem_id)
                    mailhost.send(message, email, fromEmail, alert)

                    carboncopy = "Zur Info \n"
                    # carboncopy += "Folgende Email wurde an " + member.fullname  + " verschickt\n\n"
                    carboncopy += "Folgende Email wurde an " + member['cn'] + " verschickt\n\n"
                    carboncopy += message

                    if cc != None:
                        mailhost.send(carboncopy, cc, fromEmail, "Zur Info: " + alert)
                    else:
                        pass

                    nachrichten = "von: auto\n"
                    nachrichten += message
                    nachrichten += "======================================\n"
                    nachrichten += workitem.nachrichten

                    # save the email in the workflow instance
                    instance.manage_changeProperties({'nachrichten': nachrichten,
                                                      'alert': alert})

                else:
                    pass

        print str(i) + " Erinnerungsmail(s) wurden verschickt!"
        return "<b>" + str(i) + " Erinnerungsmail(s) wurden verschickt!</b>"

    def findMailtemplate(self, alert, lang):
        portal = getToolByName(self, 'portal_url').getPortalObject()
        dprops = portal.portal_properties.dipp_properties

        mail_red_de = dprops.deadline_red_email_de
        mail_red_en = dprops.deadline_red_email_en
        mail_yellow_de = dprops.deadline_yellow_email_de
        mail_yellow_en = dprops.deadline_yellow_email_en
        print "language:", lang
        if alert == "yellow":
            if lang == "de":
                return mail_yellow_de
            elif lang == "en":
                return mail_yellow_en
            else:
                return "no template found"

        elif alert == "red":
            if lang == "de":
                return mail_red_de
            elif lang == "en":
                return mail_red_en
            else:
                return "no template found"
        else:
            return "no template found"
