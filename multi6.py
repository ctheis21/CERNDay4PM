'''
Topics covered:
    Joining processes
    Process.daemon, Process.join(), Process.isAlive()
'''
import multiprocessing
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(processName)-10s) %(message)s',
                    )

def daemon():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')

if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True

    n = multiprocessing.Process(name='non-daemon', target=non_daemon)
    n.daemon = False

    d.start()
    n.start()

    d.join(1)
    logging.debug('d.is_alive() is %s', d.is_alive())
    n.join()

    d.join()
    n.join()