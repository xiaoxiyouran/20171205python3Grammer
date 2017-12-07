import logging
import submod

' 子模块 '
logger = logging.getLogger('main.mod')
logger.info('logger of mod say something...')

def testLogger():
	logger.debug('this is mod.testLogger...')
	submod.tst()