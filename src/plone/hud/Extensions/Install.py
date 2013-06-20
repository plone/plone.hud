# -*- coding: utf-8 -*-
from plone import api
from plone.hud import conf
from plone.hud.interfaces import IHUDSettings
from plone.registry.interfaces import IRegistry
from StringIO import StringIO
from zope.component import getUtility


# Configlets to be added to control panels or removed from them
configlets = ({
    'id': conf.SETTINGS_ID,
    'name': conf.SETTINGS_LABEL,
    'action': 'string:${{portal_url}}/{0}'.format(conf.SETTINGS_ID),
    'condition': '',
    'category': conf.CONFIGLET_CATEGORY,
    'visible': 1,
    'appId': conf.PROJECT_NAME,
    'permission': 'ManagePortal',
    'imageUrl': ''
},)


def install(self):
    out = StringIO()

    registry = getUtility(IRegistry)
    registry.registerInterface(IHUDSettings)

    # add the configlets to the portal control panel
    config_tool = api.portal.get_tool(name='portal_controlpanel')
    if config_tool:
        for configlet in configlets:
            config_tool.registerConfiglet(**configlet)
            out.write('Added configlet %s\n' % configlet['id'])

    print >> out, "Successfully installed %s." % conf.PROJECT_NAME
    return out.getvalue()


def uninstall(self):
    out = StringIO()

    # remove the configlets from the portal control panel
    config_tool = api.portal.get_tool(name='portal_controlpanel')
    if config_tool:
        for configlet in configlets:
            config_tool.unregisterConfiglet(configlet['id'])
            out.write('Removed configlet %s\n' % configlet['id'])

    print >> out, "Successfully uninstalled %s." % conf.PROJECT_NAME
    return out.getvalue()
