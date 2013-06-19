# -*- coding: utf-8 -*-
from five import grok
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout
from Products.CMFCore.interfaces import ISiteRoot
from plone.hud.interfaces import IHUDSettings


class HUDSettingsEditForm(RegistryEditForm):
    """
    Define form logic
    """
    schema = IHUDSettings
    label = u"HUD settings"


class HUDSettingsView(grok.CodeView):
    """
    View which wrap the settings form using ControlPanelFormWrapper
    to a HTML boilerplate frame.
    """
    grok.name("hud_settings")
    grok.context(ISiteRoot)

    def render(self):
        view_factor = layout.wrap_form(
            HUDSettingsEditForm, ControlPanelFormWrapper
        )
        view = view_factor(self.context, self.request)
        return view()
