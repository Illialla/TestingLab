import cmath

def find_roots(a,b,c):
    print("---------------------------------")
    print(f'{a}x^2+{b}x+{c}=0')
    D=b**2-(4*a*c)
    # print(f'{b**2}-{4*a*c}={D}')
    x1=(-b+cmath.sqrt(D))/(2*a)
    # print(f'{-b}+{cmath.sqrt(D)}/{a}')
    x2=(-b-cmath.sqrt(D))/(2*a)
    # print(f'{-b}-{cmath.sqrt(D)}/{a}')
    print(x1,x2)
    return x1, x2

def test_find_roots():
    assert find_roots(1, 5, 6) == (-2.0, -3.0)
    assert find_roots(1, 2, 1) == (-1.0, -1.0)
    assert find_roots(1, 2, 5) == (-1 + 2j, -1 - 2j)
    try:
        find_roots(0, 2, 3)
    except ZeroDivisionError:
        pass  # Ожидаем ошибку деления на ноль
    assert find_roots(1, 0, -4) == (2.0, -2.0)
    assert find_roots(-1, -4, -4) == (-2.0, -2.0)
    assert find_roots(10**6, 10**6, 10**6)


if __name__ == '__main__':
    # print(find_roots(-1,-4,-4))
    test_find_roots()


