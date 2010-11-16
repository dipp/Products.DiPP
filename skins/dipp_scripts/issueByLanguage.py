## Script (Python) "issueByLanguage"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##

request     = container.REQUEST
RESPONSE    = request.RESPONSE

issues = {}
results = container.portal_catalog(portal_type=('FedoraHierarchie','Issue','Volume'), Language='all', sort_on='Date', sort_order='reverse')

for item in results:
    lang = item['Language']
    if lang == '':
        lang = 'neutral'
    if not lang in issues.keys():
        issues[lang] = []
    issues[lang].append(item)
return issues
