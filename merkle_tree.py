import hashlib

class Node():
    def __init__(self, value):
        self.val = value
        self.right = None
        self.left = None

class merkle_trees():
    def __init__(self, transactions):
        self.transactions = transactions
        self.root = None
        self.nodes = []
        self.parentNodes = []
        self.correctTree = []
    
    def create_tree(self):
        for tran in self.transactions:
            currHash = hashlib.sha256(tran.encode('utf-8')).hexdigest()
            currNode = Node(currHash)
            print(currHash)
            self.nodes.append(currNode)
            if len(self.nodes) == 2:
                #print(self.nodes)
                # for node in self.nodes:
                #     print(node.val)
                leftHash = self.nodes[0].val
                rightHash = self.nodes[1].val
                parentHash = hashlib.sha256((leftHash+rightHash).encode('utf-8')).hexdigest()
                parentNode = Node(parentHash)
                parentNode.left = self.nodes[0]
                parentNode.right = self.nodes[1]
                self.nodes.pop(0)
                self.nodes.pop(0)
                self.parentNodes.append(parentNode)
                # print(self.parentNodes)
                # for pNone in self.parentNodes:
                #     print(pNone.val)
        while self.root == None:
            self.nodes = self.parentNodes[::]
            self.parentNodes = []
            i = 0
            while i < len(self.nodes):
                leftHash = self.nodes[i].val
                rightHash = self.nodes[i+1].val
                parentHash = hashlib.sha256((leftHash+rightHash).encode('utf-8')).hexdigest()
                parentNode = Node(parentHash)
                parentNode.left = self.nodes[i]
                parentNode.right = self.nodes[i+1]
                self.parentNodes.append(parentNode)
                print(self.parentNodes)
                for pNone in self.parentNodes:
                    print(pNone.val)
                i += 2
            if len(self.parentNodes) == 1:
                self.root = self.parentNodes[0]
            else:
                continue
    
    def treeTraversal(self, root):
        if root == None:
            return
        else:
            print(root.val)
            self.treeTraversal(root.left)
            self.treeTraversal(root.right)

    def treeBreadthFirstTraversal(self, root):
        if root == None:
            return
        nodeList = []
        nodeList.append(root)
        while(len(nodeList) > 0):
            currNode = nodeList.pop(0)
            print(currNode.val)
            self.correctTree.append(currNode.val)
            if currNode.left:
                nodeList.append(currNode.left)
            if currNode.right:
                nodeList.append(currNode.right)
            



if __name__ == '__main__':
    transactions = ['a','b','c','']
    mkTree = merkle_trees(transactions)
    mkTree.create_tree()
    print("Tree 1 is like:")
    #mkTree.treeTraversal(mkTree.root)
    mkTree.treeBreadthFirstTraversal(mkTree.root)
    transactions2 = ['a','b','c','d']
    mkTree2 = merkle_trees(transactions2)
    mkTree2.create_tree()
    print("Tree 2 is like:")
    #mkTree2.treeTraversal(mkTree2.root)
    #print("Asli traversal")
    mkTree2.treeBreadthFirstTraversal(mkTree2.root)
    print("Comparison")
    print(mkTree.correctTree)
    print("Next")
    print(mkTree2.correctTree)
 