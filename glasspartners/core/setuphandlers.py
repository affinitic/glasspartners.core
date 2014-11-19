# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger('glasspartners.core')


def installCore(context):
    if context.readDataFile('glasspartners.core-default.txt') is None:
        return

    logger.info('Installing glasspartners.core')
