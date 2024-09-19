
class LinkedList:

    class Node:

        def __init__(self, value) -> None:
            self.value = value
            self.next = None

    def __init__(self) -> None:

        self.head = self.Node(-1)

        befor = self.head

        for i in range(100):
            new_node = self.Node(i)
            befor.next = new_node
            befor = new_node
        
        befor.next = self.head

a = LinkedList()
b = a.head

while 1:

    print(b.value)
    b = b.next
