# Pre-order traversal
def pre_order(node):
    res = []
    if node:
        res.append(node.data)
        res = res + pre_order(node.left)
        res = res + pre_order(node.right)
    return res

# In-order traversal
def in_order(node):
    res = []
    if node:
        res = in_order(node.left)
        res.append(node.data)
        res = res + in_order(node.right)
    return res

# Post-order traversal
def post_order(node):
    res = []
    if node:
        res = res + post_order(node.left)
        res = res + post_order(node.right)
        res.append(node.data)
    return res
  
