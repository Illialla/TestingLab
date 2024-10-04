import cmath

def find_roots(a,b,c):
    print('-----------------------------')
    print(f'{a}x^2+{b}x+{c}=0')
    if (a==0):
        print("Деление на 0!")
        return "Деление на 0!"
    D=b**2-(4*a*c)
    x1=(-b+cmath.sqrt(D))/(2*a)
    x2=(-b-cmath.sqrt(D))/(2*a)
    print(x1,x2)
    if x1==x2:
        print(f'x1={x1}')
        return x1
    else:
        print(f'x1={x1}, x2={x2}')
        return x1, x2

if __name__ == '__main__':
    roots = find_roots(1,2,1)
    print(roots)


