# B. AVL 1. Вращения
import sys

sys.setrecursionlimit(10000)


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, x):
        self.root = self._add(self.root, x)

    def _add(self, node, x):
        if node is None:
            return Node(x)
        if x < node.key:
            node.left = self._add(node.left, x)
        elif x > node.key:
            node.right = self._add(node.right, x)
        return node

    # поворот вокруг вершины с ключом x, side - left или right
    def rotate(self, x, side):
        self.root = self._rotate(self.root, x, side)

    # спускаемся до вершины с ключом x, поворачиваем ее и возвращаем новый
    # корень поддерева, чтобы родитель перецепил ссылку
    def _rotate(self, node, x, side):
        if node.key == x:
            if side == 'left':
                return self._rotate_left(node)
            return self._rotate_right(node)
        if x < node.key:
            node.left = self._rotate(node.left, x, side)
        else:
            node.right = self._rotate(node.right, x, side)
        return node

    def _rotate_left(self, a):
        b = a.right
        a.right = b.left
        b.left = a
        return b

    def _rotate_right(self, a):
        b = a.left
        a.left = b.right
        b.right = a
        return b

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
    data = sys.stdin.read().split()
    n = int(data[0])
    tree = Tree()
    for i in range(1, n + 1):
        tree.add(int(data[i]))

    m = int(data[n + 1])
    pos = n + 2
    ans = []
    for _ in range(m):
        side = data[pos]
        x = int(data[pos + 1])
        pos += 2
        tree.rotate(x, side)
        ans.append(' '.join(tree.preorder()))
    print('\n'.join(ans))


if __name__ == '__main__':
    main()
