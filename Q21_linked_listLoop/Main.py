class Node :
    data  = None
    next_node = None
    def __init__(self,data):
        self.data = data 
        next_node = None
    def __str__(self):
        return str(self.data)
    def setNext(self,nextNode):
        self.next_node=nextNode
class LinkedList :
    head = None
    def __init__ (self,head):
        self.head = head
    def append(self, nextNode):
        tmp =self.head
        while tmp.next_node != None:
            tmp = tmp.next_node
        tmp.setNext(nextNode)
    def __str__(self) :
        while self.head.next_node !=None :
            print (self.head)
            self.head = self.head.next_node
        print(self.head)
        return "\0"
def sSearch(node) :
    return node.next_node
def fSearch(node) :
    return node.next_node.next_node
def findLOOP(llist,turtle, rabbit):
    if turtle == rabbit :
        tmpHead = llist.head
        while tmpHead != turtle:
            tmpHead  = tmpHead.next_node
            turtle = turtle.next_node
        print(tmpHead)

    else :
        findLOOP(test,sSearch(turtle),fSearch(rabbit))

if __name__ =="__main__":
    a =Node(1)
    b =Node(2)
    c =Node(3)
    d = Node (4)
    e = Node(5)
    f = Node(6)
    g = Node(7)
    test = LinkedList(a)
    test.append(b)
    test.append(c)
    test.append(d)
    test.append(e)
    test.append(f)
    test.append(g)

    g.setNext(b)
    t= sSearch(test.head)
    r = fSearch(test.head)
    
    findLOOP(test,t,r)
