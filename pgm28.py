lim=int(input("enter the limit:"))
for row in range(1,lim+1):
 for col in range(1,row+1):
  print("*",end=" ")
 print()
for row in range(lim-1,0,-1):
 for col in range(1,row+1):
  print("*",end=" ")
 print()     
  
