"""
Write a Python program to develop a custom iterator that iterates over a tree data structure.
"""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)


class TreeIterator:
    def __init__(self, root):
        self.stack = [root]   

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration
        
        node = self.stack.pop()
        
        
        self.stack.extend(reversed(node.children))
        
        return node.value


root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
child3 = TreeNode(4)

root.add_child(child1)
root.add_child(child2)
child1.add_child(child3)

for value in TreeIterator(root):
    print(value)