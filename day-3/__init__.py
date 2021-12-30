from numpy.lib.twodim_base import diag


def powerConsumption(diagnostics):
    byte_len = len(str(diagnostics[0]))
    gamma, epilson = '', ''
    for i in range(byte_len):
        bits = []
        for report in diagnostics:
            bits.append(report[i])
        gamma += max(bits, key=bits.count)
        epilson += min(bits, key=bits.count)
    return int(gamma, 2) * int(epilson, 2)
        
def co2o2(diagnostics):
    rows, cols = shape(diagnostics)
    ox = ""
    i = 0
    for col in cols:
        maxv = max(col, key=col.count)
        minv = max(col, key=col.count)
        if minv == maxv:
            maxv = 1
        ox += str(maxv)     
        diagnostics = [x for x in diagnostics if x[i] == minv]
        i += 1
        rows, cols = shape(diagnostics)
    co = ""
    i = 0
    for col in cols:
        maxv = max(col, key=col.count)
        minv = max(col, key=col.count)
        if minv == maxv:
            minv = 0
        co += str(minv)           
        diagnostics = [x for x in diagnostics if x[i] == maxv]
        i += 1
        rows, cols = shape(diagnostics)
    print(co)
    print(ox)
    return int(co, 2) * int(ox, 2)

from collections import Counter

def parse_bit_pos(arr, pos):
    
    return Counter(row[pos] for row in arr)

def part2(data):
    L1 = L2 = data
    for i in range(len(data[0])):
        c1, c2 = parse_bit_pos(L1, i), parse_bit_pos(L2, i)
        
        if len(L1) > 1:
            if len(set(c1.values())) == 1:
                L1 = [row for row in L1 if row[i] == 1]
            else:
                L1 = [row for row in L1 if row[i] == max(c1.items(), key=lambda x: x[1])[0]]
        if len(L2) > 1:
            if len(set(c2.values())) == 1:
                L2 = [row for row in L2 if row[i] == 0]
            else:
                L2 = [row for row in L2 if row[i] == min(c2.items(), key=lambda x: x[1])[0]]
            
    o2, co2 = int(''.join([str(n) for n in L1[0]]), 2), int(''.join([str(n) for n in L2[0]]), 2)
    print(o2 * co2)
            
def shape(array):
    rows = []
    cols = []
    for i in array:
        rows.append(list(map(int, str(i))))
        
    for i in range(len(array[0])):
        col = []
        for n in array:
            col.append(n[i])
        cols.append(col)
            
    return rows,cols    

def readFile():
    f = open('Day 3/input.txt', 'r')
    data = f.read().splitlines()
    #data = [int(x) for x in data]
    return data

if __name__ == '__main__':
    data = readFile()
    print(powerConsumption(data))
    #print(co2o2(data))
    print(part2(data))