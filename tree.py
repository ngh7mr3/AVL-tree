class TreeNode:
    __slots__ = '__data', '__height', 'parent', 'left', 'right'

    def __init__(self, data):
        self.__data = data
        self.__height = 0
        self.parent = None
        self.left = None
        self.right = None

    @property
    def data(self):
        return self.__data

    @property
    def height(self):
        return self.__height

    @property
    def lst_height(self):
        return self.left.height + 1 if self.left else 0

    @property
    def rst_height(self):
        return self.right.height + 1 if self.right else 0

    @property
    def balance(self):
        return self.lst_height - self.rst_height

    def update_height(self):
        self.__height = max(self.lst_height, self.rst_height)

    def __lt__(self, node):
        return self.data < node.data

    def __gt__(self, node):
        return self.data > node.data

    def __repr__(self):
        left = self.left.data if self.left else None
        right = self.right.data if self.right else None
        return f"Node ({hex(id(self))}, {self.data}) balance={self.balance} left->{left} right->{right}"


class BinaryTree:
    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    def __rotate_left(self, node):
        """
        Counter-clockwise rotation
        """
        assert node.balance < 0 and node.right, f"b={node.balance}, n={node.right}"

        node_a, node_b = node, node.right
        node_a.parent, node_b.parent = node_b, node_a.parent
        node_a.right, node_b.left  = node_b.left, node_a

        if node_a.right:
            node_a.right.parent = node_a

        if node_b.parent != None:
            if node_b < node_b.parent:
                node_b.parent.left = node_b
            else:
                node_b.parent.right = node_b
        else:
            self.__root = node_b

        node_a.update_height()
        node_b.update_height()

    def __rotate_right(self, node):
        """
        Clockwise rotation
        """
        assert node.balance > 0 and node.left, f"b={node.balance}, n={node.left}"

        node_a, node_b = node, node.left
        node_a.parent, node_b.parent = node_b, node_a.parent
        node_a.left, node_b.right  = node_b.right, node_a

        if node_a.left:
            node_a.left.parent = node_a

        if node_b.parent != None:
            if node_b < node_b.parent:
                node_b.parent.left = node_b
            else:
                node_b.parent.right = node_b
        else:
            self.__root = node_b

        node_a.update_height()
        node_b.update_height()

    def __balance_subtree(self, tree_root):
        tree_root.update_height()
        if tree_root.balance == 2:
            if tree_root.left.balance == -1:
                self.__rotate_left(tree_root.left)
            self.__rotate_right(tree_root)
        elif tree_root.balance == -2:
            if tree_root.right.balance == 1:
                self.__rotate_right(tree_root.right)
            self.__rotate_left(tree_root)

    def add(self, key):
        new_node = TreeNode(key)
        if not self.__root:
            self.__root = new_node
            return

        # Find the space for a leaf
        current_node = self.__root
        while current_node:
            new_node.parent = current_node
            if current_node > new_node:
                current_node = current_node.left
            else:
                current_node = current_node.right

        # Set the leaf under its parent
        if new_node < new_node.parent:
            new_node.parent.left = new_node
        else:
            new_node.parent.right = new_node

        # Fix all the heights and balance subtrees
        current_node = new_node.parent
        while current_node:
            self.__balance_subtree(current_node)
            current_node = current_node.parent

    def find(self, key):
        current_node = self.__root

        while current_node != None and current_node.data != key:
            if key < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right

        if current_node == None:
            raise KeyError(f"Could not find {key} in a tree")

        return current_node

