class Node:
    def __init__(self,data=None,next=None) :
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertAtEnd(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        curr=self.head
        while(curr.next):
            curr=curr.next
        curr.next=Node(data,None)


    
    def printlist(self):
        if self.head is None:
            print("List is Empty")
            return
        curr=self.head
        
        while(curr):
            print(curr.data,end='-->')
            curr=curr.next
        print(None)
    def mergeTwo(self,l1,l2):
        temp=Node()
        head=temp

        if(l1==None):
            return l2
        if(l2==None):
            return l1
        while(l1 and l2):
            if(l1.data<l2.data):
                head.next=l1
                l1=l1.next
            else:
                head.next=l2
                l2=l2.next
            head=head.next
        if l1:
            head.next=l1
        else:
            head.next=l2
        return temp.next
        
        




if __name__=='__main__':
    obj=LinkedList()
    l1=LinkedList()
    l2=LinkedList()
    n=int(input())
    list1=list(map(int,input().strip().split()))
    for i in list1:
        l1.insertAtEnd(i)
    m=int(input())
    list2=list(map(int,input().strip().split()))
    for i in list2:
        l2.insertAtEnd(i)

    newList=obj.mergeTwo(l1.head,l2.head)
    while newList:
        print(newList.data,end='->')
        newList=newList.next
    print("Null")


