import datetime
def solution(s):
    
    sum = 0
    for i in range(2, getMax(s)):
        #print("The below is a top level call. ")
        sum += wrap.call(s, i, s)
    return sum

def getMax(f):
    counter = 0
    for i in range(0, f + 1):
        counter += i
        if (counter > f):
            return i
    return f

def f(bricks, stairs, mheight):
    #print("f ( " + str(bricks) + " , " + str(stairs) + " , " + str(mheight) + " )")
    # if bricks, stairs, or mheight (not exclusive) == 0, a stair
    # can't be built. 
    check = [
        bricks == 0,
        stairs == 0,
        mheight == 0
    ]
    if check.count(True) >= 1:
        # whoops!
        # print("Returning 0  " + str(check) + str(check.count(True) <= 1))
        #print("return 0")
        return 0
    if (
        stairs == 1 and
        bricks <= mheight
    ):
        
        #print("returning 1")
        return 1

    
    
    
    sum = 0
    for i in range(1, bricks):
        if i > mheight:
            continue
        sum += wrap.call(bricks - i , stairs - 1, i - 1)
    return sum

class memoizationWrapper:
    def __init__ (self, func):
        self.func = func
        self.memoed = {}
    def call(self, a, b, c):
        if (a,b,c) in self.memoed:
            #print("already calculated: " + str((a,b,c)))
            return self.memoed[(a,b,c)]
        result = self.func(a,b,c)
        self.memoed[(a,b,c)] = result
        #print(self.memoed)
        return result



wrap = memoizationWrapper(f)

start = datetime.datetime.now()

print(solution(200))

end = datetime.datetime.now()

print(end - start)