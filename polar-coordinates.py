import cmath

cmplx = complex(input())
print("\n".join(str(x) for x in cmath.polar(cmplx)))
