

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        print("New Node Created with data %d"%(data))

class Singly_Linked_List:
    def __init__(self):
        self.head=None

    
    def insert(self,data,/,end=False):
        '''
        Insertion:
            data: compalsary
            end:  optional(default: false)
            
            if end is false
                create a new node using Node
                head is added next to the new nodes
                then new node is set to head
            
            else (if end is false)
                if head is null
                    head is assigned a new node using Node
                if head is not null
                    head is stored in temp
                    temp is traveled to last node
                    then a new node is add next to the temp node using Node
            returns the self of this class
        '''
        if end is False:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
            print("New Node Inserted with data %d at the Beginning"%(data))
        else:
            if self.head==None:
                self.head=Node(data)
                print("New Node Inserted with data %d at the End"%(data))
            else:
                temp=self.head
                while temp.next:
                    temp=temp.next
                temp.next=Node(data)
                print("New Node Inserted with data %d at the End"%(data))
        return self
    
    '''
        Delete:
        Data:  optional
        end:   optional
        all:   optional
        if all is True: (deleting all the occurance of teh data)
            if data is None:
                error => No data is given to delete in the list
                returns the self of this class
            head is assigned to temp 
            passing the temp in while till next node of exist
                if the data in next node of the temp then
                    (deleting the node)
                    next node of the next node of the temp is 
                    assigned to
                    next node of the temp
                next node of the temp is assigned to temp
        if end is None: (deleting at the beginning)
            if data is None: (deleting at the beginning)
                if head is None:
                    No data to delete from the list
                else:
                    next node of head is assigned to head
                    ( if next node of head is null 
                    it shows that list have only one 
                    node so that node is deleted
                    by assigned next node of the head(null) to the head
                    )
            if data is not None:(delete a node whose data is matching with the given data)
                if head is not None:
                    head have no data to delete
                if head have only one node to delete
                    and that node have the given data:
                        assigned next node of the head(null) to the head
                else:
                    head is assigned to temp
                    passing the temp in while till next node of exist
                        if data of next node of temp is givendata:
                            deleting the node
                            and then breaking the while loop
                        next node of temp is assigned to temp
        else:
            if data is None:
                if head is None:
                    no data to delete
                if head have only one node:
                    next node of head is assigned to head
                    ( if next node of head is null 
                    it shows that list have only one 
                    node so that node is deleted
                    by assigned next node of the head(null) to the head
                    )
                else:
                    head is assigned to temp
                    passing the temp in while till next node of exist
                        next node of temp is assigned to temp
                    (temp is traveled to previous node of last node in the list)
                    and that node is deleted
            else:
                if head is None:
                    no data to delete
                else: (deleting the last occurance of data)
                    previous, temp_previous,valid set all to None
                    head is assigned to temp
                    passing the temp in while till next node of exist
                        if data in temp is matching to the given data:
                            store the previous to temp_previous and
                            True to valid
                        store temp to previous
                    if temp_previous is None:
                        if valid is True:(last occurance of data is found on the first node)
                            store next node of head to head
                    else:
                        store next node of next node of temp_pre to next node of temp_pre
        returns the self of this class
    '''
    def delete(self,*,data=None,end=None,all=False):
        if all:
            if data==None:
                print("No data is given")
                return self
            temp=self.head
            while temp.next:
                if temp.next.data==data:
                    temp.next=temp.next.next
                    if temp.next==None:
                        break
                temp=temp.next
            print("All the Node with Data%d is deleted"%(data))
        elif end is None:
            if data==None:
                if self.head==None:
                    print("No Node to delete")
                else:
                    self.head=self.head.next
                    print("Node is Deleted at the Beginning")
            else:
                if self.head==None :
                    print("No Node to delete")
                elif self.head.next==None:
                    if self.head.data==data:
                        self.head=self.head.next
                        print("Node with data %d is Deleted at the Beginning"%(data))
                else:
                    temp=self.head
                    while temp.next:
                        if temp.next.data==data:
                            temp.next=temp.next.next
                            print("Node with data %d is Deleted at the Beginning"%(data))
                            break
                        temp=temp.next
        else:
            if data==None:
                if self.head==None:
                    print("No data to delete")
                elif self.head.next==None:
                    self.head=self.head.next
                    print("Node is Deleted at the End")
                else:
                    temp=self.head
                    while temp.next.next:
                        temp=temp.next
                    temp.next=temp.next.next
                    print("Node is Deleted at the End")
            else:
                if self.head==None:
                    print("No data to delete")       
                    return self
                else:
                    pre=temp_pre=valid=None
                    temp=self.head
                    while temp:
                        if temp.data==data:
                            temp_pre=pre
                            valid=True
                        pre=temp
                        temp=temp.next;
                    if temp_pre==None:
                        if valid:
                            self.head=self.head.next
                    else:
                        temp_pre.next=temp_pre.next.next
                    print("Node with data %d is Deleted at the End"%(data))
        return self
    
    def replace(self,old_data,new_data):
        temp=self.head
        while temp:
            if temp.data==old_data:
                temp.data=new_data
                print("%d is Replaced with %d"%(old_data,new_data))
                break
            temp=temp.next
        return self
    
    def replace_all(self,old_data,new_data):
        temp=self.head
        while temp:
            if temp.data==old_data:
                temp.data=new_data
            temp=temp.next
        print("All the instances of %d is replaced with %d"%(old_data,new_data))
        return self

    def __len__(self):
        length=0
        temp=self.head
        while temp:
            length+=1
            temp=temp.next
        return length
    
    def rotate(self,times):
        if self.head==None or self.head.next==None:
            return self
        length=len(self)
        times%=length
        tail=self.head
        while tail.next:
            tail=tail.next
        while times:
            times-=1
            tail.next=self.head
            tail=tail.next
            self.head=self.head.next
            tail.next=None
        print("Nodes are rotated")
        return self
        
    def display(self):
        '''
        Display:
            if head is none:
                list is empty
                reterns the self of this class
            started displaying the nodes
            temp is assigned t head of the node list
            temp is traveled till the end of the list
                by displaying the values in each node
            returns the self of this class
        '''
        if self.head==None:
            print("No Nodes to display")
            return self
        print("Nodes are: ",end=' ')
        temp=self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next
        print()
        return self

if __name__=='__main__':
    head=Singly_Linked_List()
    head.insert(5,True).insert(6,True).insert(7,True).insert(8,True).insert(6,True).insert(10,True).insert(4).insert(3).insert(2).insert(1);
    head.display()
    head.delete(data=5).display()
    head.delete().display()
    head.delete(end=True).display()
    head.delete(data=6,end=True,all=True).display()