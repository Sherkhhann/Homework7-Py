def CountNumbers():
 text=input()
 cnt=0
 for i in text:
  if i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9" or i=="0":
   cnt+=1
 print(cnt)

CountNumbers()