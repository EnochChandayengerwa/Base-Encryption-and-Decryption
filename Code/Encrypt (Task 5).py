# Task 5

# Input
mode = input()
base = int(input())
message = input()


# Encryption Modes
if mode == 'encrypt': 

    #converts to ASCII values
    message_list = []
    for i in range(len(message)):
        new_char = ord(message[i])
        message_list.append(new_char)

    #Then converts to bases
    new_num = []
    for i in range(len(message_list)):
        if base>=2 and base<=36:
            s = message_list[i]/base
            r = int(message_list[i]%base)
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
                
                print(new_num[i],end='')
            
            #Then outputs bases with relevant spaces     
            print(" ", end = '')
            new_num = []
    
elif mode == 'decrypt':
    num = []
    num.append(message.split)
    new_num = []

    # Base to decimal number
    new_num = []
    num = message.split(" ",-1)
    output = []

    for j in range(len(num)):
        if base>=2 and base<=36:
            for i in range(len(num[j])):
                temp = num[j]
                if temp[i]=="A":new = 10
                elif temp[i]=="B":new = 11
                elif temp[i]=="C":new = 12
                elif temp[i]=="D":new = 13
                elif temp[i]=="E":new = 14
                elif temp[i]=="F":new = 15
                elif temp[i]=="G":new = 16
                elif temp[i]=="H":new = 17
                elif temp[i]=="I":new = 18
                elif temp[i]=="J":new = 19
                elif temp[i]=="K":new = 20
                elif temp[i]=="L":new = 21
                elif temp[i]=="M":new = 22
                elif temp[i]=="N":new = 23
                elif temp[i]=="O":new = 24
                elif temp[i]=="P":new = 25
                elif temp[i]=="Q":new = 26
                elif temp[i]=="R":new = 27
                elif temp[i]=="S":new = 28
                elif temp[i]=="T":new = 29
                elif temp[i]=="U":new = 30
                elif temp[i]=="V":new = 31
                elif temp[i]=="W":new = 32
                elif temp[i]=="X":new = 33
                elif temp[i]=="Y":new = 34
                elif temp[i]=="Z":new = 35
                else:new = int(temp[i])
                new_num.append(new)
            
            count = 0
            total = 0
            for i in range(len(new_num)-1,-1,-1):
                new_num[i] = new_num[i]*(base**count)
                count+=1
                total = total +new_num[i]
            
            output.append(total)
            
            new_num = []
    #print(output)

    # Decimal number to ASCII
    new_message = []

    for i in range (len(output)):
        num = int(output[i])
        og_chr = chr(num)
        new_message.append(og_chr)
    for i in range(len(new_message)):
        print(new_message[i], end='')
               
else: print ("Input error, only enter encrypt or decrypt")