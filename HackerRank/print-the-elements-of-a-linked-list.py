class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = node()

    def insert(self, data):
        new_node = node(data)
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            print(cur_node.data)
        #     elems.append(cur_node.data)
        # print(elems)


l = linkedList()
[l.insert(int(input())) for i in range(int(input()))]
l.display()

