#include <iostream>

using namespace std;

class Node {
public:
    int data;
    Node* next;

    Node() {
        this->data = 0;
        this->next = NULL;
    }

    Node(int data) {
        this->data = data;
        this->next = NULL;
    }
};

void insertAtHead(Node* &head, Node* &tail, int data) {
    Node* newNode = new Node(data);
    if (head == NULL) {
        head = newNode;
        tail = newNode;
    } else {
        newNode->next = head;
        head = newNode;
    }
}

void insertAtTail(Node* &head, Node* &tail, int data) {
    Node* newNode = new Node(data);
    if (tail == NULL) {
        tail = newNode;
        head = newNode;
    } else {
        tail->next = newNode;
        tail = newNode;
    }
}

void insertAtPosition(Node* &head, Node* &tail, int data, int position) {
    if (head == NULL) {
        Node* newNode = new Node(data);
        head = newNode;
        tail = newNode;
        return;
    }

    if (position == 1) {  
        insertAtHead(head, tail, data);
        return;
    }

    int i = 1;
    Node* prev = head;
    while (i < position - 1 && prev != NULL) { 
        prev = prev->next;
        i++;
    }

    if (prev == NULL) { 
        cout << "Position out of range" << endl;
        return;
    }

    Node* newNode = new Node(data);
    newNode->next = prev->next;
    prev->next = newNode;

    if (newNode->next == NULL) {
        tail = newNode;
    }
}

void print(Node* &head) {
    Node* temp = head;
    while (temp != NULL) {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

int main() {
    Node* head = NULL;
    Node* tail = NULL;

    insertAtHead(head, tail, 5);
    insertAtTail(head, tail, 88);
    insertAtHead(head, tail, 15);
    insertAtHead(head, tail, 153);
    insertAtHead(head, tail, 115);
    insertAtHead(head, tail, 23);

    print(head);

    insertAtPosition(head, tail, 101, 1);
    print(head);

    return 0;
}
