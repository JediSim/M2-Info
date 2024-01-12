#include "stdio.h"
#include <stdlib.h>
#include <math.h>
#include "string.h"

#include <openssl/sha.h>

typedef unsigned char byte;         // facultatif

// global variables
char* alphabet;
int lenAlphabet;
int taille;
int N;

//table infos
int largeur = 0;
int hauteur = 0;

void hash_SHA1(const char* s, byte* empreinte)
{
    SHA1((unsigned char*)s, strlen(s), empreinte);
}

void help()
{
    printf("usage: rbt\n");
    printf("  --hash  <string> : string to hash\n");
    printf("  --help   : show this help\n");
    printf("  --calculeN : calcule N (besoin d'avoir renseigné l'alphabet et la taille)\n");
    printf("  --i2c <int> : transforme un entier en texte clair (besoin d'avoir renseigné l'alphabet et la taille)\n");
    printf("  --h2i <string> <int> : transforme un hash en entier (besoin d'avoir renseigné l'alphabet et la taille)\n");
    printf("  --i2i <int> : transforme un entier en entier (besoin d'avoir renseigné l'alphabet et la taille)\n");
    printf("  --creer_table <int> <int> : creer une table avec width height (besoin d'avoir renseigné l'alphabet et la taille)\n");
    printf("=====================================================\n");
    printf("ces options doivent être rensaignées après les autres options\n");
    printf("  --alphabet <string> : alphabet\n");
    printf("  --taille <int> : taille\n");
    printf("  --N <int> : N\n");
    printf(" --test : affiche la config\n");
}

void AfficheConfig()
{
    printf("alphabet = %s\n", alphabet);
    printf("taille = %d\n", taille);
    printf("N = %d\n", N);
}

int calcule_N(int taille, char* alphabet)
{
    return pow(lenAlphabet,taille);
}

void i2c(int integer, char* txt){
    for(int i = 0; i < taille; i++)
    {
        txt[taille-1-i] = alphabet[integer % lenAlphabet];
        integer = integer / lenAlphabet;
    }
}

int h2i(byte* s, int t)
{
    // get the first 8 bytes of the hash
    byte first8Bytes[8];
    for(int i = 0; i < 8; i++)
    {
        first8Bytes[i] = s[i];
    }

    uint64_t* value = (uint64_t*)first8Bytes;
    return (*value + t) % N;
}


int i2i(int integer, int t)
{   
    char txt[taille+1];
    txt[taille] = '\0';
    i2c(integer, txt);
    byte empreinte[SHA_DIGEST_LENGTH] = {0};
    hash_SHA1(txt, empreinte);
    int number = h2i(empreinte, t);
    return number;
}

int nouvelle_chaine(int idx1, int largeur)
{
    int idx2 =  idx1;
    for(int i = 1; i < largeur; i++)
    {
        idx2 = i2i(idx2, i);
        // printf("%d %d \n",i, idx2);
    }    
    return idx2;
}

int index_aleatoire()
{
    // create a random number between 0 and N in int 64 bytes
    uint64_t random = rand();
    random = random << 32;
    random = random | rand();
    random = random % N;
    return random;
}

int cmpfunc (const void * a, const void * b) {
    // Cast the pointers to the correct type
    int* rowA = *(int**)a;
    int* rowB = *(int**)b;

    // Compare the second column of the array of int
    return rowA[1] - rowB[1];
}

void creer_table(int l, int h,int** table)
{
    //    int table[largeur][2];
    for(int i = 0; i < h; i++)
    {
        table[i][0] = index_aleatoire();
        table[i][1] = nouvelle_chaine(table[i][0], l);
        // table[i][0] = i;
        // table[i][1] = nouvelle_chaine(i, largeur);
    }
    // Attention, la table finale doit être triée par ordre croissant de la dernière colonne. 
    qsort(table, h, sizeof(int*), cmpfunc);
}

