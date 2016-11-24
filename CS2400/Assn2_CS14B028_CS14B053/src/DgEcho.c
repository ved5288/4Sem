/*-------------------------------------------------------------------------
 *  DgEcho.c - Reads a string from Client and writes it back to Client
 *  Version:	$Name:  $
 *  Module:	
 *
 *  Purpose:	
 *  See:	
 *
 *  Author:	Hema Murthy (hema@bhairavi.iitm.ernet.in)
 *
 *  Created:        Sat 17-Mar-2007 10:58:43
 *  Last modified:  Sat 17-Mar-2007 14:12:40 by hema
 *  $Id: DgEcho.c,v 1.1 2007/03/26 04:26:09 hema Exp hema $
 *
 *  Bugs:	
 *
 *  Change Log:	<Date> <Author>
 *  		<Changes>
 -------------------------------------------------------------------------*/

 
#include <stdio.h>
#include<sys/types.h>
#include<sys/socket.h>
#include "string.h"
#include "stdlib.h"

#define  MAXMESG 2048


/*-------------------------------------------------------------------------
 *  DgEcho -- Reads a packet from client and sends it back to client
 *    Args:	
 *    Returns:	Nothing
 *    Throws:	
 *    See:	UNIX Network Programming - Richard Stevens: Vol I
 *    Bugs:	
 -------------------------------------------------------------------------*/
 char XOR(char a,char b)
{
	if(a==b)
		return '0';
	return '1';
}

 
 //############################# - Check if correct string - ############################//
char* CRC_check(char* generated_string,char* gPoly)
{
	int gPoly_len=strlen(gPoly);
	int input_str_len=strlen(generated_string)-gPoly_len;
	int i,j;
	char temp[strlen(generated_string)+1];
	strcpy(temp,generated_string);
	char* decoded_string=(char*) malloc(sizeof(char)*(input_str_len+1));
	//char *string = (char*)malloc(sizeof(char)*(strlen(decoded_string)-gPoly_len+2));
	strncpy(decoded_string,generated_string,input_str_len);
	decoded_string[input_str_len]='\0';
	for(i=0;i<input_str_len;i++)
	{
		//printf("i--%d\n",i);
		if(temp[i]=='0')
			continue;
		//printf("%d\n",i);
		for(j=0;j<gPoly_len;j++)
			temp[i+j]=XOR(temp[i+j],gPoly[j]);
		//puts(temp);
	}
	//puts(generated_string);
	//puts(gPoly);
	//puts(decoded_string);
	for(i=0;i<strlen(generated_string);i++)
		if(temp[i]=='1')
			return NULL;// Error - Request for re-transmission
	
	
	
	return decoded_string;				// Correct
}
//#####################################################################################//

void DgEcho(int sockFd, struct sockaddr *pcliAddr, socklen_t  maxCliLen,char *gPoly)
  {
    int       n;
    socklen_t cliLen;
  	char mesg[MAXMESG];
  	printf("entered dgecho\n");
  	FILE *write;
  	write = fopen("received_data.txt","w");
  	//printf("opened\n");
  	fclose(write);
  	for  ( ; ;)
	  {
  		cliLen = maxCliLen;
  		n = recvfrom(sockFd, mesg, MAXMESG, 0, pcliAddr, &cliLen);
		printf("received string of size %d string is:%s\n",n, mesg);
  		if (n < 0) {
		   printf("dg_echo : recvfrom error");
  		      // err_dump("dg_echo : recvfrom error");*/
  		   exit(-1);
		}	
		char * check;
		int value,m,i;
		check = CRC_check(mesg,gPoly);
		
		if(check !=NULL)
		{
			mesg[0]='1';
			mesg[1]='\0';
			printf("Message sent back to Client:Transmit next packet(%s)\n", mesg); 
			printf("Received string after CRC check is %s\n",check);
			//puts(check);
			m = strlen(check);
			value = 0;
			for(i=0;i<m;i++)
			{
				if(check[i]=='1')
				{
					value = 2*value +1;
				}
				else
				{
					value = 2*value;
				}
			}
			//ch_print = (char)value;
			write = fopen("received_data.txt","a");
			fprintf(write,"%c",value);
			fclose(write);
			//fprintf
			//return 1;
		}
		else{
		mesg[0]='0';
		mesg[1]='\0';
		printf("Message sent back to Client:Retransmit(%s)\n", mesg); 
		}
		if (sendto (sockFd, mesg, n, 0, pcliAddr, cliLen) != n) {
		   printf("dg_echo : sendto  error\n");
                   exit(-1);
		}
		
		//return 0;
	  }
	  
	 
	  
	  
    }	/*  End of DgEcho		End of DgEcho   */

	




/*-------------------------------------------------------------------------
 * $Log: DgEcho.c,v $
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
 *                        End of DgEcho.c
 -------------------------------------------------------------------------*/
