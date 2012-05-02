# -*- coding: utf-8 -*-
#
# File: DiPPReview.py
#
# Copyright (c) 2011 by DiPP, hbz
# Generator: ArchGenXML Version 1.5.2
#            http://plone.org/products/archgenxml
#
# German Free Software License (D-FSL)
#
# This Program may be used by anyone in accordance with the terms of the 
# German Free Software License
# The License may be obtained under <http://www.d-fsl.org>.
#

__author__ = """Peter Reimer <reimer@hbz-nrw.de>"""
__docformat__ = 'plaintext'


# Workflow Scripts for: peerreview_workflow

##code-section workflow-script-header #fill in your manual code here

from DateTime import DateTime
from Products.DiPP.mail_templates import EMAIL_HEADER as header
from Products.DiPP.mail_templates import EMAIL_FOOTER as footer
from Products.CMFCore.utils import getToolByName
import logging

logger = logging.getLogger("DiPPReview")


def send_mail(self, state_change, recipient="", subject="", body="", **kwargs):
    """send mail in the workflow"""

    object = getattr(state_change, 'object')
    if object.portal_type == "Submission":

        portal = state_change.getPortal()
        mhost = portal.MailHost
        wf_tool = portal.portal_workflow
        mship = portal.portal_membership
        props = self.portal_properties.dippreview_properties
        actor = wf_tool.getInfoFor(object, 'actor')
        to_email = mship.getMemberById(recipient).getProperty('email')
        #to_email = "reimer@localhost"
        to_name = mship.getMemberById(recipient).getProperty('fullname')
        from_email = portal.email_from_address
        from_name = portal.email_from_name
        retrieve_pwd_url = "URL"
        deadline = kwargs.get('deadline','')
        decision_deadline = kwargs.get('decision_deadline','')
        user_id = kwargs.get('user_id','')
        max_review_time = str(props.max_review_time)
        self.plone_log("DiPPReview: max review time: " + max_review_time)
        min_reviewers = str(props.min_reviewers)

        # we do not have an actor, when the transition is triggert via the email link
        # Anonymous is than used instead of the real user name
        try:
            actor_name = mship.getMemberById(actor).getProperty('fullname')
        except:
            actor_name = 'Anonymous'
        journal = portal.title
        comment = state_change.kwargs.get('comment', '')

        template = header + subject +"\n\n" + body

        try:
            mail = template % {
                'from_name':from_name,
                'from_email':from_email,
                'to_name':to_name,
                'to_email':to_email,
                'journal': journal,
                'max_review_time': max_review_time,
                'min_reviewers':min_reviewers,
                'submission_id':object.id,
                'date_submitted':object.date_submitted,
                'manuscript_url':object.absolute_url(),
                'manuscript_title':str(object.title),
                'comment':comment,
                'actor_name':actor_name,
                'deadline':deadline,
                'decision_deadline':decision_deadline,
                'retrieve_pwd_url':retrieve_pwd_url,
                'user_id':user_id
            }
        except:
            msg = "Could not fill mailtemplate '%s' for user %s" % (body, recipient)
            self.plone_log("DiPPReview: " + msg)

        try:
            mhost.send(mail)
        except:
            msg = "Could not send Mail"
            self.plone_log("DiPPReview: " + msg)



##/code-section workflow-script-header


def submit_review(self, state_change, **kw):
    portal = state_change.getPortal()
    wf_tool = portal.portal_workflow
    p = self.portal_properties.dippreview_properties
    mship = self.portal_membership
    object = getattr(state_change, 'object')
    revision = int(wf_tool.getInfoFor(object, 'revision'))
    actor = wf_tool.getInfoFor(object, 'actor')
    sectioneditors = self.getSectionEditors(self, object.section)
    reviewer_id = state_change.kwargs.get('reviewer_id', actor)
    object.setReviewerProperty(revision=revision, reviewer=reviewer_id, property='date_submitted', value = DateTime())

    # mails to section editors
    for sectioneditor in sectioneditors:
        send_mail(self, state_change,
            recipient = sectioneditor['id'],
            subject = p.submitreview_pr_sectioneditor_subject,
            body = p.submitreview_pr_sectioneditor_mail)

    # confirmation mail to reviewer
    send_mail(self, state_change,
        recipient = actor,
        subject = p.submitreview_pr_reviewer_subject,
        body = p.submitreview_pr_reviewer_mail)



