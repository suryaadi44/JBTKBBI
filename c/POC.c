#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node {
    char kata[30];
    long startArti;
    struct node* left, * right;
} node;

void _insert();
void insert();
void printArti();
void _printArti();
void loadTable();
int hash();
int cekBaris(char file[]);
node* newNode();
node* search();
node* _search();

node* table[26];

char fileNames[26][20] = { "DB/kbbi_a.csv", "DB/kbbi_b.csv", "DB/kbbi_c.csv", "DB/kbbi_d.csv", "DB/kbbi_e.csv", "DB/kbbi_f.csv", "DB/kbbi_g.csv", "DB/kbbi_h.csv", "DB/kbbi_i.csv", "DB/kbbi_j.csv", "DB/kbbi_k.csv", "DB/kbbi_l.csv", "DB/kbbi_m.csv","DB/kbbi_n.csv", "DB/kbbi_o.csv", "DB/kbbi_p.csv", "DB/kbbi_q.csv", "DB/kbbi_r.csv", "DB/kbbi_s.csv", "DB/kbbi_t.csv", "DB/kbbi_u.csv", "DB/kbbi_v.csv", "DB/kbbi_w.csv", "DB/kbbi_x.csv", "DB/kbbi_y.csv", "DB/kbbi_z.csv" };

int main() {
    loadTable();
    //insert("anjing", 140, &table[0]);
    //insert("a", 141, &table[0]);
    //insert("b", 141, &table[0]);
    //printf("%s", table[0]->kata);
    //printf("\n%s", table[0]->left->kata);
    //printf("\n%s", table[0]->right->kata);


    printArti("anjing");
}

void loadTable() {
    for (int i = 0; i < 26; i++) {
        FILE* fp;

        int baris = cekBaris(fileNames[i]);
        //printf("\n%d : %s",baris, fileNames[i]);

        fp = fopen(fileNames[i], "r");
        for (int j = 0; j < baris; j++) {
            char kata[30], arti[14000];
            //long startKata = ftell(fp);
            fscanf(fp, "\"%[^\"]\",\"", kata);
            long startArti = ftell(fp);
            fscanf(fp, "%[^\"]\"\n", arti);
            //long endArti = ftell(fp);

            insert(kata, startArti, &table[i]);
            //printf("\n%s : %d", kata, startArti);
        }
        fclose(fp);
    }
}

int cekBaris(char file[]) {
    FILE* cek;
    int i = 0;
    int cs;

    cek = fopen(file, "r");
    while (!feof(cek)) {              //Loop hingga EOF  1
        cs = fgetc(cek);               //simpan stream char ke c
        if (cs == '\n') i++;         //Jika dideteksi \n , tambah i
    }
    fclose(cek);
    return i;
}

void printArti(char kata[30]) {
    node* temp = search(kata);
    _printArti(temp->startArti, hash(kata));
}

void _printArti(long startArti, int fileIndex) {
    char arti[14000];
    FILE* fp;
    fp = fopen(fileNames[fileIndex], "r");
    fseek(fp, startArti, SEEK_SET);
    fscanf(fp, "%[^\"]\"", arti);

    printf("\n%s", arti);

    fclose(fp);
}

int hash(char kata[30]) {
    return kata[0] - 97;
}

node* newNode(char kata[30], long startArti) {
    node* new = (node*)malloc(sizeof(node));
    strcpy(new->kata, kata);
    new->startArti = startArti;
    new->left = new->right = NULL;

    return new;
}

void insert(char kata[30], long startArti, node** root) {
    if (*root == NULL)
        *root = newNode(kata, startArti);
    else
        _insert(kata, startArti, root);
}

void _insert(char kata[30], long startArti, node** parent) {
    node* temp = *parent;
    if (strcmp(kata, temp->kata) > 0) {
        if (temp->left == NULL) {
            temp->left = newNode(kata, startArti);
            return;
        }
        _insert(kata, startArti, &temp->left);
    } else {
        if (temp->right == NULL) {
            temp->right = newNode(kata, startArti);
            return;
        }
        _insert(kata, startArti, &temp->right);
    }
}

node* search(char kata[30]) {
    if (table[hash(kata)] != NULL) {
        return _search(table[hash(kata)], kata);
    }
    return NULL;
}

node* _search(node* now, char kata[30]) {
    if (strcmp(kata, now->kata) == 0) {
        return now;
    } else if (strcmp(kata, now->kata) < 0 && now->right != NULL) {
        return _search(now->right, kata);
    } else if (strcmp(kata, now->kata) > 0 && now->left != NULL) {
        return _search(now->left, kata);
    }
    return NULL;
}