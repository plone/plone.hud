# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone import api
from plone.hud.misc import CONFIGLET_CATEGORY
from plone.hud.misc import PREFIX
from plone.hud.misc import normalize_name
from zope import schema
from zope.interface import Interface
from zope.interface import alsoProvides
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary


class IPloneHudLayer(Interface):
    """ A layer specific for this add-on product.

    This interface is referred in browserlayer.xml.

    All views and viewlets register against this layer will appear on
    your Plone site only when the add-on installer has been run.
    """


def panels_source(context):
    """Returns all panels in the SimpleVocabulary object."""
    portal_controlpanel = api.portal.get_tool(name='portal_controlpanel')
    configlets = portal_controlpanel.enumConfiglets(
        group=CONFIGLET_CATEGORY
    )
    prefix = normalize_name(PREFIX + '_')

    titles = [c['title'] for c in configlets
              if c['id'].startswith(prefix)]

    result = SimpleVocabulary.fromValues(titles)
    return result

alsoProvides(panels_source, IContextSourceBinder)


class IHUDSettings(Interface):
    """ Define settings data structure """

    hud_panel = schema.Choice(
        title=u"{0} Panel".format(PREFIX),
        source=panels_source
    )
