# recreated, may not match the original!

def solution(x, y):
    bottom = bottomRow( 0, 1 )
    for i in range(x-1):
        bottom = bottom.next()
    
    if y == 1:
        return bottom.value
    up = bottom.up()

    for i in range(y-2):
        up = up.up()
    return up.value

# to create the initial row: do bottomRow( 0, 1 )
class bottomRow():
    def __init__(self, before, incr):
        self.value = before+incr
        self.incr = incr
    def next(self):
        return bottomRow(self.value, self.incr+1)
    def up(self):
        return theRest(self.value, self.incr)

class theRest():
    def __init__(self, before, incr):
        self.value = before+incr
        self.incr = incr
    def up(self):
        return theRest(self.value, self.incr+1)


print(solution(5, 10))
