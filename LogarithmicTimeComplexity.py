i = 1
while i<=n:
    i = i*c 

i = n
while i>0:
    i = i//c 

# -------------------


def recurse(n):
    if n<=0:
        return
    else:
        recurse(n/c)