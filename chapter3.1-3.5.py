from queue import LifoQueue
import string
import random

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

class Queue:
    def __init__(self):
        self.items =[]

    def enqueue(self,item):
        self.items.insert(0, item)

    def dequeque(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

class Dequeue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)




##############（ 匹配算法
def parChecker(string):
    s = LifoQueue()
    index = 0
    balanced = True

    while index < len(string) and balanced:
        if string[index] == "(":
            s.put(string[index])
        else:
            if s.empty():
                balanced = False
            else:
                s.get()
        index = index + 1
    if balanced and s.empty():
        return True
    else:
        return False

#test = '(((())))'
#print(parChecker(test))

###########  {[(  匹配符号（普通情况）
def match(open, close):
    opens = '[{('
    closes = ']})'
    return opens.index(open) == closes.index(close)

def parChecke_2(string):
    s = LifoQueue()
    index = 0
    balanced = True

    while index < len(string) and balanced:
        item = string[index]
        if item in "({[":
            s.put(item)
        else:
            if s.empty():
                balanced = False
            else:
                top = s.get()
                if not match(top, item):
                    balanced = False
        index = index + 1
    if balanced and s.empty():
        return True
    else:
        return False
#test = '(([{()})))'
#print(parChecker(test))

########'除以二'算法 转换为 二进制数字
def dividedBy2(dec):
    remstack = LifoQueue()
    while dec > 0:
        remstack.put(dec % 2)
        dec = dec // 2

    binString = ''
    while not remstack.empty():
        binString = binString + str(remstack.get())

    return binString

#test = 233
#print(dividedBy2(test))


#######十进制转为任意进制
def baseConverter(dec, base):
    digits = '0123456789ABCDEF'#字符串和列表一样，只不过没法删除
    remstack = LifoQueue()
    while dec > 0:
        remstack.put(dec % base)
        dec = dec // base

    binString = ''
    while not remstack.empty():
        binString = binString + digits[remstack.get()]

    return binString
#test = 936382
#print(baseConverter(test, 16))

def infixtopostfix(infixexpr):
    prec = {'*':3, '/':3, '+':2, '-':2, '(':1}
    opStack = Stack()
    postfixList = []

    tokenList = []#待处理终须表达式符号
    for i in infixexpr:
        tokenList.append(i)

    for token in tokenList:
        # 大小写字母
        if token in string.ascii_letters:
            postfixList.append(token)

        elif token == '(':
            opStack.push(token)

        elif token == ')':
            toptoken = opStack.pop()
            while toptoken != '(':
                postfixList.append(toptoken)
                toptoken = opStack.pop()
        else:
            while (not opStack.empty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.empty():
        postfixList.append(opStack.pop())
    return ''.join(postfixList)
#test
#print(infixtopostfix("(A+B)*(C+D)"))
#print(infixtopostfix("(A+B)*C"))
#print(infixtopostfix("A+b*C"))
def doMath(op1, op2, op):
    if op == '*':
        return op1*op2
    elif op== '+':
        return op+op2
    elif op == '-':
        return op2-op1
    else:
        return op2/op1

def postfixEval(postfixExpr):
    operandStack = Stack()

    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in string.digits:
            operandStack.push(int(token))
        else:
            operand1 = operandStack.pop()
            operand2 = operandStack.pop()
            result = doMath(operand1, operand2, token)
            operandStack.push(result)

    return operandStack.pop()

#test
#print(postfixEval('6 2 / 4 *'))

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeque())
        simqueue.dequeque()
    return simqueue.dequeque()
#namelist = ['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad']
#print(hotPotato(namelist, 7))


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1,21)
    def getPages(self):
        return self.pages
    def getStamp(self):
        return self.timestamp
    def waitTime(self, currenttime):
        return currenttime - self.timestamp

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaning = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaning = self.timeRemaning -1
            if self.timeRemaning <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def stateNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaning = newtask.getPages() * 60/self.pagerate



def simulation(numSeconds, pagePerMinute):
    labprinter = Printer(pagePerMinute)
    printQueue = Queue()
    waitingtimes = []
    for currentSecond in range(numSeconds):

        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)#这里的task应该是一个地址

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeque()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.stateNext(nexttask)
        labprinter.tick()

    averageWait = sum(waitingtimes)/len(waitingtimes)
    print('Average Wait {} secs {} tasks remaining'.format(averageWait, printQueue.size()))

def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False
#test
#for i in range(10):
#   simulation(3600,5)
def palchecker(astring):
    chardequeue = Dequeue()

    for item in astring:
        chardequeue.addRear(item)

    stillEqual = True

    while stillEqual and chardequeue.size() > 1:
        first = chardequeue.removeFront()
        last = chardequeue.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual
#test
#print(palchecker('raddar'))


