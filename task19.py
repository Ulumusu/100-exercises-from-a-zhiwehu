from operator import itemgetter, attrgetter
box_with_name = []
while True:
    data = input("name, age, score: ")
    if not data:
        break
    box_with_name.append(tuple(data.split(",")))

print (sorted(box_with_name, key=itemgetter(0,1,2)))
