from timer import timer

def spiral_diagonal_sum(quadratic):
    s = 0
    for i in range(1,501):
        s += quadratic(i)
    return s

def generate_quadratics():
    # Acknowledgements: Dr. James Grime, Numberphile: https://www.youtube.com/watch?v=iFuR97YcSLM
    quadratic0 = lambda x: 4*(x*x) - 2*x + 1
    quadratic1 = lambda x: 4*(x*x) + 2*x + 1
    quadratic2 = lambda x: 4*(x*x) + 1
    quadratic3 = lambda x: 4*(x*x) + 4*x + 1
    return [quadratic0, quadratic1, quadratic2, quadratic3]

def main():
    overall_sum = 1
    for q in generate_quadratics():
        overall_sum += spiral_diagonal_sum(q)
    print(overall_sum)

timer(main)
