import numpy as np
from .symbols import *

tables = open('TABLES/list', 'r').readlines()
tables = [i.strip() for i in tables]

def reads(f):
    print('Reading table %s' %f)
    lines = open(f,'r').readlines()
    return np.asarray([float(i) for i in lines])

def sym2num(data):
    n = len(tables)
    print('Rewriting sym -> numbers for %i desriptors' %n)
    dics = [ {} for i in range(n)]
    #create n new descriptors from the tables
    for i in range(n):
       table = reads('TABLES/'+tables[i])
       dics[i]  = {sym: num for sym, num in zip(symbols, table)}

    vectors = []
    for vector in data:
        numbers = []
        for el in vector:
            for i in range(n): 
                numbers.append(float(dics[i][el]))
        vectors.append(numbers)
    return np.asarray(vectors)

def num2sym(number):
    numbers = [str(int(num)) for num in reads('TABLES/Number.table')]
    dic = {num: sym for num, sym in zip(numbers, symbols)}
    return dic[str(int(number))]
