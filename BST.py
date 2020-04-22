""""
    Program for creation of Binary Tree
    It can also dynamically add node
    It can print the BST in preorder fashion
"""


class TreeNode:
    leftChild = None
    rightChild = None
    val = None

    def __init__(self, val):
        self.leftChild = None
        self.rightChild = None
        self.val = val


def findNumberOfChilds(node: TreeNode):
    childCount = 0
    if node.leftChild is not None:
        childCount += 1
    if node.rightChild is not None:
        childCount += 1

    return childCount


class BST:
    rootNode = None

    def __init__(self):
        print("BST initialised")

    def createBST(self, BSTNodes: list):

        for element in BSTNodes:

            if self.rootNode is None:
                self.rootNode = TreeNode(element)
            else:
                self.appendTreeNode(self.rootNode, element)

    def appendTreeNode(self, node, element):
        if node.val > element:
            if node.leftChild is None:
                node.leftChild = TreeNode(element)
            else:
                self.appendTreeNode(node.leftChild, element)
        elif node.val < element:
            if node.rightChild is None:
                node.rightChild = TreeNode(element)
            else:
                self.appendTreeNode(node.rightChild, element)

    def preorderTraversal(self, node):
        if node is not None:
            print(node.val)
            self.preorderTraversal(node.leftChild)
            self.preorderTraversal(node.rightChild)

    def getSortedList(self):
        sortedList = []

        def fn(treeNode):
            if treeNode is not None:
                fn(treeNode.leftChild)
                sortedList.append(treeNode.val)
                fn(treeNode.rightChild)

        fn(self.rootNode)
        return sortedList;

    def deleteNode(self, node: TreeNode, element):
        if node.val == element:
            if node != self.rootNode:
                childNodesCount = findNumberOfChilds(node)

                if node.leftChild is None and node.rightChild is None:
                    node = None  # Node has been deleted. this is leaf node condition
                elif childNodesCount == 1 and node.leftChild is not None:
                    print("Don't know what to do")
                elif childNodesCount == 1 and node.rightChild is not None:
                    node = node.rightChild
            else:
                sortedList = self.getSortedList()
                indexOfElementToBeDeleted = sortedList.index(element)
                inorderSuccessor = sortedList[indexOfElementToBeDeleted + 1]               # Get the inorder successor

                # Find the inorder successor


myTree = BST()
myTree.createBST([43, 10, 79, 90, 12, 54, 11, 9, 50])
print("Traversal before Inserting");
myTree.preorderTraversal(myTree.rootNode)

myTree.appendTreeNode(myTree.rootNode, 41)
myTree.appendTreeNode(myTree.rootNode, 95)

print("Traversal After Inserting");

myTree.preorderTraversal(myTree.rootNode)

# print(myTree.rootNode.val)
# print(myTree.rootNode.leftChild.val)
# print(myTree.rootNode.rightChild.val)

mySortedList = myTree.getSortedList()
print(mySortedList)

print(17//2)
