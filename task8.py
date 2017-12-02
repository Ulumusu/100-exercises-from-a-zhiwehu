word=[x for x in input().split(",")]
for x in word:
    word.sort()

print (','.join(word))