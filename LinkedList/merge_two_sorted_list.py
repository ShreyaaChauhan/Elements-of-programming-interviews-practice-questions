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

    def print(self):
        curr = self.head.next
        while curr:
            print(curr.val, "->", end=" ")
            curr = curr.next
        print("\n")


class mergeTwoList:
    def __init__(self, list1, list2):
        self.head_1 = list1
        self.head_2 = list2

    def mergeTwoList(self):
        dummy = ListNode()
        tail = dummy
        curr1 = self.head_1
        curr2 = self.head_2
        while curr1 or curr2:
            curr1 = curr1.next
            curr2 = curr2.next
            if curr1 <= curr2:
                dummy.next = curr1

    def print(self):
        curr = self.head_2.next
        while curr:
            print(curr.val, "->", end=" ")
            curr = curr.next
        print("\n")


print("===================List_1===================")
list_1 = LinkedList()
list_1.inserEnd(1)
list_1.inserEnd(2)
list_1.inserEnd(4)
list_1.print()
print(list_1.head.next.val)
print("===================List_2===================")
list_2 = LinkedList()
list_2.inserEnd(1)
list_2.inserEnd(3)
list_2.inserEnd(4)
list_2.print()

mergeTwoList = mergeTwoList(list_1.head, list_2.head)
mergeTwoList.print()
mergeTwoList.mergeTwoList()
