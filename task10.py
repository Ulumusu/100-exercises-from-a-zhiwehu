word=[x for x in input().split()]


word2=[]
for x in word:
    if x  not in word2:
        word2.append(x)

for x in word2:
    word2.sort()

print(" ".join(word2))