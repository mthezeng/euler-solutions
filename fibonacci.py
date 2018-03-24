from memo import memo
from timer import timer

def fib_matrix(n):
    """iterative matrix multiplication"""
    def dot(m1, m2):
        #dot product of two 2x2 matrices
        f1 = m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]
        f2 = m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]
        f3 = m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]
        f4 = m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]
        return [[ f1, f2 ], [ f3, f4 ]]

    def matrix(n):
        assert n >= 0, 'n must be non-negative'
        f_origin = [[1,1],[1,0]]
        f = f_origin
        for i in range(n-1):
            f = dot(f,f_origin)
        return f

    return matrix(n)[0][1]

def fib_iter(n):
    """iterative list mutation"""
    assert n >= 0, 'n must be non-negative'
    f = [1, 1]
    if n <= 2:
        return 1
    else:
        for _ in range(n-2):
            f.append(f[1] + f.pop(0))
        return f[-1]

@memo
def fib_tree(n):
    """memoized tree recursion"""
    assert n >= 0, 'n must be non-negative'
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_tree(n-1) + fib_tree(n-2)

def test(n):
    print('iterative matrix multiplication ', end='')
    timer(fib_matrix, [n])

    print('iterative list mutation ', end='')
    timer(fib_iter, [n])

    print('memoized tree recursion ', end='')
    timer(fib_tree, [n])
