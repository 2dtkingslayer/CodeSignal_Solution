def alphabeticShift(inputString):
    for i in range(len(inputString)):
        inputString[i] = chr(ord(inputString[i]) + 1)
    return inputString
print(chr(98))
#print(alphabeticShift("abcde"))