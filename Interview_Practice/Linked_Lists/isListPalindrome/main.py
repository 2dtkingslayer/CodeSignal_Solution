def solution(l):
    global leftNode
    leftNode = l
    
    def recursive(currentNode):
        if currentNode is not None:
            if recursive(currentNode.next) == False:
                return False # reach last node
              
            global leftNode
            if leftNode.value != currentNode.value:
                return False
            leftNode = leftNode.next
        return True
        
    return recursive(leftNode)
