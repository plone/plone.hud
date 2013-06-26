# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.hud.misc import PREFIX
from zope import schema
from zope.interface import Interface


class IPloneHudLayer(Interface):
    """ A layer specific for this add-on product.

    This interface is referred in browserlayer.xml.

    All views and viewlets register against this layer will appear on
    your Plone site only when the add-on installer has been run.
    """


class IHUDSettings(Interface):
    """ Define settings data structure """

    hud_panel = schema.Choice(
        title=u"{0} Panel".format(PREFIX),
        vocabulary="plone.hud.panels_vocabulary"
    )
