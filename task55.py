import re
email=input("give me something: ")
email2="(\w+)@((\w+\.)+(com))"
r2=re.match(email2, email)
print(r2.group(1))




em=input("give me something: ")
em2=em.split("@")
print(em2[0])
