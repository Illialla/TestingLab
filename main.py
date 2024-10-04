import cmath

def find_roots(a,b,c):
    print(f'{a}x^2+{b}x+{c}=0')
    D=b**2-(4*a*c)
    x1=(-b+cmath.sqrt(D))/(2*a)
    x2=(-b-cmath.sqrt(D))/(2*a)
    return x1, x2

if __name__ == '__main__':
    roots = find_roots(1,5,6)
    print(roots)


