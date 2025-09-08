#problem no1
i=0
s=0
while i<1000:
    if i%3==0 or i%5==0:
        s=s+i
    i=i+1
print(s)


#problem no2
f=1
s=2
for  i in range(10):
    t=f+s
    print(f,end=' ')
    f=s
    s=t
