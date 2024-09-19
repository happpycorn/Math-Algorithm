n=int(input("n="))
i=0
j=1
sum=0
for x in range(n-1):
    y=i
    i=j
    j=y+i
print(j)