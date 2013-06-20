# -*- coding: utf-8 -*-
from five import grok
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.hud.interfaces import IHUDSettings
from plone.hud.misc import SETTINGS_ID
from plone.hud.misc import SETTINGS_LABEL
from plone.z3cform import layout
from Products.CMFCore.interfaces import ISiteRoot


class HUDSettingsEditForm(RegistryEditForm):
    """
    Define form logic
    """
    schema = IHUDSettings
    label = SETTINGS_LABEL


class HUDSettingsView(grok.CodeView):
    """
    View which wrap the settings form using ControlPanelFormWrapper
    to a HTML boilerplate frame.
    """
    grok.name(SETTINGS_ID)
    grok.context(ISiteRoot)

    def render(self):
        view_factor = layout.wrap_form(
            HUDSettingsEditForm, ControlPanelFormWrapper
        )
        view = view_factor(self.context, self.request)
        return view()
