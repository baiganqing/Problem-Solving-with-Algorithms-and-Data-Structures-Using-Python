import string
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

#######  1.
def dividedBy2(dec):
    remstack = Stack()
    while dec > 0:
        remstack.push(dec % 2)
        dec = dec // 2

    binstring = ''
    while not remstack.empty():
        binstring = binstring + str(remstack.pop())

    return binstring
'''
print(dividedBy2(17))
print(dividedBy2(45))
print(dividedBy2(96))
'''
#######  2.
def findNextEntity(str):
    res = ''
    opStack = Stack()
    for i in str:
        if i == '(':
            opStack.push(i)
        elif i == ')':
            opStack.pop()
        res = res + i
        if opStack.empty():
            break
    if res == '':
        res = False  #?

    return res

def addCompleteBrackets(expr):
    operators = []
    entities = []
    i = 0
    while i < len(expr):
        if expr[i] in '+-*/':
            if expr[i] in '+-':
                operators.append(expr[i])
                i += 1
            elif expr[i] in '*/':
                tmp = entities[-1]
                entities.remove(tmp)
                nextent = findNextEntity(expr[i+1:])
                entities.append("(" + tmp + expr[i] + nextent + ")")
                i += (len(nextent) + 1)
        else:
            temp = findNextEntity(expr[i:])
            i += len(temp)
            entities.append(temp)

    while len(entities) > 1:
        entities[0] = "(" + entities[0] + operators[0] + entities[1] + ")"
        operators.remove(operators[0])
        entities.remove(entities[1])
    return entities[0]

def infixtoprefix(expr):
    expr = addCompleteBrackets(expr)
    print(expr)
    prefixList = []
    temp = []
    for i in expr:
        if i == ')' and len(temp) >= 2:
                last = temp.pop()
                first = temp.pop()
                prefixList.append(first)
                prefixList.append(last)
        elif i in '+-*/':
            prefixList.append(i)
        elif i in string.ascii_letters:
            temp.append(i)

    return ''.join(prefixList)
'''
print(infixtoprefix('(A+B)*(C+D)*(E+F)'))
print(infixtoprefix('A+((B+C)*(D+E))'))
print(infixtoprefix('A*B*C+E+F'))
'''

def infixtopostfix(expr):
    expr = addCompleteBrackets(expr)
    print(expr)
    postfixList = []
    left = Stack()
    temp = []
    for i in expr:
        if i == ")":
            postfixList.append(temp.pop())
        elif i in '+-*/':
            temp.append(i)
        elif i in string.ascii_letters:
            postfixList.append(i)

    return ''.join(postfixList)
print(infixtopostfix('(A+B)*(C+D)*(E+F)'))