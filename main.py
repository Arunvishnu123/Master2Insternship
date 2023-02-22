import sympy

# define variables
x, y, z = sympy.symbols('x y z')

def is_linear(expr, vars):
    for x in vars:
        for y in vars:
            try:
                if not sympy.Eq(sympy.diff(expr, x, y), 0):
                    print("function is not linear")
                    return False
            except TypeError:
                print("function is not linear")
                return False
    print("function is linear")
    return True
eq1 = x*y*z

print(is_linear(eq1, [x,y,z]))
