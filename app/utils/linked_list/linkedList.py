import click
from .node import Node

class CDoublyLinkedList:
      def __init__(self):
            self.head = None
            self.tail = None
            self.count = 0

      #Function to create Circular Doubly Linked List
      def createCDLL(self, value):
              new_node = Node(value)
              new_node.next = None
              new_node.prev = None
              self.head = new_node
              self.tail = new_node
              self.count += 1
              print("The circular doubly linked list has been created.")

      #Function to add node in the beginning
      def atBeg(self, value):
            new_node =  Node(value)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
            self.head.prev = self.tail
            self.count += 1

      #Function to add node in the middle
      def inMid(self,prev_node, value):
             if prev_node is None:
                 print("Mentioned node doesn't exist")
                 return

             next_node = prev_node.next 
             new_node = Node(value)
             prev_node.next = new_node
             new_node.prev = prev_node
             new_node.next = next_node
             next_node.prev = new_node
             self.count += 1

      #Function to add node in the end
      def atEnd(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        last_node = self.head
        while(last_node.next != self.head):
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node
        self.tail = new_node
        self.tail.next = self.head
        self.head.prev = self.tail
        self.count += 1

      #searching
      def searchList(self, value):
        position = 0
        found = 0
        if self.head is None:
            print("The linked list does not exist")
        else:
            temp_node = self.head
            while temp_node:
                position = position + 1
                if temp_node.value == value:
                    print("The required value was found at position: " + str(position))
                    found = 1
                    break
                if temp_node == self.tail:
                    print("The required value does not exist in the list")
                    break
                temp_node = temp_node.next

      #delete
      #Function to delete node from the beginning
      def delBeg(self):
        if(self.head == None):
            return
        elif (self.head.next == self.tail.next):
            self.head = self.tail = None
            return
        elif (self.head is not None):
            next_node = self.head.next
            next_node.prev = None
            self.head = next_node
            self.tail.next = self.head
            self.head.prev = self.tail
            return
      #Function to delete a node from between the linked list
      def delMid(self, del_value):
       if(self.head == None):
                return
       temp_node = self.head
       found = False
       while (temp_node) :
             if(temp_node.value == del_value):
                  found = True
                  break
             temp_node = temp_node.next
       if (found == True):
             prev_node = temp_node.prev
             next_node = temp_node.next
             prev_node.next = next_node
             next_node.prev = prev_node
             return
       else:
             print("Element not found.") 

      #Function to delete node from the end
      def delEnd(self):
        if(self.head == None):
            return
        elif (self.head.next == self.tail.next):
            self.head = self.tail = None
            return
        else:
            temp_node = self.head
            while (temp_node.next is not self.tail):
                temp_node = temp_node.next
            self.tail = temp_node
            temp_node.next = None
            self.tail.next = self.head
            self.head.prev = self.tail
            return
      #delete all
      def delCDLL(self):
        if self.head is None:
            print("The circular doubly linked list does not exist.")
        else:
            self.tail.next = None
            temp_node = self.head
            while (temp_node):
                temp_node.prev = None
                temp_node = temp_node.next
            self.head = None
            self.tail.next = None
            self.tail = None
        print("The circular doubly linked list has been deleted.")    

      def printForwardList(self):
        if self.head == None:
            print("The linked list does not exist.")
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                if temp_node == self.tail:
                    break
                temp_node = temp_node.next       
      def printReverseList(self):
        if self.head == None:
            print("The linked list does not exist.")
        else:
            temp_node = self.tail
            while temp_node:
                print(temp_node.value)
                if temp_node == self.head:
                    break
                temp_node = temp_node.prev       
      def searchList(self, value):
        position = 0
        found = 0
        if self.head is None:
            print("The linked list does not exist")
        else:
            temp_node = self.head
            while temp_node:
                position = position + 1
                if temp_node.value == value:
                    print("The required value was found at position: " + str(position))
                    found = 1
                    break
                if temp_node == self.tail:
                    print("The required value does not exist in the list")
                    break
                temp_node = temp_node.next

      def __iter__(self):
            node = self.head
            while node:
                yield node
                node = node.next
                if node == self.tail.next:
                    break

@click.command()
def run():
      circulardoublyLL = CDoublyLinkedList()
      circulardoublyLL.createCDLL(5)
      circulardoublyLL.atBeg(0)
     
      print([node.value for node in circulardoublyLL])
      
