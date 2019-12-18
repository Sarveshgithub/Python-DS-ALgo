# Linked List Implementation using class
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node

    def length(self):
        cur_node = self.head
        count = 0
        while cur_node.next != None:
            count += 1
            cur_node = cur_node.next
        return count

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("ERROR: Index out of range!")
            return None
        cur_index = 0
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            if cur_index == index:
                return cur_node.data
            cur_index += 1
    
    def 


l = linked_list()
l.append(1)
l.append(2)
l.display()
l.length()
print(l.get(1))

