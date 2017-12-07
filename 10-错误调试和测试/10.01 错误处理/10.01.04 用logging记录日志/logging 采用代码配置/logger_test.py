#coding=utf-8
#!/usr/bin/python
import logging;
import logger_initiator;
# 每次会追加
logger = logger_initiator.initLogger('test_logger', './test_logger.log');

logger.debug('This is debug log 4 test1.');
logger.info('This is info log 4 test1.');
logger.warning('This is warning log 4 test1.');
logger.error('This is error log 4 test1.');
logger.critical('This is critical log 4 test1.');
# logger.exception('This is exception log 4 test1.')