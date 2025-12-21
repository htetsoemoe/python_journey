"""

Tree traversals ဆိုတာကတော့ tree တစ်ခုမှာ node တစ်ခု ခြင်းဆီ ကို သွားသည့် process လို့ ဆိုရပါမယ်။
Tree Traversals ၂ မျိုး ရှိပါတယ်။

Depth-first search (DFS), Breadth-first search (BFS) ဆိုပြီး ရှိပါတယ်။


Depth-first search (DFS)
DFS ကို အသုံးပြုပြီး data တွေကို ပြန်ပြီး ထုတ်ပြဖို့ အတွက် ထုတ်ပြနည်း ၃ ခု ရှိပါတယ်။

in order
pre order
post order
ဆိုပြီး ရှိပါတယ်။


Depth-first Search (DFS)

                A
            B       C
        D       E
    F       G

---- In Order ----
F
D
G
B
E
A
C
---- Pre Order ----
A
B
D
F
G
E
C
---- Post Order ----
F
G
D
E
B
C
A


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
    
    
    def inorder(self):
        if self != None:
            if self.get_left_child() != None:
                self.get_left_child().inorder()

            print(self.get_root_val())

            if self.get_right_child() != None:
                self.get_right_child().inorder()
            
            
    def postorder(self):
        if self != None:
            if self.get_left_child() != None:
                self.get_left_child().postorder()

            if self.get_right_child() != None:
                self.get_right_child().postorder()

            print(self.get_root_val())

    def preorder(self):
        if self != None:
            print(self.get_root_val())

            if self.get_left_child() != None:
                self.get_left_child().preorder()

            if self.get_right_child() != None:
                self.get_right_child().preorder()

root = BinaryTree("A")

root.insert_left("B")
root.insert_right("C")

b = root.get_left_child()

b.insert_left("D")
b.insert_right("E")

d = b.get_left_child()

d.insert_left("F")
d.insert_right("G")

print("---- In Order ----")
root.inorder()
print("---- Pre Order ----")
root.preorder()
print("---- Post Order ----")
root.postorder()