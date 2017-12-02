import time

def timer(f, args=[]):
    """
    Calculate the runtime of a function
    params:
        f: callable. function whose runtime is to be measured
        args: list. optional parameters to be passed into f
    returns:
        end_time: float. the runtime of f
    NOTE: currently it is better if f itself prints its output
    """
    start_time = time.time()
    f(*args)
    end_time = time.time() - start_time
    print('time:', end_time)
    return end_time
