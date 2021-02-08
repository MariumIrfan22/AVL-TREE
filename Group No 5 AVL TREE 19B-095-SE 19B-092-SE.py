#!/usr/bin/env python
# coding: utf-8

# In[7]:


#AVL tree node class
class Node:   
    def __init__(self,value): 
        self.value=value
        self.left=None
        self.right=None
        self.height=0
        
class AVL:
    def __init__(self):
        self.root=None
        
    #wrapper function
    def InOrder(self):
        return self.__InOrder(self.root)
    
    #Inorder fucntion from bst lab which prints the value
    #in this order: left,root,right
    def __InOrder(self,root):
        if root is not None:
            return
            self.__InOrder(root.left)
            print(root.value)
            self.__InOrder(root.right)
            
    #wrapper function       
    def PreOrder(self):   
        return self.__PreOrder(self.root)
    
    #Preorder fucntion from bst lab which prints the value
    #in this order: root,left,right 
    def __PreOrder(self,root):
        if root is not None:
            print(root.value)
            self.__PreOrder(root.left)
            self.__PreOrder(root.right)
            
    #wrapper function       
    def PostOrder(self):
        return self.__PostOrder(self.root)
    
    #PostOrder fucntion from bst lab which prints the value
    #in this order: left,right,root
    def __PostOrder(self,root):
        if root is not None:
            self.__PostOrder(root.left)
            self.__PostOrder(root.right)
            print(root.value)
            
    #wrapper function
    def FindMax(self):
        x=self.__FindMax(self.root)
        return x.value
    
    #FindMax function which will find the maximum value 
    #from the tree
    def __FindMax(self,root):
        while root.right!=None:
            if root.right==None:
                break
            root=root.right
        return root
    
    #wrapper function
    def FindMin(self):
        x=self.__FindMin(self.root)
        return x.value
    
    #FindMin function which will find the minimum value 
    #from the tree
    def __FindMin(self,root): 
        
        while root.left!=None: 
            if root.left==None:
                break
            root=root.left 
        return root
    
    #wrapper function
    def Successor(self):
        x=self.__Successor(self.root)
        return x.value
    
    #it will return the min value from 
    #right subtree
    def __Successor(self,root):
        return self.__FindMin(root.right)
    
    #wrapper function
    def Predecessor(self):
        x=self.__Predecessor(self.root)
        return x.value
    
    #it will return the max value from 
    #left subtree
    def __Predecessor(self,root):
        return self.__FindMax(root.left)
    
    #wrapper function
    def get_height(self):
        return self.__get_height(self.root)
    
    #it returns the height
    def __get_height(self,root):
        if root is None:
            return 0
        return root.height
    
    #wrapper function
    def updateHeight(self):
        return self.__updateHeight(self.root)
    
    #it updates the height of the tree
    def __updateHeight(self,root):  
        return 1 + max(self.__get_height(self.root.left), self.__get_height(self.root.right))
    
    #it returns the difference between
    #left subtree and right subtree
    def BalanceFactor(self):
        if not self.root:
            return 0
        bf=self.__get_height(self.root.left)-self.__get_height(self.root.right)
        return bf
    
    #wrapper function
    def Insert(self,value):
        self.root= self.__Insert(self.root,value)
        
    def __Insert(self, root, value):
        if root is None:
            return Node(value)
        #inserting value in the tree
        if value < root.value:
            root.left = self.__Insert(root.left,value)
        else:
            root.right = self.__Insert(root.right,value)
        #updates height after insertion
        root.height=self.__updateHeight(root)
        #balances the tree if it is unbalance after insertion
        return self.rebalance(value)
        
    #wrapper function
    def leftRotation(self):
        return self.__leftRotation(self.root)
    
    #it rotates the root on left side and 
    #root's right child will become the root
    def __leftRotation(self,root):      
        rightchild = root.right
        x=rightchild.left
        #rotation
        rightchild.left=root
        root.right=x
        #updates the height
        root.height=self.__updateHeight(root)
        rightchild.height=self.__updateHeight(root)
        return rightchild
    
    #wrapper function
    def rightRotation(self):
        return self.__rightRotation(self.root)
    
    #it rotates the root on right side and 
    #root's left child will become the root
    def __rightRotation(self,root):
        leftchild=root.left
        x=leftchild.right
        #rotation
        leftchild.right=root
        root.left=x
        #updates the height
        root.height=self.__updateHeight(root)
        leftchild.height=self.__updateHeight(root)
        return leftchild
    
    def rebalance(self,value):
        #checks the balance factor
        balance = self.BalanceFactor()
        #balances the tree if the balance factor is not in(-1,0,1)
        if balance > 1 and value < self.root.left.value:
            return self.rightRotation()
        if balance < -1 and value > self.root.right.value:
            return self.leftRotation() 
        if balance > 1 and value > self.root.left.value:
            self.root.left = self.__leftRotation(self.root.left)
            return self.rightRotation()
        if balance < -1 and value < self.root.right.value:
            self.root.right = self.__rightRotation(self.root.right)
            return self.leftRotation()
        return self.root
    
    #wrapper function
    def Delete(self, v):
        return self.__delete(self.root, v)
        
    def __delete(self, root,value): 
        #deleting value from the tree just like we have done in bst
        if not root: 
            return root 
  
        elif value < root.value: 
            root.left = self.__delete(root.left, value) 
  
        elif value > root.value: 
            root.right = self.__delete(root.right, value) 
  
        else: 
            if root.left is None: 
                right = root.right 
                root = None
                return right
  
            elif root.right is None: 
                left= root.left 
                root = None
                return left 
            
        NodeSuccessor = self.__Successor(root)
        root.value = NodeSuccessor.value
        self.__delete(root.right, NodeSuccessor.value)
        
        if root is None: 
            return root
        #updates the height after deletion
        root.height =self.__updateHeight(root)
        #balances the tree if it is unbalance after deletion 
        return self.rebalance(value)
            
obj=AVL()
obj.Insert(7)
obj.Insert(9)
obj.Insert(10)
obj.Insert(8)
#obj.Delete(8)
obj.BalanceFactor()


# In[ ]:




