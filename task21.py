zero=[0,0]
while True:
  first=input("give me for example: up 4: ")
  second=first.split(" ")
  
  if second[0]=="up":
    zero[0]+=int(second[1])
    print("_____________________\nYour actually position: %s"%(zero)) 
  elif second[0]=="down":  
    zero[0]-=int(second[1])
    print("_____________________\nYour actually position: %s"%(zero)) 
  elif second[0]=="left":  
    zero[1]-=int(second[1])
    print("_____________________\nYour actually position: %s"%(zero)) 
  elif second[0]=="right":  
    zero[1]+=int(second[1])
    print("_____________________\nYour actually position: %s"%(zero))   
  else:
    print("_____________________\nYour final position: %s"%(zero)) 
    break
