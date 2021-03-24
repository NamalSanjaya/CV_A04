

class Queue:
    def __init__(self):
        self.deq = []
    def enqueue(self,value):
        self.deq.append(value)
    def dequeue(self):
        if not self.is_empty():
            return self.deq.pop(0)
    def is_empty(self):
        return len(self.deq) == 0
    def __len__(self):
        return len(self.deq)
    def get_queue(self,index):
        if not self.is_empty():
            return self.deq[index]


class Node:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None

class Binary_tree:
    def __init__(self):
        self.root = None

    def IsEmpty(self):
        if self.root is None:
            return True
        else:
            return False

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._Insert(data,self.root)

    def _Insert(self,data,cur_root):
        if  data < cur_root.data:
            if cur_root.left is None:
                cur_root.left = Node(data)
            else:
                self._Insert(data,cur_root.left)
        elif data > cur_root.data:
            if cur_root.right is None:
                if cur_root.right is None:
                    cur_root.right = Node(data)
            else:
                self._Insert(data,cur_root.right)

        else:
            print("Duplications are not allowed!")

    def find(self,data):
        if self.root:
            is_found = self._find(data,self.root)
            if is_found:
                return True
            return False
        return None

    def _find(self,data,cur_root):
        if data < cur_root.data and cur_root.left:
            return self._find(data,cur_root.left)
        elif data > cur_root.data and cur_root.right:
            return self._find(data,cur_root.right)
        
        else:
            return True
    def level_triversal(self):
        if self.root is None:
            print("Nodes are not defined yet!")
        else:
            order = ""
            que = Queue()
            que.enqueue(self.root)
            while len(que) > 0:
                val = que.dequeue()
                order += str(val.data) + " "
                if val.left:
                    que.enqueue(val.left)
                if val.right:
                    que.enqueue(val.right)
            return order

    def reverse_order_triversal(self):
        if self.root is None:
            print("Nodes are not defined!")
        else:
            que  = Queue()
            que.enqueue(self.root)
            List = []
            while len(que) > 0:
                val = que.dequeue()
                List.append(str(val.data))
                right = val.right
                left  = val.left
                if right:
                    que.enqueue(right)

                if left:
                    que.enqueue(left)
                    
            return self.str_arrange(List)

    def str_arrange(self,arr):
        arrange = ""

        for each in arr[::-1]:
            arrange += " " + each

        return arrange


    def order_print(self,type):
        if type == "level":
            print(self.level_triversal())
        if type == "rev level":
            print(self.reverse_order_triversal())

    def FindMx(self):
        if self.root is None:
            return "Tree is Empty"
        else:
            return self.findMx_(self.root)

    def findMx_(self,cur_root):
        if cur_root.right is None:
            return cur_root.data
        return self.findMx_(cur_root.right)
    
    def FindMn(self):
        if self.root is None:
            return "Tree is Empty"
        else:
            return self.findMn_(self.root)

    def findMn_(self,cur_root):
        if cur_root.left is None:
            cur_root.data = None
            return cur_root.data
        return self.findMx_(cur_root.left)

    def delete(self,val):
        if self.IsEmpty():
            return "Tree is Empty"
        else:
            self._delete(val,self.root)

    def _delete(self,val,cur_root):
        if val>cur_root.data:
            if cur_root.right:
                return self._delete(val,cur_root.right)
        elif val<cur_root.data:
            if cur_root.left:
                return self._delete(val,cur_root.left)
        else:
            cur_root.data = self.findMn_(cur_root)

    def height(self):
        if self.IsEmpty():
            return "Tree is Empty"
        else:
            return self._Height(self.root)

    def _Height(self,currentRoot):
        if currentRoot is None:
            return 0
        left = self._Height(currentRoot.left)
        right = self._Height(currentRoot.right)
        print(left,right)

        return 1 + max(left,right)

    def EularTour(self):
        if self.IsEmpty():
            print("Tree is Empty")
        else:
            deq = [self.root]
            #print(self.root)
            self.Eular_tour(self.root,deq)

    def Eular_tour(self,NwRoot,stack):
        if stack == []:
            return None
        
        stack.append(NwRoot)
        left = NwRoot.left
        print(NwRoot.data)
        if left:
            stack.append(left)
            self.Eular_tour(left,stack)
        
        right = NwRoot.right
        print(NwRoot.data)

        if right:
            stack.append(right)
            self.Eular_tour(right,stack)

        del stack[-1]
        
    def CreateTree(self, obj , Arr):
        for each in Arr:
            obj.insert(each)

    def Tree_Travesel(self , type):

        if self.IsEmpty():
            return "Tree is Empty"
        else:
            if type == "inorder":
                print("\nIn order Travesel\n")
                self._Inorder(self.root)

            elif type == "preorder":
                print("\nPre order Travesel\n")
                self._Preorder(self.root)


    def _Inorder(self,currentNode):

        if currentNode:
            L  = currentNode.left
            R  = currentNode.right

            self._Inorder(L)
            print(currentNode.data , end = " ")
            self._Inorder(R)

    def _Preorder(self,currentNode):

        if currentNode:
            L  = currentNode.left
            R  = currentNode.right

            print(currentNode.data , end = " ")
            self._Preorder(L)
            self._Preorder(R)



if __name__ == "__main__":               
    Tree = Binary_tree()   

    A = [6,3,7,2,4,9,1,8,10]

    Tree.CreateTree(Tree , A)

    #Tree.order_print("level")
    #Tree.EularTour()

    Tree.Tree_Travesel("preorder")
