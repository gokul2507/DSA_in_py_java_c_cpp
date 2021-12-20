class Node {
    int data;
    Node next;

    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class sll {
    Node head;

    public sll() {
        this.head = null;
    }

    public sll insert(int data, boolean end) {
        /*
         * Insertion: data: compalsary end: optional(default: false)
         * 
         * if end is false create a new node using Node head is added next to the new
         * nodes then new node is set to head
         * 
         * else (if end is false) if head is null head is assigned a new node using Node
         * if head is not null head is stored in temp temp is traveled to last node then
         * a new node is add next to the temp node using Node returns teh self of this
         * class
         */
        if (!end) {
            Node new_node = new Node(data);
            new_node.next = this.head;
            this.head = new_node;
            System.out.println("New Node Inserted with data " + data + " at the Beginning");
        } else {
            if (this.head == null) {
                this.head = new Node(data);
                System.out.println("New Node Inserted with data " + data + " at the End");
            } else {
                Node temp = this.head;
                while (temp.next != null) {
                    temp = temp.next;
                }
                temp.next = new Node(data);
                System.out.println("New Node Inserted with data " + data + " at the End");
            }
        }
        return this;
    }

    public sll insert(int x) {
        return insert(x, false);
    }

    public sll delete(boolean data_passed, int data, boolean end, boolean all) {
        if (all) {
            if (!data_passed) {
                System.out.println("No data is given");
                return this;
            }
            Node temp = this.head;
            while (temp.next != null) {
                if (temp.next.data == data) {
                    temp.next = temp.next.next;
                    if (temp.next == null)
                        break;
                }
                temp = temp.next;
            }
            System.out.println("All the Node with Data " + data + " is deleted");
        } else {
            if (!end) {
                if (!data_passed) {
                    if (this.head == null) {
                        System.out.println("No Node to delete");
                    } else {
                        this.head = this.head.next;
                        System.out.println("Node is Deleted at the Beginning");
                    }
                } else {
                    if (this.head == null)
                        System.out.println("No Node to delete");
                    else {
                        if (this.head.next == null) {
                            if (this.head.data == data) {
                                this.head = this.head.next;
                                System.out.println("Node with data " + data + " is Deleted at the Beginning");
                            }
                        } else {
                            Node temp = this.head;
                            while (temp.next != null) {
                                if (temp.next.data == data) {
                                    temp.next = temp.next.next;
                                    System.out.println("Node with data " + data + "is Deleted at the Beginning");
                                    break;
                                }
                                temp = temp.next;
                            }
                        }
                    }
                }
            } else {
                if (!data_passed) {

                    if (this.head == null)
                        System.out.println("NO data to delete");
                    else {
                        if (this.head.next == null) {
                            this.head = this.head.next;
                        } else {
                            Node temp = this.head;
                            while (temp.next.next != null)
                                temp = temp.next;
                            temp.next = temp.next.next;
                            System.out.println("Node is Deleted at the end");
                        }
                    }
                } else {
                    if (this.head == null) {
                        System.out.println("No data to delete");
                        return this;
                    } else {
                        Node prev = null, temp_pre = null;
                        boolean valid = false;
                        Node temp = this.head;
                        while (temp != null) {
                            if (temp.data == data) {
                                temp_pre = prev;
                                valid = true;
                            }
                            prev = temp;
                            temp=temp.next;
                        }
                        if (temp_pre == null) {
                            if (valid)
                                this.head = this.head.next;
                        } else
                            temp_pre = temp_pre.next.next;
                    }
                }
            }
        }
        return this;
    }

    public sll delete() {
        return delete(false, 0, false, false);
    }

    public sll delete(int data) {
        return delete(true, data, false, false);
    }

    public sll delete(int data, boolean end, boolean all) {
        return delete(true, data, end, all);
    }

    public sll delete(boolean end) {
        return delete(false, 0, end, false);
    }

    public sll replace(int old_data, int new_data) {
        Node temp = this.head;
        while (temp != null) {
            if (temp.data == old_data) {
                temp.data = new_data;
                System.out.println(old_data + " is Replaced with " + new_data);
                break;
            }
            temp = temp.next;
        }
        return this;
    }

    public sll replace_all(int old_data, int new_data) {
        Node temp = this.head;
        while (temp != null) {
            if (temp.data == old_data) {
                temp.data = new_data;

            }
            temp = temp.next;
        }
        System.out.println("All the instances of " + old_data + " is Replaced with " + new_data);
        return this;
    }

    public int length(){
        int length=0;
        Node temp = this.head;
        while(temp != null) {
            length++;
            temp = temp.next;
        }
        return length;
    }

    public sll rotate(int times){
        if(this.head == null || this.head.next== null){
            return this;
        }
        int length=this.length();
        times%=length;
        // System.out.println(times);
        Node tail=this.head;
        while(tail.next!= null)
        tail=tail.next;
        while(times>0){
            times--;
            tail.next=this.head;
            tail=tail.next;
            this.head=this.head.next;
            tail.next=null;
        }
        System.out.println("Nodes are rotated");
        return this;
    }

    public sll display() {
        if (this.head == null) {
            System.out.println("No Node to display");
            return this;
        }
        System.out.print("Nodes are: ");
        Node temp = this.head;
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
        return this;
    }
}

public class Singly_Linked_List {
    public static void main(String[] args) {
        System.out.println("\n");
        sll x = new sll();
        x.insert(5, true).insert(6, true).insert(7, true).insert(8, true).insert(9, true).insert(10, true).insert(4)
                .insert(3).insert(2).insert(1);
        /*x.display();
        x.delete(5).display();
        x.delete().display();
        x.delete(true).display();
        x.delete(6, true, true).display();
        x.display();*/
        x.replace(2, -1).display();
        x.rotate(9).display();
    }
}