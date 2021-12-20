class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        print("New Node Created with data %d" % (data))


class Circular_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        temp = self.head
        if temp is None:
            return 0
        length = 0
        while 1:
            length += 1
            temp = temp.next
            if temp == self.head:
                break
        return length

    def get_pre_position(self, position: int):
        """
        Get_Pre_Position:
            Position:int
            index starting from 0
        """
        if position <= 0:
            return self.tail
        temp = self.head
        position -= 1
        while position > 0:
            position -= 1
            temp = temp.next
        return temp

    def insert_at_beginning(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.next = new_node
            self.head, self.tail = new_node, new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head, self.tail.next = new_node, new_node

    def insert_at_end(self, data):
        if self.tail == None:
            if self.head:
                print("Some error in the program")
                return None
            else:
                self.insert_at_beginning(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.tail.next, self.tail = new_node, new_node

    def insert(self, data, /, end=False, position=None):
        """
        Insert:
            data:data to insert
            end: To insert at the end of the list
                    position: To insert at  postion from the end
            Position:
                to insert at the position
        """

        """
            length : length of the head
        """
        if self.head is None:
            length = 0
        else:
            length = len(self)

        """
            validating Position
        """
        if position != None and (position < 0 or position > length):
            print(
                "Position should be greater than or equal 0 and less then or equal to %d "
                % (length)
            )
        elif end is False:
            # print("----")
            """

            Position is none then it should be inserted at the beginning

            else
                to be inserted at the given position from the beginning


                position is 0 insert at 1st

                position is same as lenght it should be insert at the end

                getting the pre position and then storing

            """
            if position is None:
                self.insert_at_beginning(data)
            else:
                if position == 0:
                    self.insert_at_beginning(data)
                elif position == len(self):
                    self.insert_at_end(data)
                else:
                    # print("=====")
                    # print(position)
                    # self.display()
                    temp = self.get_pre_position(position)
                    # print(temp.data)
                    new_node = Node(data)
                    temp.next, new_node.next = new_node, temp.next
                    self.display()
        else:
            """
            postion is none ->should be inserted at the end

            postion is 0 ->should be inserted at the 0th position from the end(insert at the end)

            postion is length -> should be insert at the beginning

            get the pre psotion and insert
            """
            if position is None:
                self.insert_at_end(data)
            else:
                if position == 0:
                    self.insert_at_end(data)
                elif position == length:
                    self.insert_at_beginning(data)
                else:
                    position = length - position
                    temp = self.get_pre_position(position)
                    new_node = Node(data)
                    temp.next, new_node.next = new_node, temp.next
        return self

    def delete_at_beginning(self, data=None):
        """
        Delete At Beginning:
            data:
                if data is given delete the data
                else delete at beginning
        """
        if data:
            if self.head is None:
                print("No data to delete")
            elif self.head == self.tail:
                if data == self.head.data:
                    self.head, self.tail = None, None
            else:
                if self.head.data == data:
                    self.head, self.tail.next = self.head.next, self.head.next
                elif self.tail.data == data:
                    prev = self.get_pre_position(len(self))
                    prev.next, self.tail = self.head, prev
                else:
                    temp = self.head
                    prev = self.tail
                    while 1:
                        if temp.data == data:
                            prev.next = temp.next
                            break
                        temp = temp.next
                        prev = prev.next
                        if temp == self.head:
                            break
        else:
            if self.head == None:
                print("No data to delete")
            elif self.tail == self.head:
                self.head, self.tail = None, None
            else:
                self.head, self.tail.next = self.head.next, self.head.next

    def delete_at_end(self):
        if self.head == None:
            print("No Node to delete")
            return None
        if self.head == self.tail:
            print("Node is deleted at the EnD")
            return
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next
        print("Node with teh data %d at the end is deleted" % (temp.next.data))
        temp.next = temp.next.next
        self.tail = temp

    def delete(self, /, data=None, end=False, position=None, all=False):
        """
        Delete:
            data: data to delete
            end: to delete the data from the end
            position: to delete the data from at the given position
            all: to delete all the data

        """
        if data is None:
            if end is False:
                if position is None:
                    if all is False:
                        """
                        Delete At the Beginning
                        """
                        self.delete_at_beginning()
                    else:
                        """
                        delete all the data
                        """
                        self.head, self.tail = None, None
                        print("List is cleared")
                else:
                    if all is False:
                        """
                        delete at the given position
                        """
                        if position == 0:
                            self.delete_at_beginning(data)
                        elif position == len(self):
                            self.delete_at_end(data)
                        else:
                            temp = self.get_pre_position(position)
                            new_node = Node(data)
                            temp.next, new_node.next = new_node, temp.next
                        pass
                    else:
                        """
                        delete all the occurance data at the given position
                        """
                        temp = self.get_pre_position(position)  # getting the position
                        
                        temp_head=self.head
                        while 1:
                            # if temp_head
                            temp_head=temp_head.next
                            if temp_head==self.head:
                                     break
                        
            else:
                if position is None:
                    if all is False:
                        self.delete_at_end()
                    else:
                        # end and all
                        pass
                else:
                    if all is False:
                        # end position is given
                        pass
                    else:
                        # end position and all is given
                        pass
        else:
            if end is False:
                if position is None:
                    if all is False:
                        # data
                        pass
                    else:
                        # data all
                        pass
                else:
                    # data position i sgiven
                    pass
            else:
                if position is None:
                    # data end
                    # all not used
                    pass
                else:
                    # data end position i sgiven
                    # all not used
                    pass
        pass

    def display(self):
        """
        Display:
            if head is none:
                list is empty
                reterns the self of this class
            started displaying the nodes
            temp is assigned of head of the node list
            temp is traveled till the end of the list
                by displaying the values in each node
            returns the self of this class
        """
        if self.head == None:
            print("No Nodes to display")
            return self
        print("Nodes are: ", end=" ")
        temp = self.head
        while temp != self.tail:
            print(temp.data, end=" ")
            temp = temp.next
        print(temp.data)
        return self


if __name__ == "__main__":
    head = Circular_Linked_List()
    head.insert(4).insert(2).insert(3, position=1).insert(5, position=0, end=1).insert(
        1
    )
    head.display()
    head.delete(position=4, all=1)
    head.display()
    # head.delete().display()
    # head.delete(end=True).display()
    # head.delete(data=6, end=True, all=True).display()
