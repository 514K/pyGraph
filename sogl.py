from math import *
import matplotlib.pyplot as plt
import pylab
from matplotlib import mlab

alpha = int(1)
list_sov1 = []
list_sov2 = []
list_all = []
r_i1 = float()
S_k1 = float()
r_i2 = float()
S_k2 = float()

exp = int(input("Insert quantity experts: "))
for i in range(exp):
    tmp = float(input("ins coord for {} exp: ".format(i + 1)))
    list_all.append([i + 1, tmp])
print()
for i in range(exp):
    tmp = int(input("ins 1 if exp {} appertain to 1 group or 2 if exp {} appertain to 2 group: ".format(i + 1, i + 1)))
    if tmp == 1:
        list_sov1.append(list_all[i])
    if tmp == 2:
        list_sov2.append(list_all[i])

m_k1 = int(len(list_sov1))
M_k1 = int(m_k1 * (m_k1 - 1) / 2)
for i in range(m_k1):
    for j in range(i + 1, m_k1):
        r_i1 = r_i1 + (list_sov1[i][1] - list_sov1[j][1]) ** 2
r_i1 = round(sqrt(r_i1), 2)
S_k1 = round(m_k1 / r_i1, 2)

m_k2 = int(len(list_sov2))
M_k2 = int(m_k2 * (m_k2 - 1) / 2)
for i in range(m_k2):
    for j in range(i + 1, m_k2):
        r_i2 = r_i2 + (list_sov2[i][1] - list_sov2[j][1]) ** 2
r_i2 = round(sqrt(r_i2), 2)
S_k2 = round(m_k2 / r_i2, 2)

if S_k1 < S_k2:
    print("Степень компактности сов т-к 1 меньше,чем степень комп сов т-к 2. => внутри группы экспертов {} мнения по оценке более схожи, чем в группе экспертов {}".format(list_sov2, list_sov1))
else:
    print("Степень компактности сов т-к 2 меньше,чем степень комп сов т-к 1. => внутри группы экспертов {} мнения по оценке более схожи, чем в группе экспертов {}".format(list_sov1, list_sov2))

Fi_i = []
R_i = []

for i in range(1, len(list_all)):
    tmp = round(float(sqrt((list_all[0][1] - list_all[i][1]) ** 2)), 2)
    tmp2 = round(float(1 / (1 + alpha * tmp)), 3)
    Fi_i.append(tmp2)
    R_i.append(tmp)

print()
print(R_i, Fi_i)
# part 2

pylab.subplot(1, 2, 1)
pylab.plot(sorted(R_i), sorted(Fi_i, reverse=True))
pylab.plot(sorted(R_i), sorted(Fi_i, reverse=True), 'o')
pylab.title("Функция для определения\nвысокосогласованных груп")

Sum_Fi = Fi_i
a = float(Sum_Fi[0])
for i in range(1, len(R_i)):
    a = round(a + Sum_Fi[i], 3)
    Sum_Fi[i] = a
print(Sum_Fi)


R_i_Fi_i = []
for i in range(len(R_i)):
    R_i_Fi_i.append([R_i[i], Sum_Fi[i]])
R_i.clear()
Sum_Fi.clear()
R_i_Fi_i.sort()
for i in range(len(R_i_Fi_i)):
    R_i.append(R_i_Fi_i[i][0])
    Sum_Fi.append(R_i_Fi_i[i][1])

pylab.subplot(1, 2, 2)
pylab.plot(R_i, Sum_Fi)
pylab.plot(R_i, Sum_Fi, 'o')
pylab.title("Сумма функций для определения\nвысокосогласованных групп")

pylab.show()

