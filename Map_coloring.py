from z3 import *
s, a, b, c, d = 0, 15, 15, 16, 16
diag_1 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
diag_2 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
diag_3 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
diag_4 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
x = [ [ Int("x_%s_%s" % (i+1, j+1)) for j in range(c) ] for i in range(c) ]
cells  = [ Or(x[i][j]==1, x[i][j]==2, x[i][j]==3, x[i][j]==4, x[i][j]==5) for i in range(c) for j in range(c) ]
rows   = [ Distinct([x[i][j], x[i][j+1]]) for j in range(b) for i in range(c) ]
cols   = [ Distinct([x[i][j], x[i+1][j]]) for i in range(b) for j in range(c) ]
gc = cells+rows+cols
for k in range(a):
    diag_1[k] = [ Distinct([x[i][j], x[i+1][j+1]]) for i,j in zip(range(b), range(s,b)) ]
    s = s+1
    gc = gc+diag_1[k]
s=1
for k in range(a):
    diag_2[k] = [ Distinct([x[i][j], x[i+1][j+1]]) for i,j in zip(range(s,b), range(b-1)) ]
    s = s+1
    b = b-1
    gc = gc+diag_2[k]
s=1
for k in range(a):
    diag_3[k] = [ Distinct([x[i][j], x[i+1][j-1]]) for i,j in zip(range(a), reversed(range(s,c))) ]
    c = c-1
    gc = gc+diag_3[k]
s=1
for k in range(a):
    diag_4[k] = [ Distinct([x[i][j], x[i+1][j-1]]) for i,j in zip(range(s,a), reversed(range(s,d))) ]
    s = s+1
    gc = gc+diag_4[k]

t = [[0 for j in range (c)] for i in range (c)]

instance = [If(True, True, x[i][j]==t[i][j]) for i in range(c) for j in range (c)]

s = Solver()
s.add(gc + instance)
if s.check() == sat:
    m = s.model()
    print(s.check())
    r = [ [ m.evaluate(x[i][j]) for j in range(16) ] for i in range(16) ]
    print_matrix(r)
else:
    print("failed to solve")