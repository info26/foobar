# this is not the script that i submitted to foobar,
# because python2 has some compatibility issues with 
# range, so i replaced it with a list.
def solution(a,b):
    # get numbers from grid
    # if only it was this easy, and the code below didn't exist
    gr = grid(a, b)
    
    nums = gr.getNumbers()
    #print(nums)
    return rangeXor(nums)



class grid():
    def __init__(self, start, length):
        self.start = start
        self.length = length
    def getNumbers(self):
        # cycle through numbers
        ans = []
        num = self.start
        for i in range(self.length, 0, -1):
            thisRow = leftRow(num, self.length - (self.length - i))
            ans.append(thisRow.right())
            num += self.length
        return ans


class leftRow():
    def __init__(self, thisValue, length):
        self.thisValue = thisValue
        self.length = length
    def right(self):
        return range(self.thisValue, self.thisValue + self.length - 1)


def intermediateRangeXor(ran):
    return getXorRange(ran.start - 1) ^ getXorRange(ran.stop)


def getXorRange(a):
    opt = a % 4
    if opt == 0:
        return a
    elif opt == 1:
        return 1
    elif opt == 2:
        return a + 1
    elif opt == 3:
        return 0


# range xor
def rangeXor(ran):
    ans = []
    for i in ran:
        ans.append(
            intermediateRangeXor(i)
        )
    #print(ans)
    return fastXor(ans)


# This is only an experiment, probably
# it will fail miserably!!
# Oh great, this has another use!
def fastXor(l):
    # 
    unpacked = {}
    for i in l:
        # convert to binary
        binary = bin(i)
        binary = binary[2:][::-1]
        #print(binary)
        for b in range(len(binary)):
            if b not in unpacked:
                unpacked[b] = 0
            if binary[b] == "1":
                unpacked[b] += 1
    #print(unpacked)
    binaryStr = "0b"
    for i in unpacked:
        if (unpacked[i] % 2 == 1):
            # should add one
            binaryStr = binaryStr[:2] + "1" + binaryStr[2:]
        else:
            binaryStr = binaryStr[:2] + "0" + binaryStr[2:]
    #print(binaryStr)
    return int(binaryStr, base=2) # tada!


print(solution(0, 3))