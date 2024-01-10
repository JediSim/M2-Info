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

// Si on note i2i la composition de i2c, H et h2i, les chaines sont de la forme 
// Programmez la fonction (à deux arguments) i2i, puis la fonction nouvelle_chaine(idx1, largeur) qui génère une chaine de taille largeur. 
int i2i(int integer, int t)
{   
    char txt[taille+1];
    txt[taille] = '\0';
    i2c(integer, txt);
    byte empreinte[SHA_DIGEST_LENGTH] = {0};
    hash_SHA1(txt, empreinte);
    return h2i(empreinte, t);
}

char* nouvelle_chaine(int idx1, int largeur)
{
    char* txt = malloc(largeur * sizeof(char));
    txt[largeur] = '\0';
    int idx2 = i2i(idx1, 0);
    for(int i = 0; i < largeur; i++)
    {
        txt[i] = alphabet[idx2];
        idx2 = i2i(idx2, i+1);
    }
    return txt;
}

int calcule_N(int taille, char* alphabet)
{
    return pow(lenAlphabet,taille);
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
        for(int i = 0; i < 10; i++)
        {
            printf("i2i(%d) = %d\n", i, i2i(i, 1));
        }
    }
    else {
        help();
        return 1;
    }
   
    printf("\n");
    return 0;
}

