#
# Created on Wed Nov 02 2022 8:44:16 AM
#
# Shreya Chauhan
#


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def inserEnd(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index):
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next

    def print(self):
        curr = self.head.next
        while curr:
            print(curr.val, "->", end="")
            curr = curr.next
        print()


list = LinkedList()
list.inserEnd(10)
list.inserEnd(20)
list.inserEnd(30)
list.inserEnd(10)
list.remove(1)
list.print()
