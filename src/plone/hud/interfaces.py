# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.theme.interfaces import IDefaultPloneLayer
from zope import schema
from zope.interface import Interface


class IPloneHudLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer."""


class IHUDSettings(Interface):
    """ Define settings data structure """

    adminLanguage = schema.TextLine(
        title=u"Admin language",
        default=u"EN"
    )
