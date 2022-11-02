class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class solution:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def inserEnd(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def print(self):
        curr = self.head.next
        while curr:
            print(curr.val, "->", end="")
            curr = curr.next
        print()

    def reverse(self):
        prev, curr = None, self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


solution = solution()
solution.inserEnd(5)
solution.inserEnd(4)
solution.inserEnd(3)
solution.inserEnd(2)
solution.inserEnd(1)
solution.reverse()
