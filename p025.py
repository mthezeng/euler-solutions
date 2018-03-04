from timer import timed

def dot(m1, m2):
    #dot product of two 2x2 matrices
    #workaround solution for numpy's max integer size
    f1 = m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]
    f2 = m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]
    f3 = m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]
    f4 = m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]
    return [[ f1, f2 ], [ f3, f4 ]]

@timed
def fibonacci_matrix(n):
    f_origin = [[1,1],[1,0]]
    f = f_origin
    counter = 2
    while True:
        f = dot(f,f_origin)
        cur = str(f[0][1])
        if len(cur) >= n:
            break
        counter += 1
    return counter

print(fibonacci_matrix(1000))
