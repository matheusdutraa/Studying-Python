import numpy as np
x = np.array([2, 1.5, 1.2, 1, 0.5, 0.2, 0.1, 0.01])
deltax = 5 * x ** 2 + 3 * x - 2
deltay = 2 * x ** 3 + 5
d = (deltax ** 2 + deltay ** 2) ** 0.5
vm = d / x
print("T / d / Vm")
for i in range(len(x)):
    print(round(x[i], 2), round(d[i], 2), round(vm[i], 2))

"""
T / d / Vm
2.0 31.89 15.95
1.5 18.09 12.06
1.2 12.2 10.17
1.0 9.22 9.22
0.5 5.3 10.61
0.2 5.16 25.79
0.1 5.27 52.67
0.01 5.37 537.39
"""
