# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.hud.interfaces import IHUDSettings
from plone.hud.misc import SETTINGS_LABEL
from plone.z3cform import layout


class HUDSettingsEditForm(RegistryEditForm):
    """
    Define form logic
    """
    schema = IHUDSettings
    label = SETTINGS_LABEL


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
