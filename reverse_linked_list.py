import re

class Node :
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Reverse_LinkedList:
    def __init__(self, head= None):
        self.head = head


    def to_string(self):
        current = self.head
        values = ""
        while current:
            values += f"{ {current.value} } -> "
            list_values = re.sub(r"\'", ' ', values)
            current = current.next
        list_values += "NONE"
        return list_values

    
    def append(self, new_value):
            new_node = Node(new_value)
            if self.head is None:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node


    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            newNode = curr.next
            curr.next = prev
            prev = curr
            curr = newNode
        self.head = prev
        return self.head
    

reverse= Reverse_LinkedList()
reverse.append(1)
reverse.append(2)
reverse.append(3)
print(reverse.to_string())
reverse.reverse()
print(reverse.to_string())

       
