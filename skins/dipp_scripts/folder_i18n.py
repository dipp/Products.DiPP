## Script (Python) "folder_i18n"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self,lang,sibling_title
##title=
##
user_lang = lang
request = container.REQUEST
RESPONSE =  request.RESPONSE

I18N  = 'i18n.txt'

try:
    x     = getattr(self,I18N)
    lines = x.data.splitlines()
    words = {}

    for line in lines:
        langs = line.split(';')
        id = langs[0].split(':')[1]
        words[id] = {}
        for lang in langs:
            #in case someone puts a trailing ';', which causes an emty element
            try:
                lang = lang.split(':')
                l = lang[0].strip()
                v = lang[1].strip()
                words[id][l] = v 
            except:
                pass

    if words.has_key(sibling_title):
        return words[sibling_title][user_lang]
        #return user_lang
    else:
        return sibling_title

except:
    return sibling_title
    