void save_table(char* filepath)
{
    FILE *f = fopen(filepath, "w");
    if (f == NULL)
    {
        printf("Error opening file!\n");
        exit(1);
    }
    int** table = malloc(hauteur * sizeof(int*));
    for(int i = 0; i < hauteur; i++)
    {
        table[i] = malloc(2 * sizeof(int));
    }
    creer_table(largeur, hauteur, table);
    //save params
    fprintf(f, "%s %d\n", alphabet, taille);
    fprintf(f, "%d %d\n", largeur, hauteur);
    //save table
    for(int i = 0; i < hauteur; i++)
    {
        fprintf(f, "%d %d\n", table[i][0], table[i][1]);
    }
    fclose(f);
}

int** load_table(char* filepath)
{
    FILE *f = fopen(filepath, "r");
    if (f == NULL)
    {
        printf("Error opening file!\n");
        exit(1);
    }
    //load params
    alphabet = malloc(100 * sizeof(char));
    fscanf(f, "%s %d", alphabet, &taille);
    lenAlphabet = strlen(alphabet);
    N = calcule_N(taille, alphabet);
    fscanf(f, "%d %d", &largeur, &hauteur);
    //load table
    int** table = malloc(hauteur * sizeof(int*));
    for(int i = 0; i < hauteur; i++)
    {
        table[i] = malloc(2 * sizeof(int));
    }
    for(int i = 0; i < hauteur; i++)
    {
        fscanf(f, "%d %d", &table[i][0], &table[i][1]);
    }
    fclose(f);
    return table;
}

int recherche(int** table, int hauteur, int idx, int* a, int* b) {
    int i = 0;
    int j = hauteur - 1;
    printf("search start %d \n",idx);
    while (i <= j) {
        int m = (i + j) / 2;
        if (table[m][1] == idx) {
            printf("if 1\n");
            *a = m;
            *b = m;
            while (*a > 0 && table[*a - 1][1] == idx) {
                (*a)--;
            }
            printf("while 1 ok\n");
            while (*b < hauteur - 1 && table[*b + 1][1] == idx) {
                (*b)++;
            }
            printf("search done ok\n");
            return *b - *a + 1;
        } else if (table[m][1] < idx) {
            printf("if 2\n");
            i = m + 1;
        } else {
            printf("if 3\n");
            j = m - 1;
        }
    }
    printf("search done ko\n");
    return 0;
}

int verif_hash(byte* h, byte* h2) {
    for (int i = 0; i < SHA_DIGEST_LENGTH; i++) {
        if (h[i] != h2[i]) {
            printf("i= %dh[i] = %d h2[i] = %d\n",i, h[i], h2[i]);
            return 0;
        }
    }
    return 1;
}

int verifie_candidat(byte* h, int t, int idx, byte* clair) {
    for (int i = 1; i < t; i++) {
        idx = i2i(idx, i);
    }
    i2c(idx, clair);
    printf("idx = %d clair = %s\n", idx,clair);
    byte empreinte[SHA_DIGEST_LENGTH] = {0};
    hash_SHA1(clair, empreinte);
    printf("empreinte =");
    for (int i = 0; i < SHA_DIGEST_LENGTH; i++) {
            printf("%02x", empreinte[i]);
        }
        printf("\n");
    printf("verif %d\n",verif_hash(empreinte, h));
    return verif_hash(empreinte, h);
}

int inverse(int** table, byte* h, byte* clair) {
    printf("let's crack it\n");
    for (int t = largeur - 1; t > 0; t--) {
        int idx = h2i(h, t);
        // printf("idx = %d\n", idx);
        for (int i = t + 1; i < largeur; i++) {
            idx = i2i(idx, i);
        }
        int a, b;
        // printf("before recherche\n");
        if (recherche(table, hauteur, idx, &a, &b) > 0) {
            printf("found candidats between a %d and b %d\n",a,b);
            for (int i = a; i <= b; i++) {
                printf("verif candidat i %d\n",i);
                if (verifie_candidat(h, t, table[i][0], clair) == 1) {
                    printf("found a candidate %s %s\n",h, clair);
                    return 1;
                }
            }
        }
    }
    printf("found nothing, I'm stupid");
    return 0;
}

float couverture()
{
    float m = hauteur;
    float v = 1.0;
    for (int i = 0; i < largeur; i++) {
        v = v * (1 - m / N);
        m = (float)N * (1 - exp(-m / N));
    }
    return 100 * (1-v);
}


