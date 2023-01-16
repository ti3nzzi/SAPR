import numpy as np
import json

def to_json(s):
    js = json.loads(s)
    s1 = []
    for j in js:
        if isinstance(j, list):
            s1.append(j)
        if isinstance(j, str):
            a = []
            a.append(j)
            s1.append(a)
    return s1

def task(str):
    experts = to_json(str)
    array=np.transpose(experts)
    A = np.zeros((3,3))
    B= np.zeros((3,3))
    C = np.zeros((3,3))
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][0]<array[j][0]:
                A[i][j]=1
            elif array[i][0]==array[j][0]:
                A[i][j]=0.5
            else:
                A[i][j]=0
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][1]<array[j][1]:
                B[i][j]=1
            elif array[i][1]==array[j][1]:
                B[i][j]=0.5
            else:
                B[i][j]=0
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][2]<array[j][2]:
                C[i][j]=1
            elif array[i][2]==array[j][2]:
                C[i][j]=0.5
            else:
                C[i][j]=0
    result= np.zeros((3,3))
    for i in range(len(array)):
        for j in range(len(array)):
            result[i][j]=A[i][j]/3+B[i][j]/3+C[i][j]/3
    k_0=[1,1,1]
    k_1=[1/3,1/3,1/3]
    while max(abs(np.array(k_1)- np.array(k_0)))>0.001:
        k_0=k_1
        y_0=np.dot(result,k_0)
        lambda_0=np.dot([1,1,1],y_0)
        k_1=1/lambda_0*y_0
    k=[round(i,3) for i in k_1]
    return k