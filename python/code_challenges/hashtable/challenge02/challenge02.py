# Write here the code challenge solution


class Tree :
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None


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



def first_repeated_word(string):
    # first_repeated_word is a function that will take a string as a parameter and
    # return the first repeated word in that string.
  word_count = {}
  
  words = string.split()
  
  for word in words:
    if word in word_count:
      return word
    
    word_count[word] = 1
  
  return "No Repetition"
