# 2장 Part 2, 24쪽 - Left Child / Right Sibling
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None   # 첫 번째 자식
        self.right = None  # 다음 형제


A = TreeNode('A')
B = TreeNode('B')
C = TreeNode('C')
D = TreeNode('D')
E = TreeNode('E')
F = TreeNode('F')
G = TreeNode('G')
H = TreeNode('H')
I = TreeNode('I')
J = TreeNode('J')
K = TreeNode('K')

# A의 자식: B, G, I
A.left = B
B.right = G
G.right = I

# B의 자식: C, D
B.left = C
C.right = D

# D의 자식: E, F
D.left = E
E.right = F

# G의 자식: H / I의 자식: J / J의 자식: K
G.left = H
I.left = J
J.left = K


# 추가 테스트 
def print_children(node):
    child = node.left
    while child is not None:
        print(child.data, end=" ")
        child = child.right
    print()


print("A의 자식:", end=" ")
print_children(A)

print("B의 자식:", end=" ")
print_children(B)

print("D의 자식:", end=" ")
print_children(D)