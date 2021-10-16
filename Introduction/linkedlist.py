class node:

    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:

    def __init__(self):
        self.head=None

    def printList(self):
        itr=self.head
        while(itr):
            print(itr.data,'-->',end="")
            itr=itr.next


if __name__=='__main__':

    llist=linkedlist()

    llist.head=node(1)
    
    second=node(2)
    third=node(3)

    llist.head.next=second

    second.next=third

    llist.printList()

    arr=[4,5,6,9,32]