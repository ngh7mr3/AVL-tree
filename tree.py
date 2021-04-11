class TreeNode:
    __slots__ = '__data', '__height', 'parent', 'left', 'right'

    def __init__(self, data):
        self.__data = data
        self.__height = 0
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
        return  f"Node({self.data}) balance={self.balance} L->{left} R->{right}"


class BinaryTree:
    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    def __ascending_iter(self, node):
        if node:
            yield from self.__ascending_iter(node.left)
            yield node
            yield from self.__ascending_iter(node.right)

    def __descending_iter(self, node):
        if node:
            yield from self.__descending_iter(node.right)
            yield node
            yield from self.__descending_iter(node.left)

    def __key_iter(self, node, key):
        if node:
            yield node
            if key < node.data:
                yield from self.__key_iter(node.left, key)
            else:
                yield from self.__key_iter(node.right, key)

    def __iter__(self):
        return self.__ascending_iter(self.__root)

    def __getitem__(self, user_slice):
        if user_slice == slice(None, None, -1):
            # Only handling case where tree is called with [::-1]
            return self.__descending_iter(self.__root)
        else:
            raise ValueError

    def __rotate_left(self, node):
        """
        Counter-clockwise rotation
        """
        assert node.balance < 0 and node.right

        node_a, node_b = node, node.right
        node_a.right, node_b.left  = node_b.left, node_a

        node_a.update_height()
        node_b.update_height()
        return node_b

    def __rotate_right(self, node):
        """
        Clockwise rotation
        """
        assert node.balance > 0 and node.left

        node_a, node_b = node, node.left
        node_a.left, node_b.right  = node_b.right, node_a

        node_a.update_height()
        node_b.update_height()
        return node_b

    def __balance_subtree(self, tree_root):
        tree_root.update_height()

        if tree_root.balance == 2:
            if tree_root.left.balance == -1:
                tree_root.left = self.__rotate_left(tree_root.left)
            return self.__rotate_right(tree_root)
        elif tree_root.balance == -2:
            if tree_root.right.balance == 1:
                tree_root.right = self.__rotate_right(tree_root.right)
            return self.__rotate_left(tree_root)

        return tree_root

    def __add(self, node, key):
        if node:
            if key < node.data:
                node.left = self.__add(node.left, key)
            else:
                node.right = self.__add(node.right, key)
            return self.__balance_subtree(node)
        else:
            return TreeNode(key)

    def add(self, key):
        if not self.__root:
            self.__root = TreeNode(key)
            return

        self.__root = self.__add(self.__root, key)

    def find(self, key):
        key_iter = self.__key_iter(self.root, key)
        for node in key_iter:
            if node.data == key:
                return node

        raise KeyError(f"Could not find {key} in a tree")

