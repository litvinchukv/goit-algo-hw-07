class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    # Завдання 1: Знаходження найбільшого значення
    def find_max(self):
        if not self.root:
            return None
        return self._find_max_recursive(self.root)

    def _find_max_recursive(self, node):
        if node.right is None:
            return node.value
        return self._find_max_recursive(node.right)

    # Завдання 2: Знаходження найменшого значення
    def find_min(self):
        if not self.root:
            return None
        return self._find_min_recursive(self.root)

    def _find_min_recursive(self, node):
        if node.left is None:
            return node.value
        return self._find_min_recursive(node.left)

    # Завдання 3: Знаходження суми всіх значень
    def sum_all(self):
        return self._sum_all_recursive(self.root)

    def _sum_all_recursive(self, node):
        if node is None:
            return 0
        return node.value + self._sum_all_recursive(node.left) + self._sum_all_recursive(node.right)

if __name__ == "__main__":
    # Приклад використання:
    bst = BinarySearchTree()
    values = [5, 3, 7, 1, 4, 6, 8]
    for value in values:
        bst.insert(value)

    print(f"Найбільше значення: {bst.find_max()}")
    print(f"Найменше значення: {bst.find_min()}")
    print(f"Сума всіх значень: {bst.sum_all()}")