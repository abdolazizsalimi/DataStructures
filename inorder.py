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
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Inorder traversal
# Left -> Root -> Right
    def inorder(self, root):
        resulte = []
        if root:
            resulte = self.inorder(root.left)
            resulte.append(root.data)
            resulte = resulte + self.inorder(root.right)
        return resulte 



# Root -> Left ->Right
    def Preorder(self, root):
        resulte = []
        if root:
            resulte.append(root.data)
            resulte = resulte + self.Preorder(root.left)
            resulte = resulte + self.Preorder(root.right)
        return resulte


# Left ->Right -> Root
    def Postorder(self, root):
        resulte = []
        if root:
            resulte = self.Postorder(root.left)
            resulte = resulte + self.Postorder(root.right)
            resulte.append(root.data)
        return resulte



root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)



print('inorder:' + str(root.inorder(root)))
print('Preorder:' + str(root.Preorder(root)))
print('Postorder:' + str(root.Postorder(root)))



a=  3 
print(a)
a= 'dijfih'
print(a)
a= []
print(a)

a= 'ali' + 7
print(a)