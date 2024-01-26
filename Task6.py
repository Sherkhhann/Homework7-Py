a=tuple(input())
b=tuple(input())
c=tuple(input())
i=0
lists=[]
while i<len(a):
 d=int(a[i])+int(b[i])+int(c[i])
 lists.append(d)
 i+=1
new_tuple=tuple(lists)
print(new_tuple)