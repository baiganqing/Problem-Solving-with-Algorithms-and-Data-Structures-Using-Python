from turtle import *
class Stack:
    def __init__(self):
        self.items = []
    def empty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
#递归求和
def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        #int 数学运算
        return numList[0] + listsum(numList[1:])

#递归进制转换
'''
def toStr(n, base):
    convertString = '0123456789ABCDEF'
    if n < base:
        return convertString[n] #最后一位
    else:
        return toStr(n//base, base) + convertString[n%base]
'''

#栈帧
rStack = Stack()
def toStr(n, base):
    convertString = '0123456789ABCDEF'
    if n < base:
        rStack.push(convertString[n])
    else:
        rStack.push(convertString[n%base])
        toStr(n//base,base)

myTurtle = Turtle()
myWin = myTurtle.getscreen()

def drawSpiral(myTurtle, linLen):
    if linLen > 0 :
        myTurtle.forward(linLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, linLen-5)

#drawSpiral(myTurtle, 100)
#myWin.exitonclick()
def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(25)
        tree(branchLen-15,t)
        t.left(50)
        tree(branchLen-15, t)
        t.right(25)
        t.backward(branchLen)
'''
t = Turtle()
myWin = t.getscreen()
t.left(90)
t.up()
t.backward(300)
t.down()
t.color('green')
tree(110,t)
myWin.exitonclick()
'''
#谢尔平斯基三角形
def drawTriangle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up() #画笔抬起
    myTurtle.goto(points[0])
    myTurtle.down() #画笔落下
    myTurtle.begin_fill()
    myTurtle.goto(points[1])
    myTurtle.goto(points[2])
    myTurtle.goto(points[0])
    myTurtle.end_fill()

def getMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2) #返回中央点

def sierpinski(points, degree, myTurtle):
    colormap = ['blue', 'red', 'green', 'white',
                'yellow', 'violet', 'orange']
    drawTriangle(points, colormap[degree], myTurtle)
    if degree > 0:
        sierpinski([points[0], getMid(points[0], points[1]),getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1], getMid(points[0], points[1]),getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2], getMid(points[0], points[2]), getMid(points[1], points[2])],
                   degree - 1, myTurtle)
'''
myTurtle = Turtle() #turtle class
myWin = myTurtle.getscreen()
myPoints = [(-500, -250), (0, 500), (500, -250)]
sierpinski(myPoints, 5, myTurtle)
myWin.exitonclick()
'''
def moveDisk(fp, tp):
    print('moving disk from %d to %d \n'%(fp,tp))
def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, withPole, toPole, fromPole)
'''
fromPole = 1
toPole = 2
withPole = 3
moveTower(6, fromPole, toPole, withPole)
'''
def recMC(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change-i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins
#print(recMC([1,5,10,25],26))



