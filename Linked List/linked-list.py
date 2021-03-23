class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        return

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        return
    
    def add_node(self, item):
        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        
        self.tail = item
        return
    
    def del_node(self, delItem):
        print('Delete element '+str(delItem)+': ')
        prevNode = None
        currentNode = self.head
        while currentNode:   
            if currentNode.data == delItem and prevNode is not None:
                prevNode.next = currentNode.next
                break

            prevNode = currentNode
            currentNode = currentNode.next
    
    def show_all_elements(self):
        print('Elements in the linked list:')
        currentNode = self.head
        while currentNode:   
            print(currentNode.data)
            currentNode = currentNode.next

            
    
    def reverse(self):
        print('Reverse linked list')
        currentNode = None
        prevNode = None
        nextNode = self.head
        self.tail = self.head
        while nextNode is not None:            
            currentNode = nextNode               
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
        self.head = currentNode      
        
        return



node1 = ListNode(24)
list1 = SingleLinkedList()
list1.add_node(node1)
list1.add_node(33)
list1.add_node(55)
list1.add_node(21)
list1.show_all_elements()
list1.del_node(33)
list1.show_all_elements()


list1.reverse()
list1.show_all_elements()
