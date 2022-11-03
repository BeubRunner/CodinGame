import sys
import math

def calc(li, op):
    #op = [opération, n, m]
    ar = [op[1], op[2]]
    for i in range(2):
        if str(ar[i]) == "_" :
            ar[i] = int(0)
        else :
            ar[i] = int(ar[i])

    if op[0] == "VALUE" :
        return(ar[0])
    if op[0] == "ADD" :
        return(ar[0] + ar[1])
    if op[0] == "SUB" :
        return(ar[0] - ar[1])
    if op[0] == "MULT" :
        return(ar[0] * ar[1]) 

def search_val(op_list, index_list):
    for op in op_list :
        for v in range(1,3) : 
            if "$" in op[v] :
                ix = int(op[v][1:])
                if ix in index_list :   
                    op[v] = str(l[ix])
                    op[4] -= 1
    return(op_list)


n = int(input())
op = []
op_list = []
for i in range(n):
    operation, arg_1, arg_2 = input().split()
    c = arg_1.count("$") + arg_2.count("$")
    op = [operation, arg_1, arg_2, 1, c]
    op_list.append(op)

# MEMO op_list == list of op as op = [OPERATION, arg_1, arg_2, (0,1), c]
# (0, 1) : 1 == not operated yet 0 == already done
# c : the number of dependencies 

l = [0]*n               # calculated values list 
index_list = []         # index off already calculated values

while len(index_list) != len(l) :
    for (ind, op) in enumerate(op_list) :
        if op[4] == 0 and op[3] == 1 : 
            l[ind] = calc(l, op)
            op[3] = 0
            index_list.append(ind)

    op_list = search_val(op_list, index_list)

for v in l :
    print(v)
