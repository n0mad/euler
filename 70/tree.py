class Node:
    def __init__(self, lchild = None, rchild = None, value = -1, data = None):
        self.lchild = lchild
        self.rchild = rchild
        self.value = value
        self.data = data
 
class Bst:
    """Implements Binary Search Tree"""
 
    def __init__(self):
        self.l = []  #nodes
        self.root = None
 
    def add(self, key, dt):
        """Add a node in tree"""
        if self.root == None:
            self.root = Node(value = key, data = dt)
            self.l.append(self.root)
            return 0
        else:
            self.p = self.root
            while True:
                if self.p.value > key:
                    if self.p.lchild == None:
                        self.p.lchild = Node(value = key, data = dt)
                        return 0 #success
                    else:
                        self.p = self.p.lchild
                elif self.p.value == key:
                    return -1 # value already in tree
                else:
                    if self.p.rchild == None:
                        self.p.rchild = Node(value = key, data = dt)
                        return 0 # success
                    else:
                        self.p = self.p.rchild
        return -2 #should never happen
 
    def search(self, key):
        """Searches Tree for a key and returns data; if not found returns None"""
        self.p = self.root
        if self.p == None:
            return None
 
        while True:
#            print self.p.value, self.p.data
            if self.p.value > key:
                if self.p.lchild == None:
                    return None #Not Found
                else:
                    self.p = self.p.lchild
            elif self.p.value == key:
                return self.p.data
            else:
                if self.p.rchild == None:
                    return None #Not Found
                else:
                    self.p = self.p.rchild
        return None #Should never happen
 
    def deleteNode(self, key):
        """Deletes node with value == key"""
        if self.root.value == key:
            if self.root.rchild == None:
                if self.root.lchild == None:
                    self.root = None
                else: self.root = self.root.lchild
            else:
                self.root.rchild.lchild = self.root.lchild
                self.root = self.root.rchild
            return 1
        self.p = self.root
        while True:
            if self.p.value > key:
                if self.p.lchild == None:
                    return 0 #Not found anything to delete
                elif self.p.lchild.val == key:
                    self.p.lchild = self.proceed(self.p, self.p.lchild)
                    return 1
                else:
                    self.p = self.p.lchild
            # There's no way self.p.value to be equal to key!
            if self.p.value < key:
                if self.p.rchild == None:
                    return 0 #Not found anything to delete
                elif self.p.rchild.value == key:
                    self.p.rchild = self.proceed(self.p, self.p.rchild)
                    return 1
                else:
                    self.p = self.p.rchild
        return 0
 
    def proceed(self, parent, delValue):
        if delValue.lchild == None and delValue.rchild == None:
            return None
        elif delValue.rchild == None:
            return delValue.lchild
        else:
            return delValue.rchild
 
    def sort(self):
        self.__traverse__(self.root, mode = 1)
 
    def __traverse__(self, v, mode = 0):
        """Traverse in: preorder = 0, inorder = 1, postorder = 2"""
        if v == None:
            return
        if mode == 0:
            print (v.value, v.data)
            self.__traverse__(v.lchild)
            self.__traverse__(v.rchild)
        elif mode == 1:
            self.__traverse__(v.lchild, 1)
            print (v.value, v.data)
            self.__traverse__(v.rchild, 1)
        else:
            self.__traverse__(v.lchild, 2)
            self.__traverse__(v.rchild, 2)
            print (v.value, v.data)
 
def main():
    tree = Bst()
    tree.add(4, "test1")
    tree.add(10, "test2")
    tree.add(23, "test3")
    tree.add(1, "test4")
    tree.add(3, "test5")
    tree.add(2, "test6")
    #tree.sort()
    print tree.search(3)
    print tree.deleteNode(10)
    print tree.deleteNode(23)
    print tree.deleteNode(4)
    print tree.search(3)
    tree.sort()
if __name__ == "__main__": main()
