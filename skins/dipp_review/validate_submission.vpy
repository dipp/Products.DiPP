## Controller Validator "validate_submit"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters= title='', manuscript_abstract="", manuscript_authors='', manuscript_file='', section='', agb=""
##title=Validates the contact form
##

if not title:
    state.setError('title', 'Please provide the title of your manuscript.', 'input_required')

if not section:
    state.setError('section', 'Please choose a section.', 'input_required')

if not manuscript_authors:
    state.setError('manuscript_authors', 'Please give at least one author.', 'input_required')

if not manuscript_abstract:
    state.setError('manuscript_abstract', 'Please provide an abstract.', 'input_required')

if not agb:
    state.setError('agb', 'Please agree to the Terms and Conditions.', 'input_required')

if state.getErrors():
    return state.set(status='failure', portal_status_message='Please correct the indicated errors.')

else:
    return state

