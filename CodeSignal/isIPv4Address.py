"""
import re
def isIPv4Address(S):
    if S[0] == "." or S[-1] == "." or "." not in S or (".." in S) or ("..." in S) or re.search('[a-zA-Z]', S) or S.count(".") >= 4:
        return False
    for i in range(len(S)-2):
        if i == 0 and S[0] == "0" and S[1] != ".":
            return False
        elif S[i] == "." and S[i+1] == "0" and S[i+2] != ".":
            return False
    S = S.replace("."," ")
    a = S.split()
    for i in a:
        if int(i) > 255:
            return False
    return True
"""
def isIPv4Address(inputString):
    inputString = inputString.split('.')
    if len(inputString) != 4:
        return False
    for num in inputString:
        if not num.isnumeric():
            return False
        if len(num) >= 2 and num[0] == "0":
            return False
    for num in inputString:
        if int(num) < 0 or int(num) > 255:
            return False
    return True