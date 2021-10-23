#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node
{
    char kata[30];
    long int startArti;
    struct node* left, *right;
} node;

void _insert();
void insert();
node *newNode();

node *table[26];

int main(){
    for(int i = 0; i < 26; i++){
        table[i] = NULL;
    }


    insert("anjing", 140, &table[0]);
    insert("a", 141, &table[0]);
    insert("b", 141, &table[0]);
    printf("%s", table[0]->kata);
    printf("\n%s", table[0]->left->kata);
    printf("\n%s", table[0]->right->kata);

}

node *newNode(char kata[30], long int startArti){
    node* new = (node*)malloc(sizeof(node));
    strcpy(new->kata, kata);
    new->startArti = startArti;
    new->left = new->right = NULL;

    return new;
}

void insert(char kata[20],long int arti, node **root) {
    if (*root == NULL)
        *root = newNode(kata, arti);
    else
        _insert(kata, arti, root);
}

void _insert(char kata[20],long int arti, node **parent) {
    node *temp = *parent;
    if (strcmp(kata, temp->kata) < 0) {
        if (temp->left == NULL) {
            temp->left = newNode(kata, arti);
            return;
        }
        _insert(kata, arti, &temp->left);
    } else {
        if (temp->right == NULL) {
            temp->right = newNode(kata, arti);
            return;
        }
        _insert(kata, arti, &temp->right);
    }
}