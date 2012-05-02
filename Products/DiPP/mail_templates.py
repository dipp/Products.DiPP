# -*- coding: utf-8 -*-
EMAIL_HEADER = """Content-Type: text/plain; charset="UTF-8"
From: %(from_name)s <%(from_email)s>
To: %(to_name)s <%(to_email)s>
X-DiPPReview: demo 
Subject: """

TEST = """From: reimer@localhost
To: reimer@localhost
Subject: TEST

Hallo  Welt,
%(comment)s

"""

EMAIL_FOOTER = """--
BuR - Business Research
Official Open Access Journal of VHB
German Academic Association for Business Research
Website: www.business-research.org
E-Mail: info@business-research.org"""

SUBMIT_PR_AUTHOR_SUBJECT = """Confirmation of your Submission to %(journal)s"""
SUBMIT_PR_AUTHOR_MAIL = """Dear %(to_name)s,
thank you very much for submitting your paper

ID:    %(submission_id)s	
Title: '%(manuscript_title)s'		
to %(journal)s. It will now go through the following review process:

1) The chosen Department Editor will review the paper for fit and significance of contribution
with the mission of BuR.

2) If the Department Editor feels that the paper does not fit or has other obvious problems,
he/she may desk reject it immediately. If the paper passes this stage, the Department Editor
will send it to at least two qualified referees for detailed review.

3) The Department Editor will collect the reviews and make a decision, which he/she will
communicate to you.

Our goal at %(journal)s is to get feedback to you within %(max_review_time)s days of submission. If you experience
a delay well beyond %(max_review_time)s days, you should feel entitled to inquire with the Department Editor
about the status of your paper.

You can follow the state of progress via your manuscript link:
%(manuscript_url)s
Please note that the paper status shown is not always accurate, because editors and referees 
may communicate outside the system; nevertheless, all papers are monitored with respect
to their deadlines and editors/referees are sent periodic reminders by the system.

Sincerely,
%(actor_name)s
"""

SUBMIT_PR_SECTIONEDITOR_SUBJECT = """New Submission to %(journal)s"""
SUBMIT_PR_SECTIONEDITOR_MAIL = """Dear %(to_name)s,
a new manuscript has been submitted, formally checked and anonymized for review.
Manuscript-Title: '%(manuscript_title)s'
To start the review process and invite reviewers please follow the link
%(manuscript_url)s .

Comment:
%(comment)s

Sincerly,
%(actor_name)s 
"""

DESKREJECT_PR_AUTHOR_SUBJECT = """%(journal)s: Your manuscript is deskrejected"""
DESKREJECT_PR_AUTHOR_MAIL = """Dear %(to_name)s,
I am writing with regard to your paper submitted to %(journal)s:

ID:    %(submission_id)s    
Title: '%(manuscript_title)s'

In the meantime I have read your submission. Unfortunately, I regret to 
inform you that I have decided to reject your paper and will not have 
it continue in the review process for publication in %(journal)s.  

[GRUND]

Thank you for submitting your work to %(journal)s. I am sorry I cannot 
be more positive about this particular submission. However, I hope the
comments will be helpful to you.

While the outcome for this paper is not favourable please continue 
to submit your best work to %(journal)s.

Sincerely,
%(actor_name)s """


INVITE_PR_REVIEWER_SUBJECT = """%(journal)s: Invitation to review a manuscript """
INVITE_PR_REVIEWER_MAIL = """Dear %(to_name)s,
the paper

ID:     %(submission_id)s	
Title: '%(manuscript_title)s' 

has been submitted to the %(journal)s.

I would like to invite you to review this manuscript. The abstract appears at the end of this letter. 

Please note that BuR aims to complete the review process within %(max_review_time)s days. Therefore, I would be
interested to receive a referee report within approximately six weeks. Please let me know as soon as
possible if you will be able to accept my invitation to review.
If you are unable to review at this time, I would appreciate you recommending another expert reviewer.
You may e-mail me with your reply or click the appropriate link at the bottom of the page to 
automatically register your reply with our online manuscript submission and review system.

Once you accept my invitation to review this manuscript, you will be notified via e-mail about how to access the review system.

Please, click on one of the following responses to indicate your availability:

Agreed: %(link_agreed)s
Declined: %(link_declined)s
Unavailable: %(link_unavailable)s

I realize that our expert reviewers greatly contribute to the high standards of the %(journal)s and I thank you
for your present and future service.

Abstract: %(manuscript_abstract)s

Sincerely,

Editor
%(actor_name)s"""

