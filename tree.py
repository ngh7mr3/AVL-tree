class Node:
    __slots__ = '__data', 'parent', 'left', 'right'

    def __init__(self, data):
        self.__data = data
        self.parent = None
        self.left = None
        self.right = None

    @property
    def data(self):
        return self.__data

    def __lt__(self, node):
        return self.data < node.data

    def __gt__(self, node):
        return self.data > node.data

    def __repr__(self):
        left_ch = None if self.left == None else (hex(id(self.left)), self.left.data)
        right_ch = None if self.right == None else (hex(id(self.right)), self.right.data)
        return f"Node {hex(id(self)), self.data}: left -> {left_ch}, right -> {right_ch}"

class BinaryTree:
    def __init__(self, nodes=[]):
        self.__root = None
        for node in nodes:
            self.add(node)

    @property
    def root(self):
        return self.__root

    def add(self, key):
        new_node = Node(key)
        if not self.__root:
            self.__root = new_node
            return

        current_node = self.__root
        while current_node != None:
            new_node.parent = current_node
            if current_node > new_node:
                current_node = current_node.left
            else:
                current_node = current_node.right

        if new_node.parent > new_node:
            new_node.parent.left = new_node
        else:
            new_node.parent.right = new_node

    def find(self, key):
        pass

