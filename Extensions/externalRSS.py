import feedparser

def externalRSS(url):
    rss = feedparser.parse(url)
    return rss.entries
