import re
email=input("give me something: ")
email2="(\w+)@(\w+)\.+(com)"
r2=re.match(email2, email)
print(r2.group(1))




em=input("give me something: ")
import re
em2=re.split(r"[@.]+", em)
print(em2[1])

