# A. BST - дерево поиска без балансировки
import sys

# дерево может выродиться в цепочку из 1000 вершин, рекурсии нужен запас
sys.setrecursionlimit(10000)


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class BST:
    def __init__(self):
        self.root = None

    # высоту храним в самой вершине, тогда height работает за O(1)
    def _h(self, node):
        if node is None:
            return 0
        return node.height

    def _update(self, node):
        node.height = max(self._h(node.left), self._h(node.right)) + 1

    def add(self, x):
        self.root = self._add(self.root, x)

    def _add(self, node, x):
        if node is None:
            return Node(x)
        if x < node.key:
            node.left = self._add(node.left, x)
        elif x > node.key:
            node.right = self._add(node.right, x)
        else:
            return node
        self._update(node)
        return node

    def delete(self, x):
        self.root = self._delete(self.root, x)

    def _delete(self, node, x):
        if node is None:
            return None
        if x < node.key:
            node.left = self._delete(node.left, x)
        elif x > node.key:
            node.right = self._delete(node.right, x)
        else:
            # лист или один ребенок
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # два ребенка: берем минимум из правого поддерева
            m = node.right
            while m.left is not None:
                m = m.left
            node.key = m.key
            node.right = self._delete(node.right, m.key)
        self._update(node)
        return node

    def exists(self, x):
        node = self.root
        while node is not None:
            if x == node.key:
                return True
            if x < node.key:
                node = node.left
            else:
                node = node.right
        return False

    def height(self):
        return self._h(self.root)

    def preorder(self):
        keys = []
        self._preorder(self.root, keys)
        return keys

    def _preorder(self, node, keys):
        if node is None:
            return
        keys.append(str(node.key))
        self._preorder(node.left, keys)
        self._preorder(node.right, keys)


def main():
    input = sys.stdin.readline
    tree = BST()
    ans = []
    q = int(input())
    for _ in range(q):
        cmd = input().split()
        if cmd[0] == 'add':
            tree.add(int(cmd[1]))
        elif cmd[0] == 'del':
            tree.delete(int(cmd[1]))
        elif cmd[0] == 'exists':
            if tree.exists(int(cmd[1])):
                ans.append('YES')
            else:
                ans.append('NO')
        elif cmd[0] == 'height':
            ans.append(str(tree.height()))
        elif cmd[0] == 'print':
            keys = tree.preorder()
            if keys:
                ans.append(' '.join(keys))
            else:
                ans.append('Empty')
    print('\n'.join(ans))


if __name__ == '__main__':
    main()
