#include<stdio.h>
#include<sys/types.h>
#include<sys/socket.h>
#include <string.h>
#include "stdlib.h"
#include "unistd.h"

#define MAXLINE 512


/*-------------------------------------------------------------------------
 *  DgClient -- Sends packets to server and receives packets from server
 *------------------------------------------------------------------------*/
int DgClient(char *sendMsg, int sockFd , struct sockaddr *servAddr , socklen_t servlen)
{
    int n;
    char recvMsg[MAXLINE];

    n = strlen(sendMsg);
    
    if(sendto(sockFd, sendMsg , n, 0 , servAddr , servlen) != n)
        printf("DgClient : sendto error on socket \n");

    printf ("Message Sent = %s\n", sendMsg);
    fflush(stdout);
    /*
    * Now read a message from the socket and write it to 
    * standard output.
    */
    n = recvfrom(sockFd, recvMsg, MAXLINE, 0, (struct sockaddr *) 0 , (socklen_t *) 0);

    if(n < 0)
    {
        printf("DgClient : recvfrom error \n");
        exit (-1) ;
    }
    
    // recvMsg contains the acknowledgement of whether the message was sent correctly. 
        
    recvMsg[1] = '\0';
    printf("Received Message %s\n", recvMsg);
    
    if(recvMsg[0] == '1')
        return 1; // received correctly.
    else
        return 0;
}
