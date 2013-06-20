# -*- coding: utf-8 -*-

CONFIGLET_CATEGORY = 'Products'
PREFIX = 'HUD'
PROJECT_NAME = 'plone.hud'
SETTINGS_NAME = 'Settings'


def normalize_name(name):
    result = ""
    for c in name:
        if c in [chr(32), '_']:
            c = '_'
        elif not str.isalnum(c):
            continue
        result += c
    return result.lower()


def get_panel_id(name):
    return normalize_name("{0}_{1}".format(PREFIX, name))

SETTINGS_ID = get_panel_id(SETTINGS_NAME)


def get_panel_label(name):
    return "{0} {1}".format(PREFIX, name)

SETTINGS_LABEL = get_panel_label(SETTINGS_NAME)
