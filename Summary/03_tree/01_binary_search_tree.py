'''
    이진 트리 노드 삽입, 탐색, 순회 등의 기능 구현
'''

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if key < root.val:
                root.left = self._insert(root.left, key)
            else:
                root.right = self._insert(root.right, key)
        return root

    def preorder(self, node):
        if node:
            print(node.val, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val, end=' ')
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val, end=' ')

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search(root.left, key)
        return self._search(root.right, key)

# 이진 탐색 트리 사용 예시
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("전위 순회 결과:")
bst.preorder(bst.root)
print("\n")

print("중위 순회 결과:")
bst.inorder(bst.root)
print("\n")

print("후위 순회 결과:")
bst.postorder(bst.root)
print("\n")

# 탐색 예시
search_key = 40
result = bst.search(search_key)
if result:
    print(f"{search_key}를(을) 찾았습니다.")
else:
    print(f"{search_key}는(은) 트리에 없습니다.")
