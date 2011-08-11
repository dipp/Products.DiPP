## Script (Python) "reminder"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self
##title=
##

""" This script sends out regular reminder mails to reviewer
    it has to be called vi a cronjob:

    #every 2 minutes, for testing
    */2 * * * * /usr/bin/wget -O - http://localhost:8080/dev/reminder
"""

# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName

request  = container.REQUEST
#RESPONSE = request.RESPONSE

portal_url = getToolByName(self, 'portal_url')
portal = portal_url.getPortalObject()
mship = self.portal_membership
mhost = portal.MailHost

today = DateTime()

results = container.portal_catalog(portal_type='Submission')

#actor_name = mship.getMemberById(actor).getProperty('fullname')
#comment = state_change.kwargs.get('comment', '')
comment = "mailbody"

header = """Content-Type: text/plain; charset="UTF-8"
From: %(from_name)s <%(from_email)s>
To: %(to_name)s <%(to_email)s>
X-DiPPReview: demo
X-DiPPJournal: %(journal)s
Subject: """

friendly_reminder_pr_reviewer_subject = portal.portal_properties.dippreview_properties.friendly_reminder_pr_reviewer_subject
friendly_reminder_pr_reviewer_mail    = portal.portal_properties.dippreview_properties.friendly_reminder_pr_reviewer_mail

deadline_reminder_pr_reviewer_subject = portal.portal_properties.dippreview_properties.deadline_reminder_pr_reviewer_subject
deadline_reminder_pr_reviewer_mail    = portal.portal_properties.dippreview_properties.deadline_reminder_pr_reviewer_mail

due_reminder_pr_reviewer_subject      = portal.portal_properties.dippreview_properties.due_reminder_pr_reviewer_subject
due_reminder_pr_reviewer_mail         = portal.portal_properties.dippreview_properties.due_reminder_pr_reviewer_mail

time_format = "%Y-%m-%d"

def sorttimes(times):
    """converts the unsorted tuple of deadlines, which are stored by plone as strings
       as a sorted list of floats
    """
    list = []
    for i in times:
        list.append(float(i))
    list.sort()
    return list
    
def sendreminder(object, to_name, to_email, subject, body, deadline = None, days_due = None):
    """
    """
    footer = portal.portal_properties.dippreview_properties.email_footer
    from_email = portal.email_from_address
    from_name = portal.email_from_name
    actor_name = portal.email_from_name
    journal = portal.title
    
    if deadline:
        deadline = DateTime.strftime(deadline, time_format)
                
    template = header + subject +"\n\n" + body + footer
    mail = template % {
        'from_name':from_name,
        'from_email':from_email,
        'to_name':to_name,
        'to_email':to_email,
        'journal': journal,
        'submission_id':object.id,
        'manuscript_url':object.absolute_url(),
        'manuscript_title':str(object.title),
        'comment':comment,
        'actor_name':actor_name,
        'deadline':deadline,
        'days_due':days_due
    }
    
    mhost.send(mail)
    

friendly_reminder_times = sorttimes(portal.portal_properties.dippreview_properties.friendly_reminder_times)
deadline_reminder_times = sorttimes(portal.portal_properties.dippreview_properties.deadline_reminder_times)
due_reminder_times = sorttimes(portal.portal_properties.dippreview_properties.due_reminder_times)

print "friendly: %s, deadline: %s due: %s" % (len(friendly_reminder_times), len(deadline_reminder_times), len(due_reminder_times) ) 

for result in results:
    object = result.getObject()
    revision = object.current_revision
    print "\nID:##### %s rev:%s #####" % (result.id, revision)
    ri = object.getReviewerInfo()
    for reviewer in object.reviewer_considered:
        print reviewer
        to_name = mship.getMemberById(str(reviewer)).getProperty('fullname')
        to_email = mship.getMemberById(str(reviewer)).getProperty('email')

        details = False
        try:
            details = ri[revision][reviewer]
        except:
            print "Could not get details of reviewer"
        print details
        if details:

            # get the dates
            date_invited = details.get('date_invited',None)
            date_accepted = details.get('date_accepted',None)
            date_declined = details.get('date_declined',None)
            date_submitted = details.get('date_submitted',None)

            # number of emails
            friendly_reminders = details.get('friendly_reminders',[])
            if not friendly_reminders:
                friendly_reminders = []
                
            deadline_reminders = details.get('deadline_reminders',[])
            if not deadline_reminders:
                deadline_reminders = []

            due_reminders = details.get('due_reminders',[])
            if not due_reminders:
                due_reminders = []

            # send the friendly reminder
            print "FRIENDLY REMINDER"
            if date_invited and not date_accepted and not date_declined and not date_submitted:
                days_invited = today - date_invited
                for days in friendly_reminder_times:
                    sent = False
                    if days_invited > days and days not in friendly_reminders:
                        sent = True
                        deadline = None
                        subject = friendly_reminder_pr_reviewer_subject
                        body = friendly_reminder_pr_reviewer_mail
                        friendly_reminders.append(days)
                        object.setReviewerProperty(revision=revision, reviewer=reviewer, property='friendly_reminders', value=friendly_reminders)
                        sendreminder(object, to_name, to_email, subject, body, deadline)
                    print friendly_reminder_times.index(days), days, days_invited, sent
            else:
                print "not send"
                
            # send the deadline reminder
            print "DEADLINE REMINDER"
            if date_accepted and not date_declined and not date_submitted:
                deadline = details.get('deadline',None)
                if deadline:
                    days_till_deadline = deadline - today
                    deadline_reminder_times.reverse()
                    for days in deadline_reminder_times:
                        send = False
                        if days_till_deadline < days and days not in deadline_reminders:
                            send = True
                            subject = deadline_reminder_pr_reviewer_subject
                            body = deadline_reminder_pr_reviewer_mail
                            deadline_reminders.append(days)
                            object.setReviewerProperty(revision=revision, reviewer=reviewer, property='deadline_reminders', value=deadline_reminders)
                            sendreminder(object, to_name, to_email, subject, body, deadline)
                        print deadline_reminder_times.index(days) + 1, days, days_till_deadline, send
                else:
                    print "no deadline set"
            else:
                print "not send"
                
            # send the due reminder
            print "DUE REMINDER"
            if date_accepted and not date_declined and not date_submitted:
                print "send"
                deadline = details.get('deadline',None)
                if deadline:
                    days_since_deadline = today - deadline
                    for days in due_reminder_times:
                        send = False
                        if days_since_deadline > days and days not in due_reminders:
                            send = True
                            subject = due_reminder_pr_reviewer_subject
                            body = due_reminder_pr_reviewer_mail
                            days_due = days
                            due_reminders.append(days)
                            sendreminder(object, to_name, to_email, subject, body, deadline, days_due)
                            object.setReviewerProperty(revision=revision, reviewer=reviewer, property='due_reminders', value=due_reminders)
                        print due_reminder_times.index(days) + 1, days, days_since_deadline, send
                else:
                    print "no deadline set"
            else:
                print "not send"
            

return printed
