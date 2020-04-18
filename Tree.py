# Construct a complete binary tree from given array in level order fashion


class TreeNode:
    val = None
    left = None
    right = None

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    rootNode = None

    def __init__(self, val):
        self.rootNode = TreeNode(val)

    def constructLevelWise(self, list):

        for i in range(len(list)):
            element = list[i]
            # if element is None:
            #     print("Inside None")
            #     continue
            self.insertTreeNode(element)

    def insertTreeNode(self, val):

        if self.rootNode is None:
            self.rootNode.val = val
        else:
            tempTreeNode = self.rootNode
            while tempTreeNode is not None:

                if tempTreeNode.left is None:
                    if tempTreeNode.right is not None :
                        tempTreeNode = tempTreeNode.right
                        continue
                    if val is None :
                        tempTreeNode.left = None
                        return
                    tempTreeNode.left = TreeNode(val)
                    return
                elif tempTreeNode.right is None:
                    if val is None :
                        tempTreeNode.right = None
                    tempTreeNode.right = TreeNode(val)
                    return

                tempTreeNode = tempTreeNode.left

    def preOrder(self, root):
        tempTreeNode = root
        if tempTreeNode is not None:
            print(tempTreeNode.val)
            self.preOrder(tempTreeNode.left)
            self.preOrder(tempTreeNode.right)


    def postOrder(self, root):
        tempTreeNode = root
        if tempTreeNode is not None:
            self.postOrder(tempTreeNode.left)
            self.postOrder(tempTreeNode.right)
            print(tempTreeNode.val)


myTree = Tree(1)
myTree.insertTreeNode(2)
myTree.insertTreeNode(3)
myTree.insertTreeNode(4)
myTree.insertTreeNode(5)
# print(myTree.rootNode.val)
# print(myTree.rootNode.left.val)
# print(myTree.rootNode.right.val)
# print(myTree.rootNode.left.left.val)
# print(myTree.rootNode.left.right.val)

print("----------------")

myTree.preOrder(myTree.rootNode)

print("----------------")
myTree.postOrder(myTree.rootNode)

leecodeTree = Tree(1)
leecodeTree.insertTreeNode(None)
leecodeTree.insertTreeNode(2)
leecodeTree.insertTreeNode(3)
print("----------------")
leecodeTree.preOrder(leecodeTree.rootNode)
