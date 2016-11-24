#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* crcRem(char* bitString, char* gPoly, int bsl, int gpl);
char* crcGen(char* bitString, char* gPoly);
char* crcCheck(char* codedString, char* gPoly);
char xor(char a, char b);


int main(int argc, char** argv)
{
    if(argc != 3)
    {
        printf("Usage: ./crc msgString GeneratingPolynomial\n");
        exit(-1);
    }
    
    char* decodedString;
    
    printf("rem: %s\n", crcRem(argv[1], argv[2], strlen(argv[1]), strlen(argv[2])));
    printf("gen: %s\n", crcGen(argv[1], argv[2]));
    printf("check: %s\n", (decodedString=crcCheck(crcGen(argv[1], argv[2]), argv[2]))==NULL?"False":decodedString);
    
}


char* crcRem(char* bitString, char* gPoly, int bsl, int gpl)
{
    int i, j; // counter
    
    char* dividend = (char*) malloc(sizeof(char) * (bsl + gpl - 1 + 1));
    char* rem = (char*) malloc(sizeof(char) * (gpl-1+1));
    
    strcpy(dividend, bitString);
    
    for(i=bsl; i<bsl+gpl-1; i++)
    {
        dividend[i] = '0';
    }
    
    dividend[i] = '\0';
    
    for(i=0;; i++)
    {
        while(dividend[i] != '1' && i<bsl)
        {
            i++;
        }
        
        if (i == bsl)
        {
            break;
        }
        
        for(j=0; j<gpl; j++)
        {
            dividend[i+j] = xor(dividend[i+j], gPoly[j]);
        }
        
        printf("rem: dividend = %s\n", dividend);
    }
    
    for(i=bsl; i<bsl+gpl-1; i++)
    {
        rem[i-bsl] = dividend[i];
    }
    
    rem[gpl-1] = '\0';
    
    return rem;

}

char* crcGen(char* bitString, char* gPoly)
{
    int bsl = strlen(bitString);
    int gpl = strlen(gPoly);
    
    char* rem = crcRem(bitString, gPoly, bsl, gpl);
    char* new = (char*) malloc(sizeof(char) * (bsl+gpl-1+1));
    
    strcpy(new, bitString);
    strcat(new, rem);
    
    return new;
}

char* crcCheck(char* codedString, char* gPoly)
{
    int i, j;
    int gpl = strlen(gPoly);
    int bsl = strlen(codedString) - gpl + 1;
    char* decodedString = (char*) malloc(sizeof(char) * (bsl+1));
    strncpy(decodedString, codedString, bsl);
    decodedString[bsl] = '\0';
    
    for(i=0; i<bsl; i++)
    {
        while(codedString[i] != '1' && i<bsl)
        {
            i++;
        }
        
        if(i == bsl)
        {
            break;
        }
        
        for(j=0; j<gpl; j++)
        {
            codedString[i+j] = xor(codedString[i+j], gPoly[j]);
        }
    }
    
    while(codedString[i] == '0' && i<gpl+bsl-1) i++;
    
    if (i == gpl+bsl-1)
    {
        return decodedString;
    }
    
    return NULL;
}

char xor(char a, char b)
{
    if(a == '1')
    {
        if(b == '1') return '0';
        
        return '1';
    }
    else
    {
        if(b == '1') return '1';
        return '0';
    }
}
