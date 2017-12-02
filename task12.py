dict=[]
for number in range(1000, 3001):
    number_str=str(number)
    if (int(number_str[0]) % 2 == 0) and (int(number_str[1]) % 2 == 0) and (int(number_str[2]) % 2 == 0) and (int(number_str[3]) % 2 == 0):
        dict.append(number_str)
print(dict)

#my because i didn't understand topic

for number2 in range(100, 1001):
    number_str2=str(number2)
    if (int(number_str2[1])%5==0) and (int(number_str[2])%2==0):
        print(number_str2)