/*-------------------------------------------------------------------------
 *  Client.c - Client Program for sending messages to the server
 *  Version:	$Name:  $
 *  Module:	
 *
 *  Purpose:	
 *  See:	
 *
 *  Author:	Hema Murthy (hema@bhairavi.iitm.ernet.in)
 *
 *  Created:        Sat 17-Mar-2007 14:09:41
 *  Last modified:  Mon 26-Mar-2007 09:54:20 by hema
 *  $Id: Client.c,v 1.1 2007/03/26 04:26:09 hema Exp hema $
 *
 *  Bugs:	
 *
 *  Change Log:	<Date> <Author>
 *  		<Changes>
 -------------------------------------------------------------------------*/

/* 
 * Example of client using UDP protocol.
 */

#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"
#include "strings.h"
#include "string.h"
#include "include/DgFunctions.h"
#include <time.h>
/*-------------------------------------------------------------------------
 *  Usage -- Prints the usage for the program
 *    Args:	
 *    Returns:	Nothing
 *    Throws:	
 *    See:	
 *    Bugs:	
 -------------------------------------------------------------------------*/
 
 //@@@@@@ Divide into packets @@@@@@@@@@//
char* convert_to_packet(char c)
{
	int n=c;
	char* binary=(char*)malloc(sizeof(char)*8);
	binary[7]='\0';
	int i=6;
	do
	{
	binary[i]=n%2+'0';
	n=n/2;
	i--;
	}
	while(i>=0);
	return binary;
}
//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@//
// ----------------------------Generate Error ---------------------------------------------//
char* generate_error(float p,char* input_string)
{
	float s;
	
	int n=strlen(input_string),i;
	char* output_string=(char*)malloc(sizeof(char)*(n+1));
	//printf("%f-%d\n",p,n);	
	srand(time(NULL));	
	for(i=0;i<n;i++)
	{
		s=(float)rand()/(float)(RAND_MAX);
		//printf("%f\n",s);
		if(s<p)
		{
			if(input_string[i]=='1')
				output_string[i]='0';
			else output_string[i]='1';
		}
		else
			output_string[i]=input_string[i];
		//printf("%c\n",
	}
	//printf("%d\n",i);
	output_string[i]='\0';
	return output_string;
}
//-----------------------------------------------------------------------------------------//

char XOR(char a,char b)
{
	if(a==b)
		return '0';
	return '1';
}

/***************************** - Compute Remainder - **************************************/
char* CRC_Rem(char* input_string,char* gPoly)
{
	int input_str_len=strlen(input_string);
	int gPoly_len=strlen(gPoly);
	int i,j;
	
	char* dividend=(char*)malloc(sizeof(char)*(input_str_len+gPoly_len));
	char* remainder=(char*)malloc(sizeof(char)*gPoly_len);	// remainder length will be strictly lesser than gPoly
	
	strcpy(dividend,input_string);
	for(i=0;i<gPoly_len-1;i++)
	{
		dividend[input_str_len+i]='0';
	}
	dividend[input_str_len+i]='\0';

	for(i=0;i<input_str_len;i++)
	{
		if(dividend[i]!='1')
			continue;
		for(j=0;j<gPoly_len;j++)
			dividend[i+j]=XOR(dividend[i+j],gPoly[j]);
		//printf("%s\n",dividend);
	}

	for(i=0;i<gPoly_len-1;i++)
		remainder[i]=dividend[input_str_len+i];
	remainder[i]='\0';

	return remainder;	
}
/*****************************************************************************************/

//$$$$$$$$$$$$$$$$$$$$$$$$$ - Generate the CRC string - $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$//
char* CRC_generate(char* input_string,char* gPoly)
{
	int input_str_len=strlen(input_string);
	int gPoly_len=strlen(gPoly);
	
	char* remainder=CRC_Rem(input_string,gPoly);
	char* generated_string=(char*)malloc(sizeof(char)*(input_str_len+gPoly_len));

	strcpy(generated_string,input_string);
	strcat(generated_string,remainder);
	//puts(input_string);
	//puts(generated_string);
	return generated_string;
}
//$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$//
void Usage () {
  printf ("Client ServerIPAddr ServerPort ClientIPAddress ClientPort CRC_Polynomial Error_Probability\n");
}


