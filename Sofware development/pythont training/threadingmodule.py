import threading
import queue

number_of_jobs=2; #handle to jobs
jobs_to_do=[1,2]; #jobs to do
queue=queue.Queue(); #create a queue object


def create_workers(): #function definition
    for _ in range(number_of_jobs): #infinite for loop
        t=threading.Thread(target=work); #create a thread object with a target of work(function)
        t.daemon=True; #stop when the program ends
        t.start(); #start thread

def work(): #function definition
    while True:
        x = queue.get();  # get value put into queue
        if x == 1:
            print('This is the first job\n');
        if x == 2:
            print('This is the second job\n');
    queue.task_done(); #end queue


def create_jobs(): #function definition
    for x in jobs_to_do:
        queue.put(x); #put x in queue
    queue.join(); #join the value together

if __name__=='__main__':
    create_workers(); #function call
    create_jobs(); #function call
