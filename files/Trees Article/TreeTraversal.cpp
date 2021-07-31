#include<iostream>
using namespace std;

class Node
{
    public:
        int data;
        Node* left;
        Node* right;

        void insertNode(int num);
};

void printPreOrder(Node* root)
{
    if(root != NULL)
    {
        cout << root->data << " "; //Print current node
        printPreOrder(root->left); //Visit left tree
        printPreOrder(root->right); //Visit right tree
    }
    cout << "\n"; //Print newline
}

int main(void)
{
    Node* tree = new Node;
    tree->data = 1; //Insert data

//Create left and right nodes
    tree->left = new Node;
    tree->right = new Node;

//Insert data
    tree->left->data = -10;
    tree->right->data = 20;

//Print tree
    printPreOrder(tree);


//Free nodes
    delete tree->left;
    delete tree->right;
    delete tree;
}