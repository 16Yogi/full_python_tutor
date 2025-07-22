val = []
for i in range(0,8):
    if i%2==1:
        val.append(i)

for j in val:
    for k in range(8-j):
        print(end=" ")
    for l in range(j):
        print("*",end=" ")
    print(" ")
