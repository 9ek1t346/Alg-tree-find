# C. AVL 2. Вставка
import sys


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def _h(self, node):
        if node is None:
            return 0
        return node.height

    def _update(self, node):
        node.height = max(self._h(node.left), self._h(node.right)) + 1

    # bal(v) = h(R) - h(L)
    def _bal(self, node):
        return self._h(node.right) - self._h(node.left)

    def _rotate_left(self, a):
        b = a.right
        a.right = b.left
        b.left = a
        self._update(a)
        self._update(b)
        return b

    def _rotate_right(self, a):
        b = a.left
        a.left = b.right
        b.right = a
        self._update(a)
        self._update(b)
        return b

    # пересчитываем высоту, если |bal| = 2 - делаем малое или большое вращение
    # возвращаем новый корень поддерева
    def _balance(self, v):
        self._update(v)
        b = self._bal(v)
        if b == 2:
            if self._bal(v.right) < 0:
                v.right = self._rotate_right(v.right)
            return self._rotate_left(v)
        if b == -2:
            if self._bal(v.left) > 0:
                v.left = self._rotate_left(v.left)
            return self._rotate_right(v)
        return v

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
        # на обратном ходе проверяем вершины от родителя нового листа до корня
        return self._balance(node)

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

    def root_key(self):
        if self.root is None:
            return None
        return self.root.key

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
    tree = AVLTree()
    ans = []
    q = int(input())
    for _ in range(q):
        cmd = input().split()
        if cmd[0] == 'add':
            tree.add(int(cmd[1]))
        elif cmd[0] == 'exists':
            if tree.exists(int(cmd[1])):
                ans.append('YES')
            else:
                ans.append('NO')
        elif cmd[0] == 'root':
            key = tree.root_key()
            if key is None:
                ans.append('Empty')
            else:
                ans.append(str(key))
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