def decline_invitation(self, state_change, **kw):
    """decline to be a reviewer"""
    portal = state_change.getPortal()
    wf_tool = portal.portal_workflow
    p = self.portal_properties.dippreview_properties
    mship = self.portal_membership
    object = getattr(state_change, 'object')
    revision = int(wf_tool.getInfoFor(object, 'revision'))
    comment = state_change.kwargs.get('comment', '')
    actor = wf_tool.getInfoFor(object, 'actor')
    reviewer_id = state_change.kwargs.get('reviewer_id', actor)
    roles = ['pr_ReviewerDeclined']
    object.manage_addLocalRoles(reviewer_id, roles)
    object.setReviewerProperty(revision=revision, reviewer=reviewer_id, property='date_declined', value = DateTime())
    #object.setReviewerProperty(revision = object.current_revision, reviewer=reviewer_id, property='deadline', value = DateTime() + int(p.review_time))
    msg = "Role %s assigned to user %s for submission %s" % (roles[0], reviewer_id, object.id)
    self.plone_log("DiPPReview: " + msg)
    section = object.section
    ptool = getToolByName(portal, 'dipp_peerreview')
    sectioneditors = ptool.getSectionEditors(section)
    self.plone_log(section, sectioneditors)
    for sectioneditor in sectioneditors:
        send_mail(self, state_change,
            recipient = sectioneditor['id'],
            subject = p.decline_pr_sectioneditor_subject,
            body = p.decline_pr_sectioneditor_mail)



def deskreject(self, state_change, **kw):
    pass



def submit(self, state_change, **kw):
    """run after the submit transition"""

    portal = state_change.getPortal()
    object = getattr(state_change, 'object')
    creator = object.Creator()
    section = object.section
    sectioneditors = self.getSectionEditors(self, section)
    logger.info(sectioneditors)
    p = self.portal_properties.dippreview_properties

    self.setDate_submitted(DateTime())
    self.addReviewerInfo(revision=0)
    object.manage_addLocalRoles(creator, ['pr_Author'])
    object.reindexObject()
    for sectioneditor in sectioneditors:
        object.manage_addLocalRoles(sectioneditor['id'], ['pr_SectionEditor'])

    # send mail to the sectioneditor
    for sectioneditor in sectioneditors:
        send_mail(self, state_change,
            recipient = sectioneditor['id'],
            subject = p.submit_pr_sectioneditor_subject,
            body = p.submit_pr_sectioneditor_mail)

    # send mail to the author/submitter of the manuscript
    send_mail(self, state_change,
        recipient = creator,
        subject = p.submit_pr_author_subject,
        body = p.submit_pr_author_mail)



def invite_reviewer(self, state_change, **kw):
    """invite reviewer"""
    portal = state_change.getPortal()
    object = getattr(state_change, 'object')
    wf_tool = portal.portal_workflow
    p = self.portal_properties.dippreview_properties
    comment          = state_change.kwargs.get('comment', '')
    code_accept      = state_change.kwargs.get('code_accept', '')
    code_decline     = state_change.kwargs.get('code_decline', '')
    code_unavailable = state_change.kwargs.get('code_unavailable', '')
    reviewer_id      = state_change.kwargs.get('reviewer_id', '')
    roles = ['pr_ReviewerInvited']
    object.manage_addLocalRoles(reviewer_id, roles)
    revision = int(wf_tool.getInfoFor(object, 'revision'))
    msg = "Role %s assigned to user %s for submission %s" % (roles[0], reviewer_id, object.id)
    self.plone_log("DiPPReview: " + msg)
    object.setReviewerProperty(revision=revision, reviewer=reviewer_id, property='date_invited', value=DateTime())
    object.setReviewerProperty(revision=revision, reviewer=reviewer_id, property='code_accept', value=code_accept)
    object.setReviewerProperty(revision=revision, reviewer=reviewer_id, property='code_decline', value=code_decline)
    object.setReviewerProperty(revision=revision, reviewer=reviewer_id, property='code_unavailable', value=code_unavailable)
    creator = object.Creator()
    send_mail(self, state_change,
        recipient = creator,
        subject = p.invite_pr_reviewer_subject,
        body = comment)

