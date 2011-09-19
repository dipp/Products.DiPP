## Script (Python) "sortedSubjectsClassified"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=subjects
##title=
##

# groups the subjects by system. from fedora we get an unsorted dictionary
request     = container.REQUEST
RESPONSE    = request.RESPONSE

systems = {}
for subject in subjects:
    system = subject['classificationSystem']
    if system != '':
        if not systems.has_key(system):
            systems[system] = []
        systems[system].append((subject['classificationIdent'], subject['subjectClassified']))
return systems
