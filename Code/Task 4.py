# Task 4

# Input
base = int(input())
num = input()
new_num = []

# Output
if base>=2 and base<=36:
    while num !='-1':
        for i in range(len(num)):
            if num[i]=="A" or num[i]=="a":new = 10
            elif num[i]=="B" or num[i]=="b":new = 11
            elif num[i]=="C" or num[i]=="c":new = 12
            elif num[i]=="D" or num[i]=="d":new = 13
            elif num[i]=="E" or num[i]=="e":new = 14
            elif num[i]=="F" or num[i]=="f":new = 15
            elif num[i]=="G" or num[i]=="g":new = 16
            elif num[i]=="H" or num[i]=="h":new = 17
            elif num[i]=="I" or num[i]=="i":new = 18
            elif num[i]=="J" or num[i]=="j":new = 19
            elif num[i]=="K" or num[i]=="k":new = 20
            elif num[i]=="L" or num[i]=="l":new = 21
            elif num[i]=="M" or num[i]=="m":new = 22
            elif num[i]=="N" or num[i]=="n":new = 23
            elif num[i]=="O" or num[i]=="o":new = 24
            elif num[i]=="P" or num[i]=="p":new = 25
            elif num[i]=="Q" or num[i]=="q":new = 26
            elif num[i]=="R" or num[i]=="r":new = 27
            elif num[i]=="S" or num[i]=="s":new = 28
            elif num[i]=="T" or num[i]=="t":new = 29
            elif num[i]=="U" or num[i]=="u":new = 30
            elif num[i]=="V" or num[i]=="v":new = 31
            elif num[i]=="W" or num[i]=="w":new = 32
            elif num[i]=="X" or num[i]=="x":new = 33
            elif num[i]=="Y" or num[i]=="y":new = 34
            elif num[i]=="Z" or num[i]=="z":new = 35
            else:new = int(num[i])
            new_num.append(new)
        
        count = 0
        total = 0
        for i in range(len(new_num)-1,-1,-1):
            new_num[i] = new_num[i]*(base**count)
            total = total +new_num[i]
            count+=1
        print(total)
        new_num = []
        num = input()
