#Singly Linked List

# Implement Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Singly_Linked_List:
    def __init__(self):
        self.head = None   # start with empty list

    # Insert at the beginning
    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at the end
    def insert_tail(self, data):
        new_node = Node(data)
        if not self.head:               #check
            self.head = new_node
            return
        last = self.head                #start by setting a pointer (last) to the first node (head) of the list.
        while last.next:                
            last = last.next            #traversing the list untill find the last node
        last.next = new_node            #adding the new node to the end.

    #insert after a given value
    def insert_t_value(self,prev_data,data):
        current = self.head
        while current and current.data != prev_data:
            current = current.next
        if not current:
            print("previous data not found")
            return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    #delete a node by value
    def delete_by_value(self,data):
        current = self.head
        prev = None
        # case  -> if head node itself hold the data
        if current and current.data == data:
            self.head = current.next
            return
        # case -> search for the data to delete
        while current and current.data != data:
            prev = current
            current = current.next
        # case -> data was not found
        if not current:
            print("Value not found")
            return
        # unlink the node from list
        prev.next = current.next

    #search by value
    def search_by_value(self,data):
        #Start from beginning of the list
        current = self.head
        #Loop through the entire list
        while current:
            #Check if current node matches value
            if current.data == data:
                return True
            #Move to next node
            current = current.next
        return False
    
    #delete by the position(index)
    def delete_at_index(self, index):
        if not self.head:
            return  # List is empty
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(index - 1):
            if not current.next:
                return  # Index out of bounds
        current = current.next
        if current.next:
            current.next = current.next.next

    # Display the list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


sll = Singly_Linked_List()

# Use the instance
# insert in head
sll.insert_head(1)
sll.insert_head(2)
sll.insert_head(3)
sll.insert_head(4)
#insert in tail
sll.insert_tail(0)
sll.insert_tail(2)
sll.insert_tail(3)
sll.insert_tail(4)
# insert after value
sll.insert_t_value(3,0.3)
#delete by value
sll.delete_by_value(0.3)
#display
sll.display()
#search by value
print(sll.search_by_value(1))
#delete by position
sll.delete_at_index(2)
sll.display()
