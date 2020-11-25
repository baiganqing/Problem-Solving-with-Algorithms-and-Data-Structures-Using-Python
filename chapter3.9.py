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

