int main(int argc, char* argv[])
{   

    int test = 0;

    if (argc == 1) {
        help();
        return 1;
    }
    //loop through arguments to find the ones specified
    for(int i = 0; i < argc; i++)
    {
        if(strcmp(argv[i], "--alphabet") == 0)
        {
            alphabet = argv[i + 1];
            lenAlphabet = strlen(alphabet);
        }
        else if(strcmp(argv[i], "--taille") == 0)
        {
            taille = atoi(argv[i + 1]);
        }
        else if(strcmp(argv[i], "--test") == 0)
        {
            test = 1;
        }
    }

    //calculate N
    N = calcule_N(taille, alphabet);

    if(test)
    {
        AfficheConfig();
    }

    if (strcmp(argv[1], "--hash") == 0) {
        byte empreinte[SHA_DIGEST_LENGTH] = {0};
        hash_SHA1(argv[2], empreinte);
        printf("empreinte = ");
        for (int i = 0; i < SHA_DIGEST_LENGTH; i++) {
            printf("%02x", empreinte[i]);
        }
    } else if (strcmp(argv[1], "--help") == 0) {
        help();
        return 0;
    }else if (strcmp(argv[1], "--calculeN") == 0) {
        N = calcule_N(taille, alphabet);
        printf("N = %d\n", N);
        return 0;
    } else if (strcmp(argv[1], "--i2c") == 0) {
        char txt[taille+1];
        txt[taille] = '\0';
        i2c(atoi(argv[2]), txt);
        printf("\n");
        printf("final : %s \n", txt);
        return 0;
    } else if (strcmp(argv[1], "--h2i") == 0) {
        printf("argv[2] = %s\n", argv[2]);
        int res_h2i;
        byte empreinte[SHA_DIGEST_LENGTH] = {0};
        hash_SHA1(argv[2], empreinte);
        printf("empreinte = ");
        for (int i = 0; i < SHA_DIGEST_LENGTH; i++) {
            printf("%02x", empreinte[i]);
        }
        printf("\n");
        res_h2i = h2i(empreinte, atoi(argv[3]));
        printf("h2i = %i\n", res_h2i);
        return 0;
    }
    else if(strcmp(argv[1],"--i2i") == 0 ){
        int taille = atoi(argv[2]);
        nouvelle_chaine(1, taille);
        return 0;
        
    }
    else if(strcmp(argv[1],"--creer_table") == 0 ){
        largeur = atoi(argv[2]);
        hauteur = atoi(argv[3]);
        int** table = malloc(hauteur * sizeof(int*));
        for(int i = 0; i < hauteur; i++)
        {
            table[i] = malloc(2 * sizeof(int));
        }
        creer_table(largeur, hauteur, table);
        for(int i = 0; i < hauteur; i++)
        {
            printf("%d %d %d \n",i, table[i][0], table[i][1]);
        }
        return 0;
    }
    else if(strcmp(argv[1],"--create") == 0 ){
        char * path = argv[4];
        largeur = atoi(argv[2]);
        hauteur = atoi(argv[3]);
        save_table(path);
        printf("table saved\n");
        return 0;
    }
    else if(strcmp(argv[1],"--info") == 0 ){
        int** table = load_table(argv[2]);
        printf("table loaded\n");
        for(int i = 0; i < hauteur; i++)
        {
            printf("%d %d %d \n",i, table[i][0], table[i][1]);
        }
        return 0;
    }
    else if(strcmp(argv[1],"--crack") ==0){
        int** table = load_table(argv[3]);
        printf("table loaded\n");
        if(test)
        {
            AfficheConfig();
        }
        char* toCrack = argv[2];
        printf("to crack = %s\n", toCrack);
        byte clair[taille+1];
        clair[taille] = '\0';
        if(inverse(table, toCrack, clair)){
            printf("clair = %s\n", clair);
        }
        return 0;
    }
    else if(strcmp(argv[1],"--couverture") ==0){
        largeur = atoi(argv[2]);
        hauteur = atoi(argv[3]);
        printf("couverture = %f\n", couverture());
        return 0;
    }
    else {
        help();
        return 1;
    }
   
    printf("\n");
    return 0;
}