ACCEPT_PR_REVIEWER_SUBJECT = """%(journal)s: Confirmation to review a manuscript """
ACCEPT_PR_REVIEWER_MAIL = """Dear %(to_name)s,

Thank you for agreeing to review paper

ID: %(submission_id)s
Title: '%(manuscript_title)s' 

which has been submitted to the %(journal)s.

I would be most grateful if you could complete your review within the next 6 weeks. I assigned the deadline of %(deadline)s.

To access the paper, login to %(journal)s website at 

%(manuscript_url)s

Your case-sensitive USER ID is: %(user_id)s.

If you do not know or have forgotten your password, please use the 'Password Help' function on your site log in page: 

%(retrieve_pwd_url)s

In your review, please answer all questions. On the review page, there is a space for "Comments to Editor" and a space for "Comments to the Author." 
Please be sure to put your constructive comments to the author in the appropriate space.

All communications regarding this manuscript are confidential.  Any conflict of interest, suspicion of duplicate publication, fabrication of data or plagiarism must immediately be reported to me.

Thank you for reviewing this manuscript.

Sincerely,

Editor
%(actor_name)s"""


ACCEPT_PR_SECTIONEDITOR_SUBJECT = """%(journal)s: Accept to review a manuscript """
ACCEPT_PR_SECTIONEDITOR_MAIL = """Dear %(to_name)s,
TODO: accept review mail template
ID:    %(submission_id)s	
Title: '%(manuscript_title)s'		
Url:%(manuscript_url)s .
Comment: %(comment)s

Sincerly,
%(actor_name)s """

DECLINE_PR_SECTIONEDITOR_SUBJECT = """%(journal)s: Decline to review a manuscript """
DECLINE_PR_SECTIONEDITOR_MAIL = """Dear %(to_name)s,
TODO: decline review mail template
ID:    %(submission_id)s	
Title: '%(manuscript_title)s'		
Url:%(manuscript_url)s .
Comment: %(comment)s

Sincerly,
%(actor_name)s """

SUBMITREVIEW_PR_SECTIONEDITOR_SUBJECT = """%(journal)s: A Review was submitted """
SUBMITREVIEW_PR_SECTIONEDITOR_MAIL = """Dear %(to_name)s,
TODO: submit review mail template
ID:    %(submission_id)s	
Title: '%(manuscript_title)s'		
Url:%(manuscript_url)s .
Comment: %(comment)s

Sincerly,
%(actor_name)s """

SUBMITREVIEW_PR_REVIEWER_SUBJECT = """%(journal)s: Thank you for submitting a Review """
SUBMITREVIEW_PR_REVIEWER_MAIL = """Dear %(to_name)s,
Thank you very much for reviewing the paper 

ID:    %(submission_id)s
Title: '%(manuscript_title)s'
For    :%(journal)s

We appreciate your voluntary contribution given to the Journal. We thank you very much for your participation in the online review process and hope to count on you for reviewing future papers.

Sincerly,
%(actor_name)s """

REQUESTREVISION_PR_AUTHOR_SUBJECT = """%(journal)s: A Revision of your manuscript is requested """
REQUESTREVISION_PR_AUTHOR_MAIL = """Dear %(to_name)s,
A Revision of your manuscript is requested
ID:    %(submission_id)s
Title: '%(manuscript_title)s'
Url:%(manuscript_url)s .

Sincerly,
%(actor_name)s """

