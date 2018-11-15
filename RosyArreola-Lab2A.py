class Node:
    def __init__(self,data):
        self.next = None
        self.prev = None
        self.data = data

class EmployeeID:

    def __init__(self):
        self.head = None

    def __len__(self):
        return self.length

    # Add new item to the beginning of the list
    def insert(self, new_data):
        new_id = Node(data = new_data)
        new_id.next = self.head
        new_id.prev = None

        if self.head is not None:
            self.head.prev = new_id

        self.head = new_id

    # Add new item to the end of the list
    def append(self, new_data):
        new_id = Node(data = new_data)
        last = self.head
        new_id.next = None

        if self.head is None:
            self.head = new_id
            return

        while (last.next is not None):
            last = last.next

        last.next = new_id
        new_id.prev = last

    # Print list in ascending order
    def printList(self, node):
        while node is not None:
            # Print on separate lines
            print(node.data)
            #Print on same line
            # print(node.data, end=" ")
            last = node
            node = node.next

    def printItem(self, node):
        print(node.data)

    def toInt(self, node):
        node.data = int(node.data)
        return node.data

    # Search for key
    def search(self, key):
        curr = self.head
        isFound = False
        counter = 0
        while curr != None:
            if curr.data == key:
                isFound = True
                counter = counter +1
            curr = curr.next
        #if counter > 1:
            #print("ID #", key, " found ", counter, " times")
        return isFound

# Read each line and create linked list
def read_lines(file_name, h):
    list = h
    with open(file_name, 'r') as textFile:
        for line in textFile:
            line = line.rstrip("\n")
            list.append(line)
    return h

# Compare all items using search()
def compareAll(llist):
    while llist.head != None:
        key = llist.head.data
        llist.search(key)
        llist.head = llist.head.next

def bubbleSort(llist):
    h = llist
    new_h = h
    curr = h
    a = h
    temp = h
    while h.head.next != None:
        curr.head = h.head.next
        prev = h
        a.head = curr.head.next
        while a != None:
            if (a.head.data < curr.head.data):
                temp.head = a.head.next
                a.head.next = prev.head.next
                prev.head.next = curr.head.next
                curr.head.next = temp.head
                prev = a
                a = temp
            else:
                a.head = a.head.next
                curr.head = curr.head.next
                prev.head = prev.head.next
        h.head = h.head.next
    new_h.head = new_h.head.next

def mergeSort(llist):
    if llist is None or llist.head.next is None:
        return llist
    left_h = splitList(llist)
    right_h = splitList(llist)

    left = mergeSort(left_h)
    right = mergeSort(right_h)
    return mergeLists(left, right)

def splitList(llist):
    if llist is None or llist.head.next is None:
        left_h = llist
        right_h = None
        return left_h, right_h
    else:
        mid = llist
        front = llist.head.next

        while front is not None:
            front = front.head.next
            if front is not None:
                front = front.head.next
                mid = mid.head.next
        left_h = llist
        right_h = mid.head.next
        mid.head.next = None
        return left_h, right_h

def mergeLists(left, right):
    h = None
    curr = h

    while left and right:
        if left.head.data < right.head.data:
            curr.head.next = left
            left = left.head.next
        else:
            curr.head.next = right
            right = right.head.next
        curr = curr.head.next

    if left is None:
        curr.head.next = right
    elif right is None:
        curr.head.next = left
    return h.head.next

# Create activision list
activision = EmployeeID()
activision = read_lines('activision.txt', activision)

# Create vivendi list
vivendi = EmployeeID()
vivendi = read_lines('vivendi.txt', vivendi)

# Append both lists
full_list = activision
full_list.append(vivendi)
compareAll(full_list)
full_list.printList(full_list.head)
bubbleSort(full_list)

### TRAVERSAL
n = EmployeeID()
n.head = full_list.head.next
n.printItem(n.head)
n.head = n.head.prev
n.printItem(n.head)
