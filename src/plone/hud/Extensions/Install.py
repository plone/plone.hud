# -*- coding: utf-8 -*-
from plone.hud.interfaces import IHUDSettings
from plone.registry.interfaces import IRegistry
from Products.CMFCore.utils import getToolByName
from StringIO import StringIO
from zope.component import getUtility


PROJECTNAME = 'plone.hud'

# Configlets to be added to control panels or removed from them
configlets = ({
    'id': 'MyProductSetup',
    'name': 'My Product',
    'action': 'string:${portal_url}/hud_settings',
    'condition': '',
    'category': 'Products',
    'visible': 1,
    'appId': PROJECTNAME,
    'permission': 'ManagePortal',
    'imageUrl': ''
},)


def install(self):
    out = StringIO()

    registry = getUtility(IRegistry)
    registry.registerInterface(IHUDSettings)

    # add the configlets to the portal control panel
    configTool = getToolByName(self, 'portal_controlpanel', None)
    if configTool:
        for conf in configlets:
            configTool.registerConfiglet(**conf)
            out.write('Added configlet %s\n' % conf['id'])

    print >> out, "Successfully installed %s." % PROJECTNAME
    return out.getvalue()


def uninstall(self):
    out = StringIO()

    # remove the configlets from the portal control panel
    configTool = getToolByName(self, 'portal_controlpanel', None)
    if configTool:
        for conf in configlets:
            configTool.unregisterConfiglet(conf['id'])
            out.write('Removed configlet %s\n' % conf['id'])

    print >> out, "Successfully uninstalled %s." % PROJECTNAME
    return out.getvalue()
