# -*- coding: utf-8 -*-
"""HUD panel view to be extended by individual panels."""

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from plone.hud.misc import CONFIGLET_CATEGORY


class HUDPanelView(BrowserView):
    main_template = ViewPageTemplateFile('templates/panel.pt')

    def render(self):
        return self.main_template()

    def __call__(self):
        return self.render()

    def render_panel(self):
        return None

    def list_panels(self):
        """Returns all panels in the list."""
        portal_controlpanel = api.portal.get_tool(name='portal_controlpanel')
        configlets = portal_controlpanel.enumConfiglets(
            group=CONFIGLET_CATEGORY
        )
        portal_url = api.portal.get().absolute_url()
        result = []
        for configlet in configlets:
            path = self._get_traversable_path(portal_url, configlet["url"])
            result += [(configlet["title"], path)]
        return result

    def _get_traversable_path(self, portal_url, portlet_url):
        return "hud" + portlet_url[len(portal_url):]
