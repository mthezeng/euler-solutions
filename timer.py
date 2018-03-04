import time

def timer(f, args=[], suppress_print=False):
    """
    Calculate the runtime of a function
    params:
        f: callable. function whose runtime is to be measured
        args: list. optional parameters to be passed into f
        suppress_print: optional. will not print runtime if True (still returned).
    returns:
        result: return value of f called on args
        end_time: float. the runtime of f called on args.
    """
    start_time = time.time()
    result = f(*args)
    end_time = time.time() - start_time
    if not suppress_print:
        print('time:', end_time)
    return result, end_time

def timed(fn):
    """
    Decorator which applies the timer function above.
    params:
        fn: the function whose runtime is to be measured.
    returns:
        timed_func: a function which first prints the runtime of fn, then returns its output
    """
    def timed_func(*args):
        output, time = timer(fn, [*args], True)
        print('time:', time)
        return output
    return timed_func
