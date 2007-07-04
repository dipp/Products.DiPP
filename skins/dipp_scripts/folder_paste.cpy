## Controller Python Script "folder_paste"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=self
##title=Paste objects into a folder
##

from AccessControl import Unauthorized
from ZODB.POSException import ConflictError
from Products.CMFCore.utils import getToolByName

request = container.REQUEST
RESPONSE =  request.RESPONSE

fedora = getToolByName(self, 'fedora')

msg='Copy or cut one or more items to paste.' 

if context.cb_dataValid:
    clipboard = context.REQUEST['__cp']
    try:
        # move in fedora
        try:
            dest = self.PID
            fedora.moveObjects(clipboard,dest)
        except:
            pass
        # move in Plone
        context.manage_pasteObjects(clipboard)
        from Products.CMFPlone import transaction_note
        transaction_note('Pasted content to %s' % (context.absolute_url()))

        return state.set(portal_status_message='Item(s) pasted.')
    except ConflictError:
        raise
    except ValueError:
        msg="Disallowed to paste item(s)."
    except (Unauthorized, 'Unauthorized'):
        msg="Unauthorized to paste item(s)."
    except: # fallback
        msg='Paste could not find clipboard content.'

return state.set(status='failure', portal_status_message=msg)

