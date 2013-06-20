# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.hud.misc import PREFIX
from plone.theme.interfaces import IDefaultPloneLayer
from zope import schema
from zope.interface import Interface


class IPloneHudLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer."""


class IHUDSettings(Interface):
    """ Define settings data structure """

    hud_panel = schema.Choice(
        title=u"{0} Panel".format(PREFIX),
        vocabulary="plone.hud.panels_vocabulary"
    )
