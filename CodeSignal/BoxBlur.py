def tinh(image, hang , cot):
    res = 0
    for i in range(hang , hang + 3):
        for j in range(cot , cot + 3):
            res += image[i][j]
    return res // 9

def boxBlur(image):
    doc = len(image)
    ngang = len(image[0])
    res = []
    for i in range(doc - 2):
        temp = []
        for j in range(ngang - 2):
            temp.append(tinh(image , i , j))
        res.append(temp)
    return res
