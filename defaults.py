"""
$Id$
"""
WYSIWYG_EDITOR = "FCKeditor"

DEADLINE_MAX = 56
DEADLINE_DEFAULT = 14
DEADLINE_RED = 3
DEADLINE_YELLOW = 10

ALERT_EMAIL_ADDRESSES = ('dipp-tech@hbz-nrw.de',) 
ALERT_EMAIL_TEXT = """
Dear Ladies and Gentlemen,

The eJournal %(journal)s is pleased to inform you, that we have just published a new article.
The full text can be found here: %(url)s
"""
AUTHOR_NOTICE_DE = """
Sehr geehrte(r) %(fullname)s,

sie haben einen Artikel mit dem Titel "%(title)s" bei %(journal)s eingereicht.
Der Artikel ist nun zur Veröffentlichung vorbereitet und erfordert Ihr Imprimatur.  

Bitte loggen sie sich unter <%(next_step)s> auf unserer Webseite ein, überprüfen
den Artikel genau und geben anschließend ihr Urteil ab.

Frist: %(deadline)s
Ihr Login-Name: %(login)s

Mit freundichen Grüßen,
%(from)s
"""
AUTHOR_NOTICE_EN = """
Dear %(fullname)s,

you have submitted a paper with the title "%(title)s" to %(journal)s.
The paper is now ready for publication and requires your imprimatur.

Please log into our webssite under <%(next_step)s> carefully read the 
article and let us know your judgement.

Deadline: %(deadline)s
Your login name: %(login)s

Kind regards
%(from)s
"""
