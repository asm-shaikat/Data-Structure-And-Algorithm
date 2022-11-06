#include<bits/stdc++.h>
using namespace std;

class Node{
    public:
    int data;
    Node *next;
};
void show( Node *node){
    while(node!=NULL){
        cout<<node->data<<" ";
        node = node->next;
    }
}
int main(){
    Node *head = NULL;
    Node *middle = NULL;
    Node *tail = NULL;


    head = new Node;
    middle = new Node;
    tail = new Node;

    head->data = 57;
    head->next = middle;

    middle->data = 58;
    middle->next = tail;

    tail->data = 59;
    tail->next = NULL;

    
    show(head);
}