/*-------------------------------------------------------------------------
 *  main -- Main Program for the Client - sends 10 lines of text to server
 *    Args:	Takes as arguments ServerIP, ServerPort, ClientIP, ClientPort
 *    Returns:	Nothing
 *    Throws:	
 *    See:	Unix Network Programming: Richard Stevens - Vol I
 *    Bugs:	
 -------------------------------------------------------------------------*/
int  main (int argc, char **argv)
{
    int                   sockFd;
    int                   serverPortNumber, clientPortNumber;
    struct sockaddr_in    clientAddr,serverAddr;
    char                  *sendMsg = "Testing UDP Protocol\n";

    int                   i;
    char                  tempString[256];

    if (argc != 7) {
      Usage();
      exit(-1);
    }
    
     /* Fill in the structure "serverAddr " with the address of the 
     * server that we want to send to .
     */
    sscanf(argv[2],"%d", &serverPortNumber); 
    sscanf(argv[4],"%d", &clientPortNumber); 

    bzero(( char *) &serverAddr , sizeof (serverAddr));
    serverAddr.sin_family   = AF_INET;
    serverAddr.sin_addr.s_addr =inet_addr(argv[1]);
    serverAddr.sin_port  = htons(serverPortNumber);
  
  
    /* 
     * Open a UDP socket (an Internet datagram socket).
     */
     
    if (( sockFd = socket(AF_INET,SOCK_DGRAM ,0)) < 0) {
      printf("client : can't open datagram socket \n");
      exit(-1);
    }
    /* 
     * Bind any local address for us.
     */
    
      printf ("Socket bound\n");    

    
    bzero(( char *) &clientAddr , sizeof (clientAddr));
    clientAddr.sin_family   = AF_INET;
    clientAddr.sin_addr.s_addr =inet_addr(argv[3]);
    clientAddr.sin_port  = htons(clientPortNumber);
  
    if (bind (sockFd, (struct sockaddr *) &clientAddr ,sizeof(clientAddr)) < 0) {
      printf(" client: can't bind  local address\n");
    exit(-1);
    }
   
    /*for (i = 0; i < 10; i++) {
      tempString[0] = (char) (i+48);
      tempString[1] = ' ';
      tempString[2] = '\0';
      strcat(tempString, sendMsg);
      printf ("Message Sent = %s\n", sendMsg);
     DgClient(tempString, sockFd, (struct sockaddr *) &serverAddr, sizeof(serverAddr));
    }*/
    FILE *fp;
    char ch,*temp;
    int k;
    long int counter1 = 0,counter2 = 0;
    float prob;
    prob = atof(argv[6]);
    fp = fopen("/home/vedant/Downloads/Assn2_CS14B028_CS14B053/compressed.txt","r");
    if(fp == NULL) printf("Error in opening file\n");
    else{
    	while(!(feof(fp)))
    	{
    		fscanf(fp,"%c",&ch);
    		k=0;
    		counter1++;
    		while(k==0){
				temp = convert_to_packet(ch);
				temp = CRC_generate(temp,argv[5]);
				strcat(temp,"\n");
				counter2++;
				//puts(temp);
				temp = generate_error(prob,temp);
				k = DgClient(temp, sockFd, (struct sockaddr *) &serverAddr, sizeof(serverAddr));
    		}
    		
    	}
    	
    }
    printf("Error prob: %f\n",prob);
    printf("Number of packets: %ld\nNumber of transmissions: %ld\n",counter1,counter2);
    close(sockFd);
    exit(0);
    return(0);
}	/*  End of main		End of main   */
      


/*-------------------------------------------------------------------------
 * $Log: Client.c,v $
 * Revision 1.1  2007/03/26 04:26:09  hema
 * Initial revision
 *
 *
 * Local Variables:
 * time-stamp-active: t
 * time-stamp-line-limit: 20
 * time-stamp-start: "Last modified:[ 	]+"
 * time-stamp-format: "%3a %02d-%3b-%:y %02H:%02M:%02S by %u"
 * time-stamp-end: "$"
 * End:
 *                        End of Client.c
 -------------------------------------------------------------------------*/
