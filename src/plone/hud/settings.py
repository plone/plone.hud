# -*- coding: utf-8 -*-
"""Global HUD settings view."""

from Products.Five.browser import BrowserView
from plone import api
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.hud.misc import CONFIGLET_CATEGORY
from plone.hud.misc import SETTINGS_LABEL
from plone.z3cform import layout
from z3c.form import field
from z3c.form import form
from zope.interface import alsoProvides
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary

import zope


def panels_source(context):
    """Returns all panels in the SimpleVocabulary object."""
    portal_controlpanel = api.portal.get_tool(name='portal_controlpanel')
    configlets = portal_controlpanel.enumConfiglets(
        group=CONFIGLET_CATEGORY
    )
    titles = [c['title'] for c in configlets]
    result = SimpleVocabulary.fromValues(titles)
    return result

alsoProvides(panels_source, IContextSourceBinder)


class HUDSettingsEditForm(form.EditForm):
    """
    Define form logic
    """
    label = SETTINGS_LABEL

    hud_panel = zope.schema.Choice(
        title=u"HUD Panel",
        source=panels_source,
        default=SimpleVocabulary.fromValues(["None"])
    )
    hud_panel.__name__ = 'hud_panel'

    fields = field.Fields(hud_panel)


class HUDSettingsView(BrowserView):
    """
    View which wrap the settings form using ControlPanelFormWrapper
    to a HTML boilerplate frame.
    """

    def render(self):
        view_factor = layout.wrap_form(
            HUDSettingsEditForm, ControlPanelFormWrapper
        )
        view = view_factor(self.context, self.request)
        return view()

    def __call__(self):
        return self.render()
