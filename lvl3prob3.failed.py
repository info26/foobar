import collections, copy

class connection:
    def __init__(self, desc):
        self.desc = desc
        pass
    def __str__(self):
        return "connection." + self.desc.upper()
    def __repr__(self):
        return "connection." + self.desc.upper()
class connection: # hopefully overwriting them is fine!
    def __init__(self):
        raise Exception("Can't initialize this class!")
    up = connection("up")
    right = connection("right")
    down = connection("down")
    left = connection("left")
class maze(): # TODO: caching? if it's too slow. 
    def __init__(self, mapp): #
        self.map = mapp
        self.nodeMap = {}
        self.zeroList = []
        self.fakeOne = (-1, -1)
        self.cache = {}
    #@profile
    def getDataAt(self, x, y):
        if (x,y) == self.fakeOne:
            return 0
        if x < 0 or y < 0: # watch out!
            return 1
        try:
            return self.map[y][x]
        except:
            return 1 # pretend there is a wall there
    def getNodeAt(self, x, y):
        return (x,y)
    #@profile
    def getAvailPaths(self, x, y):
        try:
            return self.cache[(x,y)]
        except:
            pass
        connections = set()
        req = [
            (self.getDataAt(x-1, y), connection.left,  x-1, y), 
            (self.getDataAt(x+1, y), connection.right, x+1, y), 
            (self.getDataAt(x, y-1), connection.down,  x,   y-1), 
            (self.getDataAt(x, y+1), connection.up,    x,   y+1)
        ]

        for i in req:
            if i[0] == 0:
                # ooh, available space!
                connections.add(self.getNodeAt(i[2], i[3]))
        self.cache[(x,y)] = connections

        return connections
    def getStart(self):
        return self.getNodeAt(len(self.map)-1, len(self.map[0])-1)
    def getEnd(self):
        return self.getNodeAt(0, 0)
    def getOnes(self):
        oneNodes = set()
        for a in range(len(self.map)):
            for b in range(len(self.map[a])):

                if self.map[a][b] == 1:
                    oneNodes.add((b,a))
        return oneNodes
    def removableOnes(self):
        # can be removed if availpaths is > 2. 
        removable = set()
        for testNode in self.getOnes():
            if len(self.getAvailPaths(testNode[0], testNode[1])) >= 2:
                removable.add(testNode)
        return removable
    def clearBadCache(self, fakeOne=None):
        if fakeOne == None:
            fakeOne = self.fakeOne
        x = fakeOne[0]
        y = fakeOne[1]
        try:
            del self.cache[(x-1, y)]
        except:
            pass
        try:
            del self.cache[(x+1, y)]
        except:
            pass
        try:
            del self.cache[(x,   y-1)]
        except:
            pass
        try:
            del self.cache[(x,   y+1)]
        except:
            pass



#@profile
def BFS(maze):
    start = maze.getStart()
    end = maze.getEnd()
    """visitlog = [False] * len(maze.map[0]) * len(maze.map)
    visitlog[start[0]][start[1]] = True

    queue = collections.deque()

    queue.append((start, 0))"""
    visited = [[False] * len(maze.map[0])] * len(maze.map)
    queue = collections.deque()


    queue.append([1, start])
    while len(queue) > 0: # as long as there are paths to try!

        primarySource = queue.popleft()
        
        lastNode = primarySource[1] # where is the end of the "path" right now?
        if lastNode == end: # oh great! we're there!
            return primarySource[0]
        for node in maze.getAvailPaths(lastNode[0], lastNode[1]):
            tryingPath = primarySource.copy()

            #if node in tryingPath[0]:
            #    continue # don't want to loop!
            if visited[node[0]][node[1]]:
                continue
            visited[node[0]][node[1]] = True
            tryingPath[0] += 1
            tryingPath[1] = node
        
           
            queue.append(tryingPath) # let's try this the next time!
    #print(queue)
    return 99999999

    
def solution(mazeSource):
    maxx = 999999999999
    maz = maze(mazeSource)
    maxx = BFS(maz)
    for removable in maz.removableOnes():
        maz.clearBadCache(maz.fakeOne)
        maz.fakeOne = removable
        maz.clearBadCache()
        res = BFS(maz)
        if res < maxx:
            maxx = res
    return maxx
    

    



print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))