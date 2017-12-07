#coding=utf-8
#!/usr/bin/python3
import logging;
import logging.handlers;

def initLogger(loggerName, loggerFile):
    # create a logger
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    # File Handler
    # fileHandler = logging.FileHandler(loggerFile)
    fileHandler = logging.handlers.RotatingFileHandler(loggerFile, maxBytes=1024 * 1024, backupCount=5)  # 实例化handler
    fileHandler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'));

    # File Handler
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'));

    # 给logger添加handler
    logger.addHandler(fileHandler);
    logger.addHandler(consoleHandler);

    return logger;
