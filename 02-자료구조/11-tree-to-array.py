# 2장 Part 2, 19~20쪽 - 이진 트리의 배열 표현

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def tree_to_array(root):
    if root is None:
        return []

    array = []
    queue = [(root, 0)]

    while queue:
        node, index = queue.pop(0)

        if index >= len(array):
            array.extend([None] * (index - len(array) + 1))

        array[index] = node.key

        if node.left:
            queue.append((node.left, 2 * index + 1))
        if node.right:
            queue.append((node.right, 2 * index + 2))

    return array


# 추가 테스트
binary_tree_root = TreeNode('A')
binary_tree_root.left = TreeNode('B')
binary_tree_root.right = TreeNode('C')
binary_tree_root.left.right = TreeNode('D')

array_representation = tree_to_array(binary_tree_root)
print(array_representation)