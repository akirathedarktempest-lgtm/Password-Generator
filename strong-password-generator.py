import random
letters="abcdefghijklmnopqrstuvwxyz"
symbols="!@#$%&*?"
numbers="0123456789"
sle=[]
ble=[]
sym=[]
num=[]
pw=[]
for i in letters:
    sle.append(i)
for y in letters.upper():
    ble.append(y)
for s in symbols:
    sym.append(s)
for n in numbers:
    num.append(n)
psw=""
length=int(input("Please enter the length of the password you want\n"))
if length<8:
    print(f"For a strong password, you will at least need 8 characters/length of 8 but it's {length} :(")
else:
    l=length//4
    if length%4!=0:
        le=length%4
        for z in range(l):
            pw.append(random.choice(sle))
            pw.append(random.choice(ble))
            pw.append(random.choice(sym))
            pw.append(random.choice(num))
        for x in range(le):
            pw+=random.choice(sle+ble+sym+num)
        random.shuffle(pw)
        for j in pw:
            psw+=j
    else:
        for z in range(l):
            pw.append(random.choice(sle))
            pw.append(random.choice(ble))
            pw.append(random.choice(sym))
            pw.append(random.choice(num))
        random.shuffle(pw)
        for j in pw:
            psw+=j
        print(psw)
"""There can be a better way to make it, more less codes for that, but my logic could only think of this much :( And please keep length of 8 or more, it wouldn't work otherwise :)"""
#by the way, what if you want to run more than one time...? making it a function?
def passwordGenerator():
    letters="abcdefghijklmnopqrstuvwxyz"
    symbols="!@#$%&*?"
    numbers="0123456789"
    sle=[]
    ble=[]
    sym=[]
    num=[]
    pw=[]
    for i in letters:
        sle.append(i)
    for y in letters.upper():
        ble.append(y)
    for s in symbols:
        sym.append(s)
    for n in numbers:
        num.append(n)
    psw=""
    length=int(input("Please enter the length of the password you want\n"))
    if length<8:
        print(f"For a strong password, you will at least need 8 characters/length of 8 but it's {length} :(")
    else:
        l=length//4
        if length%4!=0:
            le=length%4
            for z in range(l):
                pw.append(random.choice(sle))
                pw.append(random.choice(ble))
                pw.append(random.choice(sym))
                pw.append(random.choice(num))
            for x in range(le):
                pw+=random.choice(sle+ble+sym+num)
            random.shuffle(pw)
            for j in pw:
                psw+=j
            print(psw)
        else:
            for z in range(l):
                pw.append(random.choice(sle))
                pw.append(random.choice(ble))
                pw.append(random.choice(sym))
                pw.append(random.choice(num))
            random.shuffle(pw)
            for j in pw:
                psw+=j
            print(psw)

passwordGenerator()
