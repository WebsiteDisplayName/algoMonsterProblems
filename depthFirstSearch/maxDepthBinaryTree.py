class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_max_depth(root: Node) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    def dfs(root, depth):
        if not root:
            return depth

        if root.left:
            left = dfs(root.left, depth+1)
        else:
            left = depth

        if root.right:
            right = dfs(root.right, depth+1)
        else:
            right = depth
        return max(left, right)

    return dfs(root, 0)

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
    res = tree_max_depth(root)
    print(res)
