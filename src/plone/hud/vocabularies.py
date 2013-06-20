# -*- coding: utf-8 -*-
from five import grok
from plone import api
from plone.hud import conf
from plone.hud import normalize_name
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


class HUDPanelsVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        portal_controlpanel = api.portal.get_tool(name='portal_controlpanel')
        configlets = portal_controlpanel.enumConfiglets(
            group=conf.CONFIGLET_CATEGORY
        )
        prefix = normalize_name(conf.PREFIX + '_')

        titles = [c['title'] for c in configlets
                  if c['id'].startswith(prefix)]

        result = SimpleVocabulary.fromValues(titles)
        return result

grok.global_utility(
    HUDPanelsVocabulary,
    name="plone.hud.panels_vocabulary",
)
