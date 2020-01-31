class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if value is found, return false to indicate no node inserted
        if self.value == value:
            return False
        # value smaller than node, look left
        elif value < self.value:
            # if node exists, continue recursively checking until something is found or inserted
            if self.left:
                return self.left.insert(value)
            # if no node exists, create new one and return true
            else:
                self.left = BinarySearchTree(value)
                return True
        else:
            # if node exists, continue recursively checking until something is found or inserted
            if self.right:
                return self.right.insert(value)
            # if no node exists, create new one and return true
            else:
                self.right = BinarySearchTree(value)
                return True

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if target is there, return true if so
        if self.value == target:
            return True
        # if target is less than node value and left node exists, check for value again
        elif target < self.value and self.left:
            return self.left.contains(target)
        # if target is less than node value and right node exists, check for value again
        elif target > self.value and self.right:
            return self.right.contains(target)
        # if target not found, return false
        else:
            return False
