#!/usr/bin/python

from multiprocessing import Process,Pool,Queue
import os,time,random

print 'starting multiprocesssing'

pid = os.fork()
if pid == 0:
	print 'I\'m a child process %s and my parent is %s' % (os.getpid(),os.getppid())
else:
	print 'I\'m a parent process %s and my child is %s' % (os.getpid(),pid)

# when we call fork(), the parent process makes a duplicate of itself and passes to the child
# process, fork returns the child id for the parent procss and 0 for the child process
# however, the child process has it's unique id

# this is why we use processing instead of threading in webserver's because unlike
# threading (which the thread does not have a unique idnetity) process can differiantiate
# from each other
 

def run_proc(name):
	print 'Run child process %s (%s)...' % (name, os.getpid())

print 'create child'
p = Process(target=run_proc,args=('test',))
print 'start child process'
p.start()
p.join()
print 'End process %s' % os.getpid()
# printed twice, parent runs once, child runs once

# a Pool can be used if you want to create multiple processes
def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool(5)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'

# a quue is used to communicate between processes
def write(q):
	for value in ['A','B','C']:
		print 'put',value,'into Queue'
		q.put(value)
		time.sleep(random.random())
def read(q):
	while True:
		print 'get',q.get(True),'from queue'

if __name__ == '__main__':
	q = Queue()
	pw = Process(target=write,args=(q,))
	pr = Process(target=read,args=(q,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()


