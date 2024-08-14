
class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


    def insert(self, val):
        if not self.val:
           self.val = val
        elif val<self.val:
            if not self.left:
                self.left = BST(val)
            else:
                self.left.insert(val)
        else:
            if not self.right:
                self.right = BST(val)
            else:
                self.right.insert(val)
            
    def getMin(self):
        current =self
        while current.left is not None:
            current = current.left
        return current.val
    
    def getMax(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val
    
    def search(self, val):
        if self is not None:
            if self.val == val:
                return True
            elif val < self.val:
                if self.left is None:
                    return False
                else:
                    self.left.search(val)
            else:
                if self.right is None:
                    return False
                else:
                    self.right.search(val)

    def inOrder(self):
        if self.left:
            self.left.inOrder()
        print(self.val)
        if self.right:
            self.right.inOrder()

    def preOrder(self):
        print(self.val)
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()
        

    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self.val)

   
bst = BST(8)
bst.insert(10)
bst.insert(21)
bst.insert(1)
bst.insert(1)
bst.insert(1)
bst.insert(31)
bst.insert(41)

bst.inOrder()
print("**************************")
bst.preOrder()
print("**************************")
bst.postOrder()

