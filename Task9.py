a=input().split()
mini=9999
cnt=0
for i in a:
 if int(i)%2!=0:
  if int(i)<int(mini):
   mini=i
   cnt=1
if cnt>0:
 print(mini)
else:
 print("0")