class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class singlyLL:
    def __init__(self):
        self.head = None
        
    def InsertAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insertAtIndex(self, data, index):
        if index == 0:
            self.InsertAtBegin(data)
            return
        position = 0
        current_node = self.head
        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.next
        
        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")
            
        def insertAtEnd(self, data):
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                return
            
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node