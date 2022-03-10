'''
Topics covered:
    Terminating processes + Logging
    Process.daemon, Process.terminate()
'''
import multiprocessing
import time
import logging

def slow_worker():
    print('Starting worker')
    time.sleep(2)
    print('Exiting worker')

if __name__ == '__main__':

    multiprocessing.log_to_stderr(logging.DEBUG)

    p = multiprocessing.Process(target=slow_worker)
    print('BEFORE:', p, p.is_alive())

    p.start()
    print('DURING:', p, p.is_alive())

    p.terminate()
    print('TERMINATED:', p, p.is_alive())

    p.join()
    print('JOINED:', p, p.is_alive())
