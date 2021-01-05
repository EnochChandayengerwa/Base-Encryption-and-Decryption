# Task 2

# Input
message = int(input())

# Coversion loop
new_message = []
while message != -1:
    og_chr = chr(message)
    new_message.append(og_chr)
    message = int(input())

# Output
for i in range(len(new_message)):
    print(new_message[i], end='')