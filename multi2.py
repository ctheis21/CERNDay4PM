'''
Topics covered:
    Creation of Processes with parameters
    Process()
'''
import multiprocessing

def worker(num):
    """thread worker function"""
    print('Worker:', num)
    return

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        p.start()
