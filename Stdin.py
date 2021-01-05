from sys import stdin

inp = ""  # This will store the inputs

for line in stdin:  # This will ask for input until the user stops input by pressing Ctrl + D or Ctrl + Z
    inp += line  # Adds a new input to the inp variable

# remove the whitespaces at the end because stdin keeps the \n at the end
inp = inp.rstrip()

print(inp)

# You can do your processing here the same way you did for encrypt in task 5
