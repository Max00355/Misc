import thread

global found
global threadsLeft
found = False
threadsLeft = 0

def sequentialSearch(value, array):
    global found
    global threadsLeft
    for v in array:
        if found:
            break
        if v == value:
            found = v
    threadsLeft -= 1

def search(value, array, threads=10):
    global threadsLeft
    global found
    if len(array) <= threads:
        for v in array:
            thread.start_new_thread(sequentialSearch, (value, [v]))
    else:
        ranges = len(array) / threads
        extra = len(array) % threads
        pev = 0
        nex = ranges
        for v in xrange(threads):
            thread.start_new_thread(sequentialSearch, (value, array[prev:nex]))
            threadsLeft += 1
            prev = nex 
            nex = ranges * (v + 1)
        


