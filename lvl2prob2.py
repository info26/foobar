def solution(s):
    # define the hallway
    ##
    salutes = 0
    indices = []
    for i in range(len(s)):
        if s[i] == ">":
            indices.append(i)

    for rightOccurence in indices:
        salutes += s.count("<", rightOccurence)

    # # let's do the > first.
    # firstRight = s.find(">")
    # if (firstRight == -1):
    #     right = 0
    # else:
    #     # let's search through the string!
    #     right = s.count("<", firstRight) * s.count(">")
    
    # # firstLeft = s[::-1].find("<")
    # # if (firstLeft == -1):
    # #     left = 0
    # # else:
    # #     left = s[::-1].count(">", firstLeft) * s[::-1].count("<")


    
    return salutes*2



# <<>><
# 1 < after the first > (2 >'s) 2 * 1 = 2
# <<>><<>>
