# Task 3
import math

# Input
base = int(input())
num = int(input())
new_num = []

# Output
if base>=2 and base<=36:
    while num !=-1:
        s = num/base
        r = int(num%base)
        new_num.append(r)
        q = s-(r/base)

        while q!=0:
            s = q/base
            r = int(q%base)
            new_num.append(r)
            q = s-(r/base)
            
        for i in range(len(new_num)-1,-1,-1):
            if new_num[i]==10:new_num[i]='A'
            if new_num[i]==11:new_num[i]='B'
            if new_num[i]==12:new_num[i]='C'
            if new_num[i]==13:new_num[i]='D'
            if new_num[i]==14:new_num[i]='E'
            if new_num[i]==15:new_num[i]='F'
            if new_num[i]==16:new_num[i]='G'
            if new_num[i]==17:new_num[i]='H'
            if new_num[i]==18:new_num[i]='I'
            if new_num[i]==19:new_num[i]='J'
            if new_num[i]==20:new_num[i]='K'
            if new_num[i]==21:new_num[i]='L'
            if new_num[i]==22:new_num[i]='M'
            if new_num[i]==23:new_num[i]='N'
            if new_num[i]==24:new_num[i]='O'
            if new_num[i]==25:new_num[i]='P'
            if new_num[i]==26:new_num[i]='Q'
            if new_num[i]==27:new_num[i]='R'
            if new_num[i]==28:new_num[i]='S'
            if new_num[i]==29:new_num[i]='T'
            if new_num[i]==30:new_num[i]='U'
            if new_num[i]==31:new_num[i]='V'
            if new_num[i]==32:new_num[i]='W'
            if new_num[i]==33:new_num[i]='X'
            if new_num[i]==34:new_num[i]='Y'
            if new_num[i]==35:new_num[i]='Z'
            if new_num[i]==36:new_num[i]='10'
            print(new_num[i], end='')

        print("")
        new_num = []
        num = int(input())