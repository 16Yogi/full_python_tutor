val = []
rev = []
for i in range(0,8):
    if i%2==1:
        val.append(i)
len = 0
for j in val:
    len = len+1
# print(len)

for k in val:
    len = len-1
    # print(val[len])
    rev.append(val[len])
# print(rev)

for l in rev:
    for n in range(8-l):
        print(end=" ")
    for m in range(l):
        print("*",end=" ")
    print(" ")
