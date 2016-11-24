#include<stdio.h>
#include<math.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>
#include<time.h>


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

	return generated_string;
}
//$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$//


//############################# - Check if correct string - ############################//
char* CRC_check(char* generated_string,char* gPoly)
{
	int gPoly_len=strlen(gPoly);
	int input_str_len=strlen(generated_string)-gPoly_len+1;
	int i,j;
	char temp[strlen(generated_string)+1];
	strcpy(temp,generated_string);
	char* decoded_string=(char*) malloc(sizeof(char)*(input_str_len+1));
	strncpy(decoded_string,generated_string,input_str_len);
	decoded_string[input_str_len]='\0';

	for(i=0;i<input_str_len;i++)
	{
		printf("i--%d\n",i);
		if(temp[i]=='0')
			continue;
		//printf("%d\n",i);
		for(j=0;j<gPoly_len;j++)
			temp[i+j]=XOR(temp[i+j],gPoly[j]);
		//puts(temp);
	}

	for(i=0;i<strlen(generated_string);i++)
		if(temp[i]=='1')
			return NULL;			// Error - Request for re-transmission
	return decoded_string;				// Correct
}
//#####################################################################################//

int main(int argc, char** argv)
{
    if(argc != 2)
    {
        printf("Usage: ./channel bitString p\n");
        exit(-1);
    }
    
    float errorProb = 0.4;
    
   // char BitString[strlen(argv[1]) + 1];
   
    
    printf("Bit string with error: %s - %s\n",argv[1],  generate_error(errorProb,argv[1]));
	//printf("%s\n",CRC_Rem(convert_to_packet('A'),"1011"));
	printf("%s\n",CRC_generate(convert_to_packet('A'),"1011"));
	char* temp=CRC_generate(convert_to_packet('A'),"1011");
	
	if(CRC_check(generate_error(errorProb,temp),"1011")==NULL)
		printf("Didn't work\n");
	else printf("s\n");
	printf("%s\n",convert_to_packet('A'));
}

