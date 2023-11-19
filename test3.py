n1="1234567890"
lst=[]
lst1=[]
ps=[]
ps1=[]
n=list(input().rstrip())
for i in n:
    if i in n1:
        lst1.append(i)
    else:
        lst.append(i)
lst.sort()
lst1.sort()
for i in lst:
    if i==i.upper():
        ps.append(i)
        continue
    print(i,end='')
for i in ps:
    print(i,end='')
for i in lst1:
    if int(i)%2==0:
        ps1.append(i)
        continue
    print(i,end='')
for i in ps1:
    print(i,end='')

