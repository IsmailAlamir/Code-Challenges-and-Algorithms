class Node :
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class Tree:
    def __init__(self):
        self.root=None
        self.tree=''


    def __str__(self,node):
        self.print_Tree(node)
        return self.tree

    def print_Tree(self,node):
    # print the node of the tree
        if node is None:
            return None
        if node is not None:
            self.tree+=f'{node.value} ,'
        if node.left is not None:
            self.print_Tree(node.left)
        if node.right is not None:  
            self.print_Tree(node.right)


    def Construct_Tree(self,preorder,inorder):
        #Construct Binary Tree from Preorder and Inorder Traversal

        if not preorder or not inorder or not len(preorder)==len(inorder):
            return None
        
        root= Node(preorder[0])
        mid=inorder.index(preorder[0])
        root.left=self.Construct_Tree(preorder[1:mid+1],inorder[:mid])
        root.right=self.Construct_Tree(preorder[mid+1:],inorder[mid+1:])

        return root
