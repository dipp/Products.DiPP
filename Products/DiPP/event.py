from Products.DiPP import HAS_PLONE30

if HAS_PLONE30:
    from zope.lifecycleevent.interfaces import IObjectModifiedEvent
else:
    from zope.app.event.interfaces import IObjectModifiedEvent