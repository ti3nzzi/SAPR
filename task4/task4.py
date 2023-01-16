from io import StringIO
import math
import csv

def task(csvStr):
    f = StringIO(csvStr)
    reader = csv.reader(f, delimiter=',')
    graph = []
    for row in reader:
        graph.append(row)
    for x in graph:
        for y in x:
            y = int(y)
    # Отношение 1 - прямое управление
    arr1 = []
    for x in graph:
        arr1.append(x[0])
    # Отношение 2 - прямое подчинение
    arr2 = []
    for x in graph:
        arr2.append(x[1])
    # Отношение 3 - косвенное управление
    f = graph
    g = graph
    arr3 = []
    for i in range(len(f)):
        for j in range(len(g)):
            if i != j and f[i][1] == g[j][0]:
                arr3.append(f[i][0])
    # Отношение 4 - косвенное подчинение
    arr4 = []
    for i in range(len(f)):
        for j in range(len(g)):
            if i != j and f[i][0] == g[j][1]:
                arr4.append(f[i][1])
    # Отношение 5 - соподчинение
    arr5 = []
    for i in range(len(f)):
        for j in range(len(g)):
            if i != j and f[i][0] == g[j][0]:
                arr5.append(f[i][1])

    res_arr = [] # результат
    vertices = [] # количество вершин
    for x in graph:
        for y in x:
            if y not in vertices:
                vertices.append(y)
    vertices.sort()

    for v in vertices:
        res_arr.append([])
    
    for v in vertices:
        res_arr[int(v)-1].append(arr1.count(v))
        res_arr[int(v)-1].append(arr2.count(v))
        res_arr[int(v)-1].append(arr3.count(v))
        res_arr[int(v)-1].append(arr4.count(v))
        res_arr[int(v)-1].append(arr5.count(v))

    s = 0
    for j in range(len(vertices)):
        for i in range(5):
            if res_arr[j][i] != 0:
                s += (res_arr[j][i] / (len(vertices) - 1)) * math.log(res_arr[j][i] / (len(vertices) - 1), 2)

    return -s