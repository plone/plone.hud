# -*- coding: utf-8 -*-
"""Init and utils."""

from plone import api
from plone.hud import conf
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('plone.hud')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""


def normalize_name(name):
    result = ""
    for c in name:
        if c in [chr(32), '_']:
            c = '_'
        elif not str.isalnum(c):
            continue
        result += c
    return result.lower()


def get_panel_id(name):
    return normalize_name("{0}_{1}".format(conf.PREFIX, name))


def get_panel_label(name):
    return "{0} {1}".format(conf.PREFIX, name)


def register_hud_panel(name):
    config_tool = api.portal.get_tool(name='portal_controlpanel')

    if not config_tool:
        return None

    configlet_id = get_panel_id(name)
    configlet_label = get_panel_label(name)
    configlet = {
        'id': configlet_id,
        'name': configlet_label,
        'action': 'string:${{portal_url}}/{0}'.format(configlet_id),
        'condition': '',
        'category': conf.CONFIGLET_CATEGORY,
        'visible': 1,
        'appId': conf.PROJECT_NAME,
        'permission': 'ManagePortal',
        'imageUrl': ''
    }

    config_tool.registerConfiglet(**configlet)

    return configlet_id


def unregister_hud_panel(name):
    config_tool = api.portal.get_tool(name='portal_controlpanel')

    if not config_tool:
        return None

    configlet_id = get_panel_id(name)

    config_tool.unregisterConfiglet(configlet_id)

    return configlet_id
