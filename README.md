# AVL-tree implementation
Basic AVL-tree implementation class with `add`, `find` and `iterate` methods (`delete` and `merge` haven't been implemented yet)

## Usage
- Initialize tree
```python3
from tree import BinaryTree
bin_tree = BinaryTree()
```
- Add some values
```python3
values_to_add = [1, 2, 3]
for value in values_to_add:
    bin_tree.add(value)
```
- Find value in a tree
```python3
tree_node = bin_tree.find(2) -> TreeNode
tree_node.data == 2 -> True
```
- Iterate through tree
```python3
# Ascending order: TreeNode(1), TreeNode(2), ...
for node in bin_tree:
    print(node)

# Descending order: TreeNode(3), TreeNode(2), ...
for node in bin_tree[::-1]:
    print(node)
```

## Tests
Run `python3 -m unittest tree_test.py` to check whether the tree class is working properly. Note that tests require `numpy` installed.

## Performance
Here's the time table for tree creation and node searching

| Methods \ Num. of elements | 10 | 10**2 | 10**3 | 10**4| 10**5 |
| :---: | --- | --- | ---| --- | --- |
| `add` | 63.4 µs ± 2.25 µs | 1.23 ms ± 5.06 µs | 18.1 ms ± 47.9 µs | 240 ms ± 911 µs | 3 s ± 16.3 ms |
| `find` | 4.71 µs ± 16 ns | 6.98 µs ± 53.7 ns | 9.65 µs ± 58.4 ns | 13 µs ± 85.5 ns | 16.9 µs ± 366 ns |

All performance measured with `ipython` and `%%timeit`

`add` method perfomance test based on n*log(n) tree creation time:
```python3
array_size = N
arr = np.arange(0, N)

%%timeit
bin_tree = BinaryTree()
for num in arr:
    bin_tree.add(num)
```

`find` method performance test based on random node searching:
```python3
def test_find(tree, size):
    rnd = np.random.randint(0, size)
    tree.find(rnd)

for i in range(1, 6):
    tree = build_tree(10**i) # Returns tree with nodes [0, ..., 10**i - 1]
    %timeit test_find(tree, 10**i)
```

