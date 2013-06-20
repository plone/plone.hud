# -*- coding: utf-8 -*-
from plone.hud import get_panel_id
from plone.hud import get_panel_label


PROJECT_NAME = 'plone.hud'
PREFIX = 'HUD'
CONFIGLET_CATEGORY = 'Products'
SETTINGS_NAME = 'Settings'
SETTINGS_ID = get_panel_id(SETTINGS_NAME)
SETTINGS_LABEL = get_panel_label(SETTINGS_NAME)
