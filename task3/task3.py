from io import StringIO
import csv

def read(csvString):
  f = StringIO(csvString)
  reader = csv.reader(f, delimiter=',')
  graph = []
  for row in reader:
     graph.append(row)
  for x in graph:
    for y in x:
      y = int(y)
  return graph

def rel1(graph):
  arr = []
  for x in graph:
    if x[0] not in arr:
      arr.append(str(x[0]))
  return arr

def rel2(graph):
  arr = []
  for x in graph:
    if x[1] not in arr:
      arr.append(str(x[1]))
  return arr

def rel3(graph):
  f = graph
  g = graph
  arr = []
  for i in range(len(f)):
    for j in range(len(g)):
      if i != j and f[i][0] not in arr and f[i][1] == g[j][0]:
        arr.append(str(f[i][0]))
  return arr

def rel4(graph):
  f = graph
  g = graph
  arr = []
  for i in range(len(f)):
    for j in range(len(g)):
      if i != j and f[i][1] not in arr and f[i][0] == g[j][1]:
        arr.append(str(f[i][1]))
  return arr

def rel5(graph):
  f = graph
  g = graph
  arr = []
  for i in range(len(f)):
    for j in range(len(g)):
      if i != j and f[i][1] not in arr and f[i][0] == g[j][0]:
        arr.append(str(f[i][1]))
  return arr

def task(csvString):
    graph = read(csvString)
    # Прямое управление
    arr1 = rel1(graph)
    # Прямое подчинение
    arr2 = rel2(graph)
    # Косвенное управление
    arr3 = rel3(graph)
    # Косвенное подчинение
    arr4 = rel4(graph)
    # Соподчинение
    arr5 = rel5(graph)
    
    return [arr1, arr2, arr3, arr4, arr5]

