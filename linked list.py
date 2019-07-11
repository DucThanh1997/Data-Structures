# 1 phần tử trong linked list có 2 thứ
# data
# next node

# data chứa dữ liệu còn next node để đánh dấu tìm phần tử tiếp theo

# có 3 kiểu linked list,
# linked list thường
# Doubly linked lists
# linked list vòng tròn


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def surf(self):
        node = self
        while node != None:
            print(node.data)
            node = node.next


if __name__ == "__main__":
    node1 = Node(12)
    node2 = Node(99)
    node3 = Node(37)
    node1.next = node2
    node2.next = node3
    node1.surf()
