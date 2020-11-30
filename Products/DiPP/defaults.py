# -*- coding: utf-8 -*-

DEFAULT_LANGUAGE = 'eng'
AVAILABLE_LANGUAGES = ('ger', 'eng', 'fra', 'ita', 'spa')

WYSIWYG_EDITOR = "FCKeditor"

DEADLINE_MAX = 56
DEADLINE_DEFAULT = 14
DEADLINE_RED = 3
DEADLINE_YELLOW = 10

CITATION_FORMAT = "%(authors)s (%(year)s). %(title)s. %(journal)s, Vol. %(volume)s. (%(urn)s)"
ISSUE_DATE_FORMAT = "%b %Y"
SHORT_CITATION_FORMAT = "%(journal)s, Vol. %(volume)s, Iss. %(issue)s"

ALERT_EMAIL_ADDRESSES = ('dipp@hbz-nrw.de',)
ALERT_EMAIL_TEXT = """
Das Journal "%(journal)s" hat einen neuen Artikel veröffentlicht:
%(citation)s

URL: %(url)s
DataCite XML: %(url)s/metadata/datacite
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

ANALYTICS_JAVASCRIPT = """
var _paq = window._paq = window._paq || [];
/* tracker methods like "setCustomDimension" should be called before "trackPageView" */
_paq.push(['trackPageView']);
_paq.push(['enableLinkTracking']);
(function() {
    var u="//%s/";
    _paq.push(['setTrackerUrl', u+'matomo.php']);
    _paq.push(['setSiteId', '%s']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.type='text/javascript'; g.async=true; g.src=u+'matomo.js'; s.parentNode.insertBefore(g,s);
})();
"""
ANALYTICS_JAVASCRIPT_NOTFOUND = """
var _paq = window._paq = window._paq || [];
/* tracker methods like "setCustomDimension" should be called before "trackPageView" */
_paq.push(['setDocumentTitle',  '404/URL = ' +  encodeURIComponent(document.location.pathname+document.location.search) + '/From = ' + encodeURIComponent(document.referrer)]);
_paq.push(['trackPageView']);
_paq.push(['enableLinkTracking']);
(function() {
    var u="//%s/";
    _paq.push(['setTrackerUrl', u+'matomo.php']);
    _paq.push(['setSiteId', '%s']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.type='text/javascript'; g.async=true; g.src=u+'matomo.js'; s.parentNode.insertBefore(g,s);
})();
"""
