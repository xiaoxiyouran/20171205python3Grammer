import logging
import logging.config # 正则表达式是r'^[(.*)]$',从而匹配出所有的组件。对于同一个组件具有多个实例的情况使用逗号‘，’进行分隔。对于一个实例的配置采用componentName_instanceName配置块。

logging.config.fileConfig("logging.conf")    # 采用配置文件

# create logger
logger = logging.getLogger("simpleExample")

# "application" code
logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")