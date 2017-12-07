import logging

' 子子模块 '

logger = logging.getLogger('main.mod.submod')
logger.info('logger of submod say something...')

def tst():
	logger.info('this is submod.tst()...')