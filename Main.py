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
        self.num1 = self.convert_ll_to_int(first_list)
        self.num2 = self.convert_ll_to_int(second_list)
        num3 = self.num1 + self.num2
        self.return_ll = LinkedList()
        self.convert_int_to_ll(
            num3, max(first_list.length, second_list.length))
        return self.return_ll

    def convert_ll_to_int(self, linked: Optional[LinkedList]):
        num = 0
        if linked.head != None:
            t = linked.head
            while t:
                num = num*10 + t.data
                t = t.next
        # print(num)
        return num

    def convert_int_to_ll(self, num, length):
        list1 = []
        while num != 0:
            list1.append(num % 10)
            num //= 10
        list1.reverse()
        list1 = list1[:length]
        for i in list1:
            self.return_ll.insert_at_end(i)


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
