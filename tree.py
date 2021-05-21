class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left_child = None
        self.parent = None
    
    def add_Neighbor(self, Neighbor):
        node = self
        while node.right:
            node = node.right

        node.right = Neighbor
        Neighbor.parent = self.parent
    
    def add_child(self, child):
        if self.left_child:
            self.left_child.add_Neighbor(child)
        else:
            self.left_child = child
            child.parent = self
    
    def get_depth(self):
        depth = 0
        node = self
        while node.parent:
            depth += 1
            node = node.parent
        return depth
    
    def number_of_nodes(self):
        nodes = 1
        child = self.left_child
        while child:
            nodes += child.number_of_nodes()
            child = child.right
        return nodes

    def __str__(self):
        ret = '--'*self.get_depth() + '(' + str(self.value) + ')'
        
        child = self.left_child
        while child:
            ret += '\n' + child.__str__()
            child = child.right
        
        return ret 


# left ->> root --> other
def in_order(node):
    if not node:
        return
    in_order(node.left_child)
    
    print(node.value, end = " ")
    if node.left_child:
        child =  node.left_child.right
        while child:
            in_order(child)
            child = child.right

# root --> left --> other
def pre_order(node):
    if not node:
        return
    print(node.value, end = " ")
    
    pre_order(node.left_child)
    
    if node.left_child:
        child =  node.left_child.right
        while child:
            pre_order(child)
            child = child.right

# left --> other --> root
def post_order(node):
    if not node:
        return
    
    post_order(node.left_child)
    
    if node.left_child:
        child =  node.left_child.right
        while child:
            post_order(child)
            child = child.right

    print(node.value, end = " ")

def main():
    G1 = TreeNode("1")

    G = TreeNode('4')

    G3 = TreeNode('5')
    G3.add_child(TreeNode('7'))
    G3.add_child(TreeNode('3'))
    G.add_child(G3)

    G4 = TreeNode('9')
    G4.add_child(TreeNode('5'))
    G4.add_child(TreeNode('8'))
    G.add_child(G4)

    G1.add_child(G)

    G5 = TreeNode('2')
    G5.add_child(TreeNode('10'))
    G5.add_child(TreeNode('11'))
    G5.add_child(TreeNode('16'))

    G1.add_child(G5)
    
    print('printing tree:')
    print(G1)
    
    print('\n\n===============pre-order===============')
    pre_order(G)
    print('\n\n===============in-order===============')
    in_order(G)
    print('\n\n===============post-order===============')
    post_order(G)
    
    print('\n\n\nNumber of Nodes for G5 node(self included):')
    print(G5.number_of_nodes())
    print('\nNumber of Nodes for G node(self included):')
    print(G.get_depth())
if __name__ == "__main__":
    main()