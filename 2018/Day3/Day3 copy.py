#Day3 - problem with wires
import copy
import sys
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def makeMove(point, move):
    newPoint = copy.deepcopy(point)
    if "U" in move:
        newPoint.y = point.y+int(move[1::])
    elif "D" in move:
        newPoint.y = point.y-int(move[1::])
    elif "L" in move:
        newPoint.x = point.x-int(move[1::])
    elif "R" in move:
        newPoint.x = point.x+int(move[1::])
    return newPoint

def checkParallel(A,B,C,D):
    if ((A.x == B.x and C.x == D.x) or (A.y == B.y and C.y == D.y)):
        return True

def intersection(A,B,C,D):
    nA = Point(min(A.x,B.x),min(A.y,B.y))
    nB = Point(max(A.x,B.x),max(A.y,B.y))
    nC = Point(min(C.x,D.x),min(C.y,D.y))
    nD = Point(max(C.x,D.x),max(C.y,D.y))
    if nA.x == nB.x:
        if ((nA.x > nC.x and nA.x < nD.x) and (nC.y > nA.y and nC.y < nB.y)):
            return Point(nA.x,nC.y)
    elif nA.y == nB.y:
        if ((nC.x > nA.x and nC.x < nB.x) and (nA.y > nB.y and nA.y < nD.y)):
            return Point(nC.x,nA.y)
    
def manhattanDist(A,B):
    return abs(B.x-A.x) + abs(B.y-A.y)

#reading input files with instructions
with open("/home/jazzhoo/Dropbox/Code/AdventOfCode/Day3/wireA_input", "r") as f:
    for line in f.readlines():
        wireA_instructions = [x for x in line.split(',')]
with open("/home/jazzhoo/Dropbox/Code/AdventOfCode/Day3/wireB_input", "r") as f:
    for line in f.readlines():
        wireB_instructions = [x for x in line.split(',')]

#building lists of poits
wireA = [Point(0,0)]
for i in range(0,len(wireA_instructions)):
    wireA.append(makeMove(wireA[i],wireA_instructions[i]))

wireB = [Point(0,0)]
for i in range(0,len(wireB_instructions)):
    wireB.append(makeMove(wireB[i],wireB_instructions[i]))

#checking the intersections
listOfPoints =[]
for i in range(1,len(wireB)):
    for j in range(1,len(wireA)):
       if not(checkParallel(wireB[i-1],wireB[i],wireA[j-1],wireA[j])):
           tempPoint=intersection(wireB[i-1],wireB[i],wireA[j-1],wireA[j])
           if tempPoint != None:
               listOfPoints.append(tempPoint)
distance = sys.maxsize
for point in listOfPoints:
    print(listOfPoints.index(point), ':',point.x, point.y, "dist:", manhattanDist(Point(0,0),point))
for point in listOfPoints:
    if manhattanDist(Point(0,0),point) < distance:
        distance = manhattanDist(Point(0,0),point)
print ("min distance", distance)        
    
