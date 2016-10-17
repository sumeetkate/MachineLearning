import sys
import random
import math

def dot_product(a, b):
    res = 0
    for i in range(0, cols, 1):
        res += (a[i] * b[i])
    return res

dataFile = sys.argv[1]
f = open(dataFile)
data = []
i = 0
l = f.readline()

#### Read Data ####

while (l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
    l2.append(1)

    data.append(l2)
    l = f.readline()

f.close()

rows = len(data)
cols = len(data[0])

#### Read Labels ####

labelFile = sys.argv[2]
f = open(labelFile)
classData = {}
l = f.readline()
while (l != ''):
    a = l.split()
    if (a[0] == str(0)):
        classData[int(a[1])] = -1
    else:
        classData[int(a[1])] = int(a[0])
    l = f.readline()

f.close()

#### Initialize W ####
w = [0 for j in range(0, cols, 1)]
# random.seed(1)
for j in range(0, cols, 1):
    w[j] = (0.02 * random.uniform(0, 1)) - 0.01

#### Gradient Descent Iteration ####
eta = 0.001
temp = float(0)
for k in range(0, 100000, 1):
    dellf = [0 for i in range(0, cols, 1)]
    for i in range(0, rows, 1):
        if (classData.get(i) != None):
            dp = dot_product(w, data[i])
            for j in range(0, cols, 1):
                dellf[j] += (float(classData.get(i)) - dp) * data[i][j]

    #### Update ####
    for j in range(0, cols, 1):
        w[j] = w[j] + (eta * dellf[j])

    #### Compute Error ####
    error = float(0)
    for i in range(0, rows, 1):
        if (classData.get(i) != None):
            error += (float(classData.get(i)) - dot_product(w, data[i])) ** 2

    temp = math.fabs(error - temp)

    if float(temp) <= 0.001:
        print("Error : " + str(error))
        break
    temp = error

print("w =")

normw = 0

for j in range(0, cols - 1, 1):
    normw += w[j] ** 2
    print(w[j])

normw = math.sqrt(normw)

d_origin = w[len(w) - 1] / normw

print("Distance from origin ::" + str(math.fabs(d_origin)))

#### Prediction ####

for i in range(0, rows, 1):

    if (classData.get(i) == None):
        dp = dot_product(w, data[i])
        if (dp > 0):
            print("0", i)
        else:
            print("1", i)
















