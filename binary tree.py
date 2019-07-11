# 1 phần tử trong cây được gọi là node
# 1 node chứa 3 thứ: data, left node, right node
# nếu bé hơn thì là left node nếu lớn hơn là right node

# cài đặt:

class Node:
    def __init__(self, data):
        self.data = data
        self.right_node = None
        self.left_node = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left_node is None:
                    self.left_node = Node(data)
                else:
                    self.left_node.insert(data)
            elif data > self.data:
                if self.right_node is None:
                    self.right_node = Node(data)
                else:
                    self.right_node.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left_node:
            self.left_node.print_tree()
        if self.right_node:
            self.right_node.print_tree()
        print(self.data)

    def height(self):
        if self.data is None:
            return 0
        elif self.left_node is None and self.right_node is None:
            return 0
        elif self.left_node is None:
            if self.right_node is not None:
                return 1 + self.right_node.height()
        elif self.right_node is None:
            if self.left_node is not None:
                return 1 + self.left_node.height()
        else:
            return 1 + max(self.left_node.height(), self.right_node.height())

    def look(self, number):
        if self.data == number:
            print("Tồn tại số ", number)
        else:
            if self.left_node is not None:
                self.left_node.look(number)
            elif self.right_node is not None:
                self.right_node.look(number)


if __name__ == "__main__":
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    print("kết quả: ", root.height())
    root.print_tree()
