from operator import *
list_a = [[9.4, 0.096], [7.2, 0.122], [1.7, 0.37], [3.2, 0.238], [8.0, 0.111], [8.3, 0.108]]
list_b = []
list_c = []
list_bc = []
for i in range(len(list_a)):
    list_b.append(list_a[i][0])
    list_c.append(list_a[i][1])
print(list_b)
#print(list_c)
a = float(list_c[0])
for i in range(1, len(list_a)):
    a = round(a + list_c[i], 3)
    list_c[i] = a
print(list_c)

for i in range(len(list_a)):
    list_bc.append([list_b[i], list_c[i]])
list_b.clear()
list_c.clear()
list_bc.sort()
for i in range(len(list_bc)):
    list_b.append(list_bc[i][0])
    list_c.append(list_bc[i][1])
print(list_bc)
print(list_b)
print(list_c)
from numpy import *
import matplotlib.pyplot as plt
plt.plot(list_b, list_c)
plt.plot(list_b, list_c, 'o')
plt.show()