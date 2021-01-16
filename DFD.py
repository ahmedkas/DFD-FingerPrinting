import pickle
import numpy as np
import random

# The data should be loaded from https://github.com/deep-fingerprinting/df, and used here.
# X_test: The original data, a matrix of shape Nx5000
# N refer to the number of traces, where each trace contains values within {-1,0,1}
f = open("./sampleInput.pickle","rb")
X_test = pickle.load(f)# Data

# pert: the perturbation rate to be applied
pert = 0.50

# variation_ratio: the variation parameter, affect the perturbation rate at the begining of each burst, this will only effect the white-box attack accuracy. (0 < variation_ratio < 1.0)
variation_ratio = 0.5

# ServerSide: If True, server-side injection will also be used (True/False)
ServerSide = True

# ClientSide: If True, client-side injection will also be used (True/False)
ClientSide = True

# X_testN: the perturbed representation
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
            perturbationCurrent = random.uniform(pert*variation_ratio, pert*(1+variation_ratio))
            if X_test[i][j] == 1:
                Cout += 1
                if last == -1 :
                    if ClientSide:
                        toAppend = int(1+perturbationCurrent*Cin)
                        for k in range(toAppend):
                            X_testN[i].append(-1)
                    Cin = 0
            elif X_test[i][j] == -1:
                Cin += 1
                if last == 1 :
                    if ServerSide:
                        toAppend = int(1+perturbationCurrent*Cout)
                        for k in range(toAppend):
                            X_testN[i].append(1)
                    Cout = 0
        last = X_test[i][j]
    X_testN[i] = X_testN[i][:5000] # Limit to the first 5,000 packets

# X_testN: the perturbed data.
X_testN = np.asarray(X_testN)
f = open("./sampleOutput.pickle","wb")
pickle.dump(X_testN,f)
