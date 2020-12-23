'''
Singly linked list implementation
Adapted from Usman Malik's implementation on Stackabuse.
Thanks Usman.
'''
class Node:
    def __init__ (self, data):
        self.item = data
        self.ref = None

class LinkedList:
    def __init__ (self):
        self.start_node = None

    def traverse_list (self):
        if self.start_node is None:
            print('List has no element')
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.ref
    
    def insert_at_start (self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node #set reference of last node to newly created node
    
    #dynamic item addition: after
    def insert_after_item (self, x, data):
        n = self.start_node

        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print('Item not in list')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    #dynamic item addition: before
    def insert_before_item(self, x, data):
        #check if node exists
        if self.start_node is None:
            print("List has no element")
            return
        
        if x == self.start_node.item:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return
        
        n = self.start_node
        print(n.ref)
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("Item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_at_index (self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
        i = 1
        n = self.start_node
        while i < index-1 and n is not None:
            n = n.ref
            i = i+1
        if n is None:
            print("Index out of bound")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def count_list(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        count = 0
        while n is not None:
            count += 1
            n = n.ref
        return count
    
    def search_for_item(self, x):
        if self.start_node is None:
            return 0
        n = self.start_node
        while n is not None:
            if n.item == x:
                print('Item found')
                return True
            n = n.ref
        print('Item not found')
        return False
    
    #creating linkedlists by users
    def create_list(self):
        num_node = int(input('Enter num of nodes for creation: '))
        if num_node == 0:
            return
        for i in range(num_node):
            value_of_node = int(input('Enter node value: '))
            self.insert_at_end(value)
    
    #deleting from end
    def delete_end(self):
        if self.start_node is None:
            print('No element to delete')
        else:
            n = self.start_node
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    #deleting nodes from the start
    def delete_start(self):
        if self.start_node is None:
            print('No element to delete')
            return
        
    
    #deleting nodes by value
    def delete_by_value(self, x):
        if self.start_node is None:
            print("List has no element to delete")
            return
    
        #deleting first node
        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return
        
        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        
        if n.ref is None:
            print('Item not found in the list')
        else:
            n.ref = n.ref.ref
    
    #reversing list 
        

#testing insertion functions
new_linked_list = LinkedList()
new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(10)
new_linked_list.insert_at_end(15)
new_linked_list.insert_at_start(20)
new_linked_list.insert_after_item(10, 11)
new_linked_list.insert_at_index(3,6)
new_linked_list.insert_before_item(15, 100)
new_linked_list.traverse_list()
new_linked_list.count_list()
new_linked_list.search_for_item(11)

#testing deletion functions
print('Deletion functions activate')
new_linked_list.delete_start()
new_linked_list.delete_end()
new_linked_list.delete_by_value(100)

print('Travesring list')
new_linked_list.traverse_list()