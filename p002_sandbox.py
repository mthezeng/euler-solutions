from fibonacci import fibonacci

def dot(m1, m2):
    #dot product of two 2x2 matrices
    f1 = m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]
    f2 = m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]
    f3 = m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]
    f4 = m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]
    return [[ f1, f2 ], [ f3, f4 ]]

def fibonacci_matrix(n):
    # returns the nth fibonacci number
    f_origin = [[1,1],[1,0]]
    f = f_origin
    for i in range(n-1):
        f = dot(f,f_origin)
    return f

def fibonacci(n):
    return fibonacci_matrix(n)[0][1]

def even_fibs(value):
    s = 0
    i = 1
    current_fib = fibonacci(i)
    while current_fib < value:
        if current_fib % 2 == 0:
           s += current_fib
        current_fib = fibonacci(i)
        i += 1
    print(s)

# def even_fibs(value):
#     s = 0
#     f_origin = [[1,1],[1,0]]
#     matrix = f_origin[:]
#     current_fib = matrix[0][0]
#     while current_fib < value:
#         if current_fib % 2 == 0:
#             s = s + current_fib
#         matrix = dot(matrix, f_origin)
#         current_fib = matrix[0][0]
#     return s


#########

def last_in_cache(n, cache):
    last_i = cache[0]
    for i in cache.keys():
        if i < n:
            last_i = cache[i]
        else:
            break
    return last_i

def memo(f):
    cache = {0: (0, [[1,1],[1,0]])}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n, last_in_cache(n, cache))
        return cache[n][0]
    return memoized

@memo
def even_fibs(value, last):
    s, matrix = last
    f_origin = [[1,1],[1,0]]
    current_fib = matrix[0][0]
    while current_fib < value:
        if current_fib % 2 == 0:
            s = s + current_fib
        matrix = dot(matrix, f_origin)
        current_fib = matrix[0][0]
    return (s, matrix)
