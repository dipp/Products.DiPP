## Script (Python) "get_article_toc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self
##title=
##
request = container.REQUEST
RESPONSE =  request.RESPONSE

def get_article_obj(object):
    """check wether the calling object or it's parent is an article"""
    
    if object.portal_type == "FedoraArticle":
        return object

    elif object.portal_type != "Plone Site":
        parent = object.getParentNode()
        if parent.portal_type == "FedoraArticle":
            return parent
        else:
            return None
    else:
        return None

article = get_article_obj(self)

if article:
    if hasattr(article, 'toc'):
        return getattr(article,'toc')
    else:
        return None
else:
    return None
