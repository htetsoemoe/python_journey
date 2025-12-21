"""

Tree traversals ဆိုတာကတော့ tree တစ်ခုမှာ node တစ်ခု ခြင်းဆီ ကို သွားသည့် process လို့ ဆိုရပါမယ်။
Tree Traversals ၂ မျိုး ရှိပါတယ်။

Depth-first search (DFS), Breadth-first search (BFS) ဆိုပြီး ရှိပါတယ်။


Using Breadth-first search (BFS)

                A
            B       C
        D       E
    F       G

A
B,C
D,E
F,G

"""

class BinaryTree:
    
    def __repr__(self):
        return "Binary Tree, Key is " + self.key
        
    def __init__(self,root):
        self.key = root
        self.left_child = None
        self.right_child = None
    
    def insert_left(self,new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t
            
    def insert_right(self,new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child
        
    def set_root_val(self,obj):
        self.key = obj
        
    def get_root_val(self):
        return self.key
    
    def bfs(self):
        thislevel = [self]
        while thislevel:
            nextlevel = []
            level = []
            for n in thislevel:
                level.append(n.get_root_val())
                if n.get_left_child() != None:
                    nextlevel.append(n.get_left_child())
                if n.get_right_child() != None:
                    nextlevel.append(n.get_right_child())
            print(",".join(level))
            thislevel = nextlevel


root = BinaryTree("A")

root.insert_left("B")
root.insert_right("C")

b = root.get_left_child()

b.insert_left("D")
b.insert_right("E")

d = b.get_left_child()

d.insert_left("F")
d.insert_right("G")

root.bfs()