def request_revision(self, state_change, **kw):
    portal = state_change.getPortal()
    p = self.portal_properties.dippreview_properties
    wf_tool = portal.portal_workflow
    mship = self.portal_membership
    object = getattr(state_change, 'object')
    creator = object.Creator()
    actor = wf_tool.getInfoFor(object, 'actor')
    revision = int(wf_tool.getInfoFor(object, 'revision'))
    comment = state_change.kwargs.get('comment', '')
    current_revision = revision + 1
    logger.info(revision)
    object.manage_changeProperties({'current_revision':current_revision})
    object.setCurrent_revision(current_revision)
    object.reindexObject()

    send_mail(self, state_change,
        recipient = creator,
        subject = p.requestrevision_pr_author_subject,
        body = comment)



def resubmit(self, state_change, **kw):
    portal = state_change.getPortal()
    wf_tool = portal.portal_workflow
    object = getattr(state_change, 'object')
    revision = int(wf_tool.getInfoFor(object, 'revision'))
    self.addReviewerInfo(revision=revision)
    



def accept_invitation(self, state_change, **kw):
    """accepting to be a reviewer"""
    portal = state_change.getPortal()
    wf_tool = portal.portal_workflow
    p = self.portal_properties.dippreview_properties
    mship = self.portal_membership
    object = getattr(state_change, 'object')
    comment = state_change.kwargs.get('comment', '')
    actor = wf_tool.getInfoFor(object, 'actor')
    revision = int(wf_tool.getInfoFor(object, 'revision'))
    reviewer_id = state_change.kwargs.get('reviewer_id', actor)
    roles = ['pr_Reviewer']
    object.manage_addLocalRoles(reviewer_id, roles)
    object.setReviewerProperty(revision = revision, reviewer=reviewer_id, property='date_accepted', value = DateTime())
    deadline =  DateTime() + float(p.review_time)
    object.setReviewerProperty(revision = revision, reviewer=reviewer_id, property='deadline', value=deadline)
    msg = "Role %s assigned to user %s for submission %s" % (roles[0], reviewer_id, object.id)
    #self.plone_log("DiPPReview: " + msg)
    section = object.section
    ptool = getToolByName(portal, 'dipp_peerreview')
    sectioneditors = ptool.getSectionEditors(section)
    #self.plone_log(section, sectioneditors)

    for sectioneditor in sectioneditors:
        send_mail(self, state_change,
            recipient = sectioneditor['id'],
            subject = p.accept_pr_sectioneditor_subject,
            body = p.accept_pr_sectioneditor_mail,
            deadline = deadline,
            user_id = reviewer_id)

    send_mail(self, state_change,
        recipient = reviewer_id,
        subject = p.accept_pr_reviewer_subject,
        body = p.accept_pr_reviewer_mail,
        deadline = deadline,
        user_id = reviewer_id)



def request_technical_revision(self, state_change, **kw):
    """request a technical revision
    """
    portal = state_change.getPortal()
    wf_tool = portal.portal_workflow
    p = self.portal_properties.dippreview_properties
    mship = self.portal_membership
    object = getattr(state_change, 'object')
    creator = object.Creator()
    revision = int(wf_tool.getInfoFor(object, 'revision'))
    actor = wf_tool.getInfoFor(object, 'actor')
    comment = state_change.kwargs.get('comment', '')

    current_revision = object.current_revision + 1
    object.manage_changeProperties({'current_revision':current_revision})


