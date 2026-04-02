import time

def performanceTracker(func):
    def wrapper():
        start=time.time()
        func()
        end=time.time()
        print("Execution Time: ",end-start,"seconds")
    return wrapper
@performanceTracker
def task1():
    print("task 1 is running")
    time.sleep(2)

@performanceTracker
def task2():
    print("task 2 is running")
    time.sleep(1)

task1()
task2()