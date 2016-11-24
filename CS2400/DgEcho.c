#include <stdio.h>
#include<sys/types.h>
#include<sys/socket.h>
#include "string.h"
#include "stdlib.h"
#include "crc.c"
#define  MAXMESG 2048
#include "files.h"


/*-------------------------------------------------------------------------
 *  DgEcho -- Reads a packet from client and sends it back to client
 *------------------------------------------------------------------------*/
void DgEcho(int sockFd, struct sockaddr *pcliAddr, socklen_t  maxCliLen)
{
    int n;
    socklen_t cliLen;
    char mesg[MAXMESG];
    char* packet;
    FILE* outfile;
    
    outfile = fopen(RECEIVED_FILE, "w");
    
    printf("entered dgecho\n");
    
    while(1)
    {
        cliLen = maxCliLen;
        
        //receive a message from a socket
        n = recvfrom(sockFd, mesg, MAXMESG, 0, pcliAddr, &cliLen);
        printf("received string of size %d string is:%s\n",n, mesg);
        
        if (n < 0) 
        {
            printf("dg_echo : recvfrom error");
            // err_dump("dg_echo : recvfrom error");*/
            exit(-1);
        }
        
        // end of transmission
        if(mesg[0] == 'E')
        {
            fclose(outfile);
            break;
        }
        
        if((packet = crcCheck(mesg, GPOLY)) != NULL)
        {
            fprintf(outfile, "%s", packet);
            mesg[0] = '1'
            mesg[1] = '\0'
        }
        else
        {
            mesg[0] = '0'
            mesg[1] = '\0'
        }
        
        n = 2;
        
        if (sendto(sockFd, mesg, n, 0, pcliAddr, cliLen) != n) 
        {
           printf("dg_echo : sendto  error\n");
           exit(-1);
        }
        
        printf("Message sent back to Client:%s\n", mesg); 
    }
}

