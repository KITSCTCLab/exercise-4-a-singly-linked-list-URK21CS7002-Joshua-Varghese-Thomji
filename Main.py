from typing import Optional


class Node:
    """
    Provide necessary documentation
    """

    def __init__(self, data=None, next=None):
        """
        Provide necessary documentation
        """
        self.data = data
        self.next = next


class LinkedList:
    """
    Provide necessary documentation
    """

    def __init__(self):
        """
        Initialize the head
        """
        self.head = None
        self.length = 0

    def insert_at_end(self, data):
        n = Node(data)
        if self.head != None:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = n
        else:
            self.head = n
        self.length += 1

    def status(self):
        """
        It prints all the elements of list.
        """
        status_list = []
        if self.head != None:
            t = self.head
            while t:
                status_list.append(t.data)
                t = t.next
            print(status_list)


class Solution:
    """
    Provide necessary documentation
    """

    def addTwoNumbers(self, first_list: Optional[LinkedList], second_list: Optional[LinkedList]) -> Optional[LinkedList]:
        self.first_list = first_list
        self.second_list = second_list
        self.equalize_ll()

        t1 = first_list.head
        t2 = second_list.head
        return_ll = LinkedList()
        carry = 0
        for i in range(first_list.length):
           sum = t1.data + t2.data + carry
           data = sum%10
           carry = sum//10
           return_ll.insert_at_end(data)
           t1 = t1.next
           t2 = t2.next
        if carry:
            return_ll.insert_at_end(carry)
        
        return return_ll

    def equalize_ll(self):
        while(self.first_list.length > self.second_list.length):
            self.second_list.insert_at_end(0)
        while(self.second_list.length > self.first_list.length):
            self.first_list.insert_at_end(0)


# Do not edit the following code
# Create an instance for LinkedList
first_list = LinkedList()
# Create an another instance for LinkedList
second_list = LinkedList()
# Read data for first list
data_for_first_list = list(map(int, input().strip().split(" ")))
# Add data at the end of first_list
for data in data_for_first_list:
    first_list.insert_at_end(data)
# Read data for second list
data_for_second_list = list(map(int, input().strip().split(" ")))
# Add data at the end of second_list
for data in data_for_second_list:
    second_list.insert_at_end(data)
# Create an instance for Solution
solution = Solution()
# Pass first_list and second_list to addTwoNumbers, which returns a new linked list
new_list = solution.addTwoNumbers(first_list, second_list)
# Display the status of new_list
new_list.status()
