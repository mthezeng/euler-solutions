import time
# import progressbar

def timer(f, args=[]):
    start_time = time.time()
    f(*args)
    end_time = time.time() - start_time
    print('time:', end_time)
    return end_time
