def reverse(x , a , b):
    return x[:a] + x[a+1 : b][::-1] + x[b+1:]

def solution(x):
    idx = 0
    while (idx < len(x)):
        if x[idx] == "(":
            left = idx
        elif x[idx] == ")":
            x = reverse(x , left , idx)
            idx = -1
        idx += 1
    return x