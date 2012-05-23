from Products.DiPP import HAS_PLONE30

# the event classes are kept in different modules for different Plone versions
# this is just a wrapper which allows the use the same subscriber for Plone 2.5.5 and 4.x
# not tested with Plone 3  

if HAS_PLONE30:
    #from zope.lifecycleevent.interfaces import IObjectModifiedEvent
    from Products.Archetypes.interfaces.event import IObjectModifiedEvent
else:
    from zope.app.event.interfaces import IObjectModifiedEvent
