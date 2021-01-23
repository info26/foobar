import collections
# map here is more like a "source" for information for the nodes
# the nodes generate the the next nodes
class solpos():
    def __init__(self, brokenWall, maze, x, y):
        self.x = x
        self.y = y
        self.brokenWall = brokenWall
        self.maze = maze
    def __str__(self):
        #return f"{self.x} - {self.y}"
        return ""
    def __repr__(self):
        return self.__str__()
    def __hash__(self):
        return hash((self.x, self.y, self.brokenWall))
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.brokenWall == other.brokenWall
    def neighbor(self):
        neighbors = set()
        x = self.x
        y = self.y
        req = (
            (x-1, y ),
            (x+1, y ),
            (x,   y-1),
            (x,   y+1)
        )
        for i in req:
            dat = self.maze.get(i[0], i[1])
            if dat == -1:
                continue
            if dat == 1 and self.brokenWall == True:
                continue
            if self.brokenWall == True:
                brokenWall = True # you can't ever get your power back!
            elif self.brokenWall == False:
                if dat == 1:
                    brokenWall = True
                elif dat == 0:
                    brokenWall = False
            else:
                raise BaseException("what?")

            neighbors.add(
                solpos(brokenWall, self.maze, i[0], i[1])
            )
        return neighbors 
class sol():
    def __init__(self, mapp, fakeOne):
        self.fake = fakeOne
        self.map = mapp
    def solve(self):
        initNode = solpos(False, self, len(self.map[0])-1, len(self.map)-1)
        distances = {initNode: 1}
        q = collections.deque() # haha, "q" sounds like "queue"
        q.append(initNode)

        while q:
            
            processing = q.popleft()

            if processing.x == 0 and processing.y == 0:
                return distances[processing]
            
            for neighbour in processing.neighbor():
                if neighbour not in distances:
                    distances[neighbour] = distances[processing] + 1
                    q.append(neighbour)
        
        #print("RETURNING NOTHING!")

    def get(self, x, y):
        
        if (x, y) == self.fake:
            return 0
        if x < 0 or y < 0:
            return -1
        try:
            return self.map[y][x] # it's kinda weird
        except:
            return -1 # doesn't exist
def solveMaze(mapp, fake):
    a = sol(mapp, fake)
    res = a.solve()
    if res == None:
        return 99999999
    return res
class solver():
    def __init__(self, mapp):
        self.map = mapp
    def get(self, x, y):
        if x < 0 or y < 0:
            return 1
        try:
            return self.map[y][x]
        except:
            return 1
    def countConnections(self, x, y):
        connections = 0
        req = [
            self.get(x-1, y), 
            self.get(x+1, y), 
            self.get(x, y-1), 
            self.get(x, y+1)
        ]
        for i in req:
            if i == 0:
                # ooh, available space!
                connections += 1
        return connections
    def getOnes(self):
        oneNodes = set()
        for a in range(len(self.map)):
            for b in range(len(self.map[a])):
                if self.map[a][b] == 1:
                    oneNodes.add((b,a))
        return oneNodes
    def solve(self):
        maxx = 999999999999
        maxx = solveMaze(self.map, (-1, -1))
        return maxx
def solution(m):
    e = solver(m)
    return e.solve()

