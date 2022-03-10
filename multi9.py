'''
Topics covered:
    Logger: get_logger(), log_to_stderr()
'''
import multiprocessing
import logging


def worker():
    log=multiprocessing.get_logger()
    log.info('Doing some work')

if __name__ == '__main__':
    multiprocessing.log_to_stderr(logging.DEBUG)
    logger=multiprocessing.get_logger()
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()
