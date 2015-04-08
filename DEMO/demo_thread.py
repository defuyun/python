#!/usr/bin/python

# python uses posix thread to perform threading, therefore the threading is not simulated
import time,threading

def loop():
	print 'running',threading.current_thread().name

t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()

# the difference between threading and process is that all vars are shared between thread
# so we need a lock to prevent both thread from accessing the same var at the same time

balance = 0

def change_balance(n):
	global balance
	balance += n
	balance -= n

def run_thread():
	for i in range(10000):
		change_balance(i)

t1 = threading.Thread(target=run_thread)
t2 = threading.Thread(target=run_thread)

t1.start()
t2.start()

t1.join()
t2.join()

print balance # 4410

# balance += n is balance = balance + n
# at first balance = 0
# if t1 n = 5, then
# balance = 0 + 5 
# but if at the same time t2 n = 8 and is also called
# then balance = 0 + 8
# if t1 finishes second than balance = 5
# then we run balance = balance - n 
# if t2 finishes second (t2 n = 8) then what we have is -3
# therefore if we don't control the process, things will go wrong
# that's why we have a lock

balance = 0
lock = threading.Lock()

def run_thread():
	for i in range(10000):
		lock.acquire()
		change_balance(i)
		lock.release()

t3 = threading.Thread(target=run_thread)
t4 = threading.Thread(target=run_thread)

t3.start()
t4.start()

t3.join()
t4.join()

print balance # 0

# python has a GIL lock that is created by ther interpolator, whenever a thread tries to 
# load, it must acquire a GIL lock. and whenver it runs over 100 byte of code, the lock
# is released and given to other threads. Python does not really create multi-threading environment
# even if you have multi-core because the GIL lock would always limit to 1 thread running

local_school = threading.local()

def process_student():
	print local_school.name, threading.current_thread().name

def process_thread(name):
	# bind name to process_thread, from this point anything called by process_thread
	# shares the local_school.name variable

	# the local_school is like a dict with key = current_thread().name + attribute
	local_school.name = name
	process_student()

t1 = threading.Thread(target=process_thread,args=('Alice',),name='Thread _ Alice')
t2 = threading.Thread(target=process_thread,args=('Beta',),name='Thread _ Beta')

t1.start()
t2.start()

t1.join()
t2.join()

process_thread('Hi')
