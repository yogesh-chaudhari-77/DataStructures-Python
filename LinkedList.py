class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    head = None

    def __init__(self, val):
        if self.head is None:
            self.head = ListNode(val)

    def insert(self, val):
        newListNode = ListNode(val)
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = newListNode
        return True

    def print(self):
        temp = self.head

        while temp:
            print(str(temp.val) + " ")
            temp = temp.next

    def remove(self, element):
        removed = False
        if self.head.val == element :
            self.head = self.head.next
            removed = True
            return True
        else :
            temp = self.head

            while temp :
                if temp.next.val == element:
                    temp.next = temp.next.next
                    return True

                temp = temp.next


myLinkedList = LinkedList(1)
myLinkedList.insert(5)
myLinkedList.insert(6)
myLinkedList.insert(7)
myLinkedList.insert(6)
myLinkedList.insert(6)
myLinkedList.insert(8)
myLinkedList.print()
print("-------")
myLinkedList.remove(6)
myLinkedList.print()