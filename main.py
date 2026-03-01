import random
text="abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*+-*="
l=[]
for i in text:
    l.append(i)
ques=int(input("Number characters of your password: \n"))
pw=""
for i in range(ques):
    a=random.choice(l)
    pw+=a

print(f"Your password: {pw}")
