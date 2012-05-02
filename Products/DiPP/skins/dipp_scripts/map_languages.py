## Script (Python) "map_languages"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=lang
##title=
##

# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from Products.PythonScripts.PythonScript import DateTime

map = {
    'ger': 'Deutsch',
    'eng': 'English',
    'fra': 'Français',
}
try:
    return map[lang]
except:
    return lang
