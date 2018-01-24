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
    return f[0][1]

user_input = int(input('nth fibonacci number: '))
print(fibonacci_matrix(user_input))
