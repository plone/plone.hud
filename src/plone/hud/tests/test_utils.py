# -*- coding: utf-8 -*-
from plone.hud import normalize_name

import unittest2


class TestUtils(unittest2.TestCase):

    def test_normalize_name(self):
        self.assertEqual(
            normalize_name("HUD Users Panel"),
            "hud_users_panel"
        )
        self.assertEqual(
            normalize_name("HUD_Users_Panel"),
            "hud_users_panel"
        )
