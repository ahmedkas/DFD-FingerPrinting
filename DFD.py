import pickle
import numpy as np
import random

# X_test: the data to be perturbed
X_test = load()

# pert: the perturbation rate
pert = 0.50
# variation_ratio: the variation of the perturbation at each burst, this will only effect the white-box attack accuracy.
variation_ratio = 0.5

# ServerSide: If True, server side injection will also be used
ServerSide = True

# ClientSide: If True, client side injection will also be used
ClientSide = True

# X_testN: the new perturbed representation
X_testN = []

for i in range(len(X_test)):
    
    X_testN.append([])
    Cout = 0
    Cin = 0
    last = 0
    for j in range(len(X_test[i])):
        X_testN[i].append(X_test[i][j])
        if X_test[i][j] == 0:
            continue
	else:
            perturbationCurrent = random.randrange(pert*variation_ratio, pert*(1+variation_ratio))
            if X_test[i][j] == 1:
                Cout += 1
                if last == -1 :
                    toAppend = int(1+perturbationCurrent*Cin)
                    for k in range(toAppend):
                        X_testN[i].append(-1)
                        countAdded += 1
                    Cin = 0
            elif X_test[i][j] == -1:
                Cin += 1
                if last == 1 :
                    toAppend = int(1+perturbationCurrent*Cout)
                    for k in range(toAppend):
                        X_testN[i].append(1)
                        countAdded += 1
                    Cout = 0
        last = X_test[i][j]
    X_testN[i] = X_testN[i][:5000]


