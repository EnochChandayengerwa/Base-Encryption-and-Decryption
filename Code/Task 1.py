# Task 1

# Input
message = input()

# Converstion loop
message_list = []
for i in range(len(message)):
    new_char = ord(message[i])
    message_list.append(new_char)
    
# Output
for i in range(len(message_list)):
    print (message_list[i], end=' ')
    

