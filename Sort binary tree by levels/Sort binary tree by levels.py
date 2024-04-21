def tree_by_levels(node):
    if not node:
        return []
    queue = [node]
    visited = []
    while queue:
        current = queue.pop(0)
        visited.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return visited
