#include<stdio.h>
#include<stdlib.h>
struct Node{
    int data;
    struct Node* next;
};
struct Node *New_Node(int data){
    struct Node* new_node=(struct Node*)malloc(sizeof(struct Node));
    new_node->data=data;
    new_node->next = NULL;
    printf("New Node Created with data %d\n",data);
    return new_node;
}
struct Node *insert_at_beginning(struct Node *h,int data){
    struct Node *temp=New_Node(data);
    temp->next=h;
    h=temp;
    printf("New Node Inserted with data %d at the Beginning\n",data);
    return h;
}
struct Node *insert_at_end(struct Node *h,int data){
    if(h == NULL){
        h=New_Node(data);
        printf("New Node Inserted with data %d at the End\n",data);
    }
    else{
        struct Node* temp=h;
        while(temp->next){
            temp=temp->next;
        }
        temp->next=New_Node(data);
        printf("New Node Inserted with data %d at the End\n",data);
    }
    return h;
}
struct Node *delete_at_beginning_without_data(struct Node *h){
    if(h==NULL){
        printf("No Node to delete\n");
        return h;
    }
    else{
        h=h->next;
        printf("Node is Deleted\n");
        return h;
    }
}
struct Node *delete_at_end_without_data(struct Node *h){
    if(h==NULL){
        printf("No Node to delete\n");
        return h;
    }
    if(h->next==NULL){
        h=h->next;
        printf("Node is Deleted\n");
        return h; 
    }
    struct Node *t=h;
    while(t->next->next){
        t=t->next;
    }
    t->next=t->next->next;
    printf("Node is Deleted\n");
    return h; 
}
struct Node *delete_at_beginning_with_data(struct Node *h,int data){
    if(h==NULL){
        printf("No Node to delete\n");
        return h;
    }
    if(h->data==data){
        printf("Node is Deleted\n");
        return h->next;
    }
    else{
        struct Node *temp=h;
        while(temp->next){
            if(temp->next->data==data){
                temp->next=temp->next->next;
                printf("Node is Deleted\n");
                break;
            }
            temp=temp->next;
        }
        return h;
    }
}
struct Node *delete_at_end_with_data(struct Node *h,int data){
    if(h==NULL){
        printf("No Node to delete\n");
        return h;
    }
    struct Node *pre=NULL,*temp_pre=NULL,*last_data=NULL,*temp=h;
    while(temp){
        if(temp->data==data){
            temp_pre=pre;
            last_data=temp;
        }
        pre=temp;
        temp=temp->next;
    }
    if(temp_pre==NULL){
        h=h->next;
        printf("Node is Deleted\n");
    }
    else{
        temp_pre->next=temp_pre->next->next;
        printf("Node is Deleted\n");
    }
    return h;
}
struct Node *replace(struct Node * h,int old_data,int new_data){
    struct Node *temp=h;
    int flag=1;
    while(temp){
        if(temp->data==old_data){
            temp->data=new_data;
            flag=0;
            printf("%d is Replaced with %d\n",old_data,new_data);
            break;
        }
        temp=temp->next;
    }
    if(flag){
        printf("No such data(%d)\n",old_data);
    }
    return h;
}
struct Node *replace_all(struct Node *h,int old_data,int new_data){
    struct Node *temp=h;
    int count=0;
    while(temp){
        if(temp->data==old_data){
            temp->data=new_data;
            count++;
        }
        temp=temp->next;
    }
    if(count){
        printf("All the instances of %d is replaced with %d\n",count,old_data,new_data);
    }
    else{
        printf("No such data(%d)\n",old_data);
    }
    return h;
}
int length(struct Node *h){
    int len=0;
    while(h){
        len++;
        h=h->next;
    }
    return len;
}
struct Node *rotate(struct Node *h,int times){
    if(h==NULL || h->next==NULL)
    return h;
    int len=length(h);
    times%=len;
    struct Node *tail=h;
    while(tail->next)
    tail=tail->next;
    while(times--){
        tail->next=h;
        tail=tail->next;
        h=h->next;
        tail->next=NULL;
    }
    printf("Node is rotated\n");
    return h;
}
void display(struct  Node *h){
    if(h==NULL){
        printf("No data to display\n");
        return;
    }
    printf("Datas are: ");
    struct Node *temp=h;
    while(temp){
        printf("%d ",temp->data);
        temp=temp->next;
    }
    printf("\n");
}
void main(){
    struct Node *head=NULL;
    head=insert_at_end(head,5);
    head=insert_at_end(head,6);
    head=insert_at_end(head,7);
    head=insert_at_end(head,8);
    head=insert_at_end(head,9);
    head=insert_at_end(head,8);
    head=insert_at_end(head,8);
    head=insert_at_end(head,9);
    display(head);
    head=delete_at_end(head,5);
    display(head);
    head=delete_at_end_without_data(head);
    display(head);
    head=replace(head,8,0);
    display(head);
    head=replace_all(head,8,5);
    display(head);
    head=rotate(head,2);
    display(head);
}