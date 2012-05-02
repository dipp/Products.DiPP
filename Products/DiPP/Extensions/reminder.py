from DateTime import DateTime
from time import *
import smtplib


def reminder(self):
    oftool = self.portal_openflow
    mtool  = self.portal_membership

    red    = self.portal_properties.deadline_red
    yellow = self.portal_properties.deadline_yellow



    try:
        mailhost=getattr(self, self.portal_url.superValues('Mail Host')[0].id)
    except:
        raise AttributeError, "Cannot find a Mail Host object"

    fromEmail = "DiPP-Admin <" + self.portal_properties.email_from_address + ">"
    workitems = oftool.Catalog(meta_type='Workitem',sort_on='creation_time')

    #send a copy of the reminder to following recipients
    copy_of_reminder = self.portal_properties.copy_of_reminder
    
    if copy_of_reminder[0] != '':
        cc = []
        for user in copy_of_reminder:
            member   = self.ext.getMember(user)
            email = member['mail']
            fullname = member['cn']
            cc.append(fullname + " <" + email + ">")
        print cc
    else:
        cc = None
    
    i = 0 # number of sent mails
    for item in workitems:
        wi = item.getObject()
        if wi.status != 'complete' and wi.actor != '':
            member    = self.ext.getMember(wi.actor)
            autor     = self.ext.getMember(wi.autor)
            instance, workitem =  oftool.getInstanceAndWorkitem(wi.instance_id,wi.id)
            instance_id  = wi.instance_id
            workitem_id  = wi.id

            if member != None:
                email = member['cn'] + " <" + member['mail'] + ">"
                lang  = member['preferredLanguage']
            else:
                email = "no email"
            days = workitem.deadline_next - DateTime()

            alert = instance.alert
            sendmail = 'False'

            if red < days < yellow and alert != "yellow":
                sendmail = "True"
                i += 1
                alert = "yellow"
                mailbody = findMailtemplate(self,alert,lang)
            elif days <= red and alert != "red":
                sendmail = "True"
                i += 1
                alert = "red"
                mailbody = findMailtemplate(self,alert,lang)
            else:
                alert = alert
                mailbody =""
            print "instance: ", workitem.instance_id
            print "sendmail: ", sendmail
            print "alert:    ", alert
            print "days:     ", days, "red", red, "yellow", yellow
            print "---------------------"

            if sendmail == 'True':
                message  = "Sehr geehrte(r) " + member['cn'] + ",\n"
                message += mailbody
                message += "\n\n"
                message += self.article_info(instance_id,workitem_id)
                mailhost.send(message, email, fromEmail,alert)

                carboncopy  = "Zur Info \n"
                #carboncopy += "Folgende Email wurde an " + member.fullname  + " verschickt\n\n"
                carboncopy += "Folgende Email wurde an " + member['cn']  + " verschickt\n\n"
                carboncopy += message
                
                if cc != None:
                    mailhost.send(carboncopy, cc, fromEmail,"Zur Info: " + alert)
                else:
                    pass

                nachrichten  = "von: auto\n"
                nachrichten += message
                nachrichten += "======================================\n"
                nachrichten += workitem.nachrichten
                
                # save the email in the workflow instance
                instance.manage_changeProperties({'nachrichten':nachrichten,
                                                  'alert':alert})
                # save in MySQL database
                self.ext.history_insert(instance_id=instance_id,
                        workitem_id=workitem_id,
                        process_id=wi.process_id,
                        #activity_id=wi.activity_id,
                        activity_id='reminder',
                        message=message,
                        formalOK=str(wi.formalOK),
                        autorOK=str(wi.autorOK),
                        gastHrsgOK=str(wi.gastHrsgOK),
                        deadline=wi.deadline.strftime("%Y-%m-%d %H:%M:%S"),
                        deadline_next=wi.deadline_next.strftime("%Y-%m-%d %H:%M:%S"),
                        autor=wi.autor,
                        titel=wi.titel,
                        #ausgabe=wi.ausgabe,
                        actor=wi.actor)

            else:
                pass

    print str(i) + " Erinnerungsmail(s) wurden verschickt!"
    return "<b>" + str(i) + " Erinnerungsmail(s) wurden verschickt!</b>"

def findMailtemplate(self, alert, lang):

    mail_red_de    = self.portal_properties.deadline_red_email_de
    mail_red_en    = self.portal_properties.deadline_red_email_en
    mail_yellow_de = self.portal_properties.deadline_yellow_email_de
    mail_yellow_en = self.portal_properties.deadline_yellow_email_en
    print "language:",lang
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


