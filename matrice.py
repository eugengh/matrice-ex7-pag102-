
m = [[4, -3, 10, 0 , -12],
    [3, 22, -4, 11, 1],
    [5, -5, -2, 9, 7],
    [8, -10, -7, 24, 31],
    [-11, 14, 17, -19, 20]]

print(sum(m[0]))
print(sum(m[1]))
print(sum(m[2]))
print(sum(m[3]))
print(sum(m[4]))
c0 = []
for i in m:
    c0.append(i[0])
print(sum(c0))
c1 = []
for a in m:
    c1.append(a[1])
print(sum(c1))
c2 = []
for b in m:
    c2.append(b[2])
print(sum(c2))
c3 = []
for e in m:
    c3.append(e[3])
print(sum(c3))
c4 = []
for d in m:
    c4.append(d[4])
print(sum(c4))
### diagonaal princ
for x in range(len(m[0])):
    print(m[x][x])
#diagonala secundara prin reversarea matricei 
d = (m[::-1])
for q in range(len(d[0])):
    print(d[q][q])