import logging.handlers


def getLoger(name):
    logger = logging.getLogger(str(name))
    logger.setLevel(level=logging.INFO)
    handler = logging.handlers.TimedRotatingFileHandler('./log/' + str(name), 'H', backupCount=3, interval=1,encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger