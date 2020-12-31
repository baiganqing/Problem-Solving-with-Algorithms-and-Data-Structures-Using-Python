class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head  #最初的none就是尾部的none
        self.head = temp

    def length(self):
        current = self.head
        count = 0
        while current != None:
            current = current.getNext()
            count = count + 1

        return count

    def search(self, item):
        found = False
        current = self.head
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        found = False
        previous = None
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        current = self.head
        previous = None
        temp = Node(item)
        while current != None:
            previous = current
            current = current.getNext()
        if previous == None:
            self.head = temp
        else:
            previous.setNext(temp)

    def index(self, item):
        pos = 0
        current = self.head
        while current.getData() != item:
            current = current.getNext()
            pos = pos + 1

        return pos

    def insert(self, pos, item):
        previous = None
        current = self.head
        index = 0
        temp = Node(item)
        while index != pos:
            previous = current
            current = current.getNext()
            index = index + 1

        if previous != None:
            previous.setNext(temp)
            temp.next = current
        else:
            self.head = temp
            temp.next = current
    def pop(self, pos=None):
        current = self.head
        previous= None
        index = 0
        stop = False
        while not stop:
            previous = current
            current = current.getNext()
            index += 1
            if pos == None and current.getNext() == None:
                previous.setNext(None)
                stop = True
            elif pos == index:
                if previous != None:
                    previous.setNext(current.getNext())
                else:
                    self.head = current.getNext()
                stop = True
        return current.getData()


'''
#test
mylist = UnorderedList()

mylist.add(14)
mylist.add(12)
mylist.add(24)
mylist.add(32)
mylist.add(34)
mylist.add(56)

print('列表长度为{}'.format(mylist.length()))
print('列表有 {} 个节点'.format(mylist.length()))
print('数据 32 的索引是 {}'.format(mylist.index(32)))
mylist.insert(0, 90)
print('现在数据 32 的索引是 {}'.format(mylist.index(32)))
print('移除最后一节点{}'.format(mylist.pop()))
print('移除后列表长度为{}'.format(mylist.length()))
print('移除索引4处的节点{}'.format(mylist.pop(4)))
'''


class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def length(self):
        current = self.head
        count = 0
        while current != None:
            current = current.getNext()
            count = count +1

        return count

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def search(self, item):
        found = False
        stop = False
        current = self.head
        #找到，没到头没找到，到头了没找到
        while not stop and not found and current != None :
            if current.getData() > item:
                stop = True
            elif current.getData() < item:
                current = current.getNext()
            else:
                found = True

        return found

    def add(self, item):
        stop = False
        current = self.head
        previous = None
        while current != None and not stop: #没找新节点的位置
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            previous.setNext(temp)
            temp.setNext(current)

    def index(self, item):
        found = False
        count = 0
        current = self.head
        while not found:
           if current.getData() == item:
               found = True
           else:
               current = current.getNext()
               count += 1
        return count

    def pop(self, pos = None):
        current = self.head
        previous = None
        index = 0
        stop = False
        while not stop:
            previous = current
            current = current.getNext()
            index += 1
            if pos == None and current.getNext() == None:
                previous.setNext(None)
                stop = True
            elif pos == index:
                if previous != None:
                    previous.setNext(current.getNext())
                else:
                    self.head = current.getNext()
                stop = True

        return current.getData()












