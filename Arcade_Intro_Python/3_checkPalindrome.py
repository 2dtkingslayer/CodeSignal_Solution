# Approach 1
def solution(inputString):
    for i in range(len(inputString) // 2):
        if inputString[i] != inputString[len(inputString) - 1 - i]:
            return False
    return True

# Approach 2
def solution(inputString):
    return inputString == inputString[::-1]
