import pickle
import numpy as np
import random

# X_test: the data to be perturbed
# The data should be loaded from https://github.com/deep-fingerprinting/df, and used here.
X_test = load()

# pert: the perturbation rate (positive number)
pert = 0.50

# variation_ratio: the variation of the perturbation at each burst, this will only effect the white-box attack accuracy. (0 < variation_ratio < 1.0)
variation_ratio = 0.5

# ServerSide: If True, server side injection will also be used (True/False)
ServerSide = True

# ClientSide: If True, client side injection will also be used (True/False)
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
                    if ClientSide:
                        toAppend = int(1+perturbationCurrent*Cin)
                        for k in range(toAppend):
                            X_testN[i].append(-1)
                            countAdded += 1
                    Cin = 0
            elif X_test[i][j] == -1:
                Cin += 1
                if last == 1 :
                    if ServerSide:
                        toAppend = int(1+perturbationCurrent*Cout)
                        for k in range(toAppend):
                            X_testN[i].append(1)
                            countAdded += 1
                    Cout = 0
        last = X_test[i][j]
    X_testN[i] = X_testN[i][:5000] # The representation cut traces above 5,000 packets

# X_testN contains the perturbed data.
