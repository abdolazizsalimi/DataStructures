class Node:
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data 


    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data



    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()




def Death (root , node):
    if node == None :
        return float('-inf')
    if int(root) == int(node.data):
        return 0 
    return max(Death(root, node.left) , Death(root ,node.right)) + 1



root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

print(Death(14 ,root))
# root.PrintTree()