FRIENDLY_REMINDER_PR_REVIEWER_SUBJECT = """%(journal)s: friendly reminder """
FRIENDLY_REMINDER_PR_REVIEWER_MAIL = """Dear %(to_name)s,

Recently, I invited you to review the paper

ID:     %(submission_id)s
Title: '%(manuscript_title)s'
For    :%(journal)s.

This e-mail is simply a reminder to give us an answer whether you are willing to review.

Please let me know as soon as possible if you will be able to accept my invitation to review.  If you are unable to review at this time, I would appreciate you recommending another expert reviewer.  You may e-mail me with your reply or click the appropriate link at the bottom of the page to automatically register your reply with our online manuscript submission and review system.

Once you accept my invitation to review this manuscript, you will be notified via e-mail about how to access the review system.

Agreed:  

Declined:  

Unavailable:  

I realize that our expert reviewers greatly contribute to the high standards of the %(journal)s and I thank you for your present and future service.

Abstract: 

Sincerly,
Editor
%(actor_name)s
"""

DEADLINE_REMINDER_PR_REVIEWER_SUBJECT = """%(journal)s: deadline reminder """
DEADLINE_REMINDER_PR_REVIEWER_MAIL = """Dear %(to_name)s,

This is a friendly reminder that I am expecting to receive your review of the paper 

ID:    %(submission_id)s
Title: '%(manuscript_title)s'
For:   %(journal)s .

by %(deadline)s. Thank you very much.

To access the paper, login to BuR – Business Research website at 

%(manuscript_url)s

Your case-sensitive USER ID is: %(user_id)s.

If you do not know or have forgotten your password, please use the 'Password Help' function on your site log in page: 

%(retrieve_pwd_url)s

In your review, please answer all questions. On the review page, there is a space for "Comments to Editor" and a space for "Comments to the Author." 
Please be sure to put your constructive comments to the author in the appropriate space.

All communications regarding this manuscript are confidential.  Any conflict of interest, suspicion of duplicate publication, fabrication of data or plagiarism must immediately be reported to me.

Thank you for reviewing this manuscript.

Sincerely,

Editor
%(actor_name)s
"""
DUE_REMINDER_PR_REVIEWER_SUBJECT = """%(journal)s: due reminder """
DUE_REMINDER_PR_REVIEWER_MAIL = """Dear %(to_name)s,

Recently, you agreed to review the paper 

ID:    %(submission_id)s
Title: '%(manuscript_title)s'
For   :%(journal)s .

Unfortunately, I did not receive your review until the deadline of %(deadline)s. The review is now due for %(days_due)s days. Therefore, I would be very glad if you could now deliver your review of the paper as soon as possible. Thank you very much.

To access the paper, login to BuR – Business Research website at 

%(manuscript_url)s

Your case-sensitive USER ID is: %(user_id)s.

If you do not know or have forgotten your password, please use the 'Password Help' function on your site log in page: 

%(retrieve_pwd_url)s

In your review, please answer all questions. On the review page, there is a space for "Comments to Editor" and a space for "Comments to the Author." 
Please be sure to put your constructive comments to the author in the appropriate space.

All communications regarding this manuscript are confidential. Any conflict of interest, suspicion of duplicate publication, fabrication of data or plagiarism must immediately be reported to me.

Thank you for reviewing this manuscript.
Sincerly,
%(actor_name)s"""

DEADLINE_REMINDER_PR_SECTIONEDITOR_SUBJECT = """%(journal)s: deadline reminder """
DEADLINE_REMINDER_PR_SECTIONEDITOR_MAIL = """Dear %(to_name)s,

The paper

ID:    %(submission_id)s
Title: '%(manuscript_title)s'
For:   %(journal)s .

has been submitted on %(date_submitted)s. We are approaching the promised period of decision within %(max_review_time)s days. Please, make sure that you reach a decision within this promised period. The deadline for your decision is %(decision_deadline)s. 

Sincerely,
Editor-in-chief"""


