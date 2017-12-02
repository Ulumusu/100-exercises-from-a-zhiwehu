one=["I", "You"]
two=["Play", "Love"]
three=["Hockey","Football"]
for  i in range(len(one)):
    for x in range(len(two)):
        for a in range(len(three)):
            answer="%s %s %s" %(one[i],two[x],three[a])
            print(answer)
