a = [2,1,3,4]

for i in range(len(a)-1):
    if a[i]>a[i+1]:
        a[i],a[i+1] = a[i+1],a[i]

print(a)
