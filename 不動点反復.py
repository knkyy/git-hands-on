# x = 1/cosh(x) の近似解を求めるためのプログラム

x = float(0)

# print(type(x))
for i in range(10):
    x = 2/(2.7182**x+2.7182**(-x))
print(x)