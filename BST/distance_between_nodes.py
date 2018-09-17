class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, element):
        if (self.root == None):
            # First element
            self.root = Node(element)
        else:
            # Second or later element
            prev = self.root
            root = self.root
            while root != None:
                left, right = 0, 0
                if element < root.data:
                    left = 1
                    prev = root
                    root = root.left
                else:
                    right = 1
                    prev = root
                    root = root.right
            if left:
                prev.left = Node(element)
            else:
                prev.right = Node(element)

    def preorder(self, root):
        if (root):
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

    def distance_between_nodes(self, root, no1, no2):
        print ("root is ", root)
        if root == None:
            return 0
        if root.data > no1 and root.data > no2:
            # go to left subtree
            return self.distance_between_nodes(root.left, no1, no2)
        if root.data < no1 and root.data < no2:
            return self.distance_between_nodes(root.right, no1, no2)

        if root.data >= no1 and root.data <= no2:
            # least common ancestor
            print ('reached ', root.data)
            return self.distance_from_root(root, no1) + self.distance_from_root(root, no2)

    def distance_from_root(self, root, no1):
        print("distance: ", root)
        if(root.data == no1):
            return 0
        elif (root.data > no1):
            return 1 + self.distance_from_root(root.left, no1)
        return 1 + self.distance_from_root(root.right, no1)

if __name__ == '__main__':
    bst = BST()
    bst.insert(5)
    bst.insert(6)
    bst.insert(3)
    bst.insert(1)
    bst.insert(2)
    bst.insert(4)
    bst.preorder(bst.root)
    print "distance is ", bst.distance_between_nodes(bst.root, 2, 6)
