#include<iostream>
#include <queue>
using namespace std;

class node {
    public:
        int data;
        node* left;
        node* right;

    node(int d){ 
        this -> data = d;
        this -> left = NULL;
        this -> right = NULL;
    }
};

node* buildTree(node* root) {
    cout<<"Enter the data: " <<endl;
    int data;
    cin>>data;
    root = new node(data);

    if(data == -1){
        return NULL;
    }

    cout<<"Enter data for ins left of " <<data<<endl;
    root->left = buildTree(root-> left);
    cout<<"Enter data for ins right of " <<data<<endl;
    root->right = buildTree(root->right);
    return root;
}

void levelOrderTraversal(node* root) {
    queue<node*> q;
    q.push(root);
    q.push(NULL); // separator

    while(!q.empty()){
        node* temp = q.front();
        q.pop();

        if(temp == NULL){
            cout<<endl;
            if(!q.empty()){
                q.push(NULL);
            }
        }else {
            cout<<temp -> data << " "; 

            if(temp->left){
                q.push(temp->left);
            }

            if(temp->right){
                q.push(temp->right);
            }

        }
    }
}

void buildFromLevelOrder(node* &root){
    queue<node*> q;
    cout<<"Enter data for root" << endl;
    int data;
    cin>>data;
    root = new node(data);
    q.push(root);

    while(!q.empty()){
        node* temp = q.front();
        q.pop();

        cout<<"Enter left node for: "<<temp->data<<endl;
        int leftData;
        cin>>leftData;

        if(leftData!=-1){
            temp -> left = new node(leftData);
            q.push(temp->left);
        }

        cout<<"Enter right node for: "<<temp->data<<endl;
        int rightData;
        cin>>rightData;

        if(rightData!=-1){
            temp->right = new node(rightData);
            q.push(temp->right);
        }
    }
}

void inOrder(node* root){
    if(root == NULL){
        return;
    }

    inOrder(root->left);
    cout<<root->data<<" ";
    inOrder(root->right);
}

void preOrder(node* root){
    if(root == NULL){
        return;
    }

    cout<<root->data<<" ";
    inOrder(root->left);
    inOrder(root->right);
}

void postOrder(node* root){
    if(root == NULL){
        return;
    }

    inOrder(root->left);
    inOrder(root->right);
    cout<<root->data<<" ";
}



int main() {
    node* root = NULL;
    buildFromLevelOrder(root);
    levelOrderTraversal(root);
    // root = buildTree(root);
    // //  1 3 7 -1 -1 11 -1 -1 5 17 -1 -1 -1
    // cout<<"INORDER TRAVERSAL ";
    // inOrder(root);
    // cout<<"PRE  ORDER TRAVERSAL ";
    // preOrder(root);
    // cout<<"POST ORDERTRAVERSAL ";
    // postOrder(root);
    // return 0;
}