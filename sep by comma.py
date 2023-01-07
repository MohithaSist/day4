a=int(input())
import json
b=str(a)
c=b[::-1]
count=0
li=[]
st=''
for i in c:
    count+=1
    if (count%3==0):
        m=i+','
        li.append(m)
    else:
        li.append(i)
for j in li:
    st+=j
if(st[-1]==','):
    st=st[:-1]
q=st[::-1]
print(json.dumps(q))
