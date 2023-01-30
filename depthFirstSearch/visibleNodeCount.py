class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://stackoverflow.com/questions/51662467/using-a-global-variable-inside-a-function-nested-in-a-function-in-python


def visible_tree_node(root: Node) -> int:
    # child node can check value if parent node, can also check if parent is visible
    counter = 0

    def dfs(root, maxVal):
        if not root:
            return

        if root.val >= maxVal:
            maxVal = root.val
            nonlocal counter
            counter += 1

        dfs(root.left, maxVal)
        dfs(root.right, maxVal)

        return
    dfs(root, float('-inf'))
    return counter

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree


def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x':
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = visible_tree_node(root)
    print(res)