DUE_REMINDER_PR_SECTIONEDITOR_SUBJECT = """%(journal)s: due reminder """
DUE_REMINDER_PR_SECTIONEDITOR_MAIL = """Dear %(to_name)s,

The paper 

ID:    %(submission_id)s
Title: '%(manuscript_title)s'
Url:   %(manuscript_url)s .

has been submitted on %(date_submitted)s. Unfortunately, you have not reached a decision within the promised period of %(max_review_time)s days. Therefore, I would be very glad if you could come up with your decision immediately, even without sufficient information from reviewers. We need to keep our promise! 

Sincerly,
%(actor_name)s"""

REJECT_PR_AUTHOR_SUBJECT = """%(journal)s: Your manuscript is rejected"""
REJECT_PR_AUTHOR_MAIL = """Dear %(to_name)s,
The review for your paper 

ID:    %(submission_id)s    
Title: '%(manuscript_title)s'
For:    %(journal)s

is now completed. The manuscript was reviewed by a panel of two knowledgeable reviewers. In addition I read the paper carefully myself. Unfortunately we do not have good news. The reviewers have identified major problems with the paper, and my own reading confirms their objections. Based on their arguments, we will not be able to publish your paper in %(journal)s.

[GRUND]

I hope that the reviewers’ comments will be helpful to you in developing this work for submission to another journal. I am sorry that we cannot publish this paper, but I invite you to submit your future research to BuR – Business Research.

Sincerely,
%(actor_name)s """

REJECT_PR_REVIEWER_SUBJECT = """%(journal)s: The manuscript is rejected"""
REJECT_PR_REVIEWER_MAIL = """Dear %(to_name)s,

The review and evaluation of the following manuscript are now complete.

ID:    %(submission_id)s    
Title: '%(manuscript_title)s'
For:    %(journal)s

Since you were one of the reviewers of this paper, I want to take this opportunity to inform you about the outcome. As you can see from the decision letter I have decided to reject the paper.

To access the decision letter and the reviews, please login to BuR – Business Research website at:

%(manuscript_url)s

I am thankful to you for your timely and thorough review of the manuscript.  I strongly believe that the constructive nature of your comments will be very helpful to the author(s) in significantly improving future drafts of the manuscript.

Thank you once again for sharing your valuable expertise. I am hopeful that with the continued cooperation and assistance of reviewers like you, who are committed to providing timely and constructive reviews to authors, %(journal)s will have a competitive edge in attracting outstanding manuscripts.

Sincerely,
%(actor_name)s """
ACCEPT_PR_AUTHOR_SUBJECT = """%(journal)s: Your manuscript is accepted"""
ACCEPT_PR_AUTHOR_MAIL = """Dear %(to_name)s,

The review for your paper 

ID:    %(submission_id)s    
Title: '%(manuscript_title)s'
For:    %(journal)s

is now completed. The manuscript was reviewed by a panel of two knowledgeable reviewers. In addition I read the paper carefully myself. The reviewers are very pleased about the excellent quality of your paper. Congratulations!

Therefore, I accept your paper for publication in %(journal)s.

Sincerely,
%(actor_name)s """

ACCEPT_PR_REVIEWER_SUBJECT = """%(journal)s: The manuscript is accepted"""
ACCEPT_PR_REVIEWER_MAIL = """Dear %(to_name)s,

The review and evaluation of the following manuscript are now complete.

ID:    %(submission_id)s    
Title: '%(manuscript_title)s'
For:    %(journal)s

Since you were one of the reviewers of this paper, I want to take this opportunity to inform you about the outcome. As you can see from the decision letter I have decided to accept the paper for publication.

To access the decision letter and the reviews, please login to BuR – Business Research website at:

%(manuscript_url)s

I am thankful to you for your timely and thorough review of the manuscript.  I strongly believe that the constructive nature of your comments will be very helpful to the author(s) in significantly improving future drafts of the manuscript.

Thank you once again for sharing your valuable expertise. I am hopeful that with the continued cooperation and assistance of reviewers like you, who are committed to providing timely and constructive reviews to authors, %(journal)s will have a competitive edge in attracting outstanding manuscripts.

Sincerely,
%(actor_name)s """
