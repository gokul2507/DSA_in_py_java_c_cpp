#include <iostream>
using namespace std;

struct Node
{
    int data;
    Node *next;
};

class sll
{
    Node *head;

public:
    sll()
    {
        head = NULL;
    }
    Node *node(int data)
    {
        Node *new_node = new Node;
        new_node->data = data;
        new_node->next = NULL;
    }
    void insert(int data, bool end = false)
    {
        if (end)
        {
            if (this->head == NULL)
            {
                this->head = node(data);
            }
            else
            {
                Node *temp = this->head;
                while (temp->next)
                {
                    temp = temp->next;
                }
                temp->next = node(data);
            }
        }
        else
        {
            Node *temp = node(data);
            temp->next = this->head;
            this->head = temp;
        }
    }
    void delet(int data = NULL, bool end = false, bool all = false)
    {
        if (all)
        {
            if (data == NULL)
            {
                cout << "No Data is given\n";
                return;
            }
            Node *temp = this->head;
            while (temp->next)
            {
                if (temp->next->data == data)
                {
                    temp->next = temp->next->next;
                    if (temp->next == NULL)
                        break;
                }
                temp = temp->next;
            }
            cout << "All the Node with Data " << data << " is deleted\n";
        }
        else
        {
            if (end == false)
            {
                if (data == NULL)
                {
                    if (this->head == NULL)
                        cout << "No Node to delete\n";
                    else
                    {
                        this->head = this->head->next;
                        cout << "Node is Deleted at the Beginning\n";
                    }
                }
                else
                {
                    if (this->head == NULL)
                        cout << "No Node to delete\n";
                    else
                    {
                        if (this->head->next == NULL)
                        {
                            if (this->head->data == data)
                            {
                                this->head = this->head->next;
                                cout << "Node with data " << data << " is Deleted at the Beginning\n";
                            }
                        }
                        else
                        {
                            Node *temp = this->head;
                            while (temp->next != NULL)
                            {
                                if (temp->next->data == data)
                                {
                                    temp->next = temp->next->next;
                                    cout << "Node with data " << data << "is Deleted at the Beginning\n";
                                    break;
                                }
                                temp = temp->next;
                            }
                        }
                    }
                }
            }
            else
            {
                if (data == NULL)
                {
                    if (this->head == NULL)
                        cout << "NO data to delete\n";
                    else
                    {
                        if (this->head->next == NULL)
                        {
                            this->head = this->head->next;
                        }
                        else
                        {
                            Node *temp = this->head;
                            while (temp->next->next != NULL)
                                temp = temp->next;
                            temp->next = temp->next->next;
                            cout << "Node is Deleted at the end\n";
                        }
                    }
                }
                else
                {
                    if (this->head == NULL)
                    {
                        cout << "No data to delete\n";
                    }
                    else
                    {
                        Node *prev = NULL;
                        Node *temp_pre = NULL;
                        bool valid = false;
                        Node *temp = this->head;
                        while (temp != NULL)
                        {
                            if (temp->data == data)
                            {
                                temp_pre = prev;
                                valid = true;
                            }
                            prev = temp;
                            temp = temp->next;
                        }
                        if (valid)
                        {
                            if (temp_pre == NULL)
                            {
                                this->head = this->head->next;
                            }
                            else
                            {
                                temp_pre->next = temp_pre->next->next;
                            }
                        }
                    }
                }
            }
        }
    }
    void replace(int old_data, int new_data, bool all = false)
    {
        Node *temp = this->head;
        while (temp)
        {
            if (temp->data == old_data)
            {
                temp->data = new_data;
                if (!all)
                    break;
            }
            temp = temp->next;
        }
    }
    int length()
    {
        int length = 0;
        Node *temp = this->head;
        while (temp)
        {
            length++;
            temp = temp->next;
        }
        return length;
    }
    void rotate(int times)
    {
        if (this->head == NULL || this->head->next == NULL)
            return;
        int length = this->length();
        times %= length;
        Node *tail = this->head;
        while (times--)
        {
            tail->next = this->head;
            tail = tail->next;
            this->head = this->head->next;
            tail->next = NULL;
        }
        cout << "Node are rotated\n";
    }
    void display()
    {
        Node *temp = this->head;
        while (temp)
        {
            cout << temp->data << " ";
            temp = temp->next;
        }
        cout << endl;
    }
};

int main()
{
    sll head;
    head.insert(5, true);
    head.insert(6, true);
    head.insert(7, true);
    head.insert(5, true);
    head.insert(9, true);
    head.insert(10, true);
    head.insert(4);
    head.insert(3);
    head.insert(2);
    head.insert(5);
    head.display();
    head.delet();
    head.display();
    head.replace(5, 0, true);
    head.rotate(5);
    head.display();
    return 0;
}
