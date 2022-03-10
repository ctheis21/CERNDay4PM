'''
Topics covered:
    Joining processes
    Process.daemon, join()
'''
import multiprocessing
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(processName)-10s) %(message)s',
                    )

def daemon():
    logging.debug('Starting: %s', multiprocessing.current_process().name)
    time.sleep(10)
    logging.debug('Exiting')

def non_daemon():
    logging.debug('Starting: %s', multiprocessing.current_process().name)

    logging.debug('Exiting')

if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True

    n = multiprocessing.Process(name='non-daemon', target=non_daemon)
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()

    d.join()
    n.join()