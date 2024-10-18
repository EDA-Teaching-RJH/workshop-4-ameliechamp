camel = input("Enter in your variable in camel case: ")
outputstr=""
for c in camel:
    if c.islower():
        outputstr+=c
    else:
        outputstr += "_" + c.lower()
print(outputstr)
