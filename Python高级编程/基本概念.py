import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
logging.error('This is error message')
logging.critical('This is critical message')