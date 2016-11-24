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

int current_bit = 0;
int ascii_value = 0;
char bit_buffer;

FILE *f;

void WriteBit (int bit)
{
 ascii_value = 2*ascii_value + bit;

  current_bit++;
  if (current_bit == 7)
  {
  	bit_buffer = ascii_value;
  	printf("%d\n",ascii_value);
    fprintf(f,"%c",bit_buffer);
    current_bit = 0;
    bit_buffer = 0;
    ascii_value = 0;
  }
}


int main()
{
	FILE *codes,*text;
	text = fopen("new_text.txt","r");
	codes = fopen("code_book.txt","r");
	f = fopen("compressed.txt","w");
	char ch,a[100];
	float p=0.25;					// error probablity
	int w,find,n,i;
	while(!(feof(text)))
	{
		fscanf(text,"%c",&ch);
		fseek(codes,0,SEEK_SET);
		w = toascii(ch);
		do
		{
			fscanf(codes,"%d%s",&find,a);
		}while(find!=w);
		n = strlen(a);
		for(i=0;i<n;i++)
		{
			if(a[i]=='0')WriteBit(0);
			else WriteBit(1);
		}
	}
	fclose(text);
	fseek(f,0,SEEK_SET);
	fclose(codes);
	while(!feof(f))
	{
		fscanf(f,"%c",&ch);
		char* packet = convert_to_packet(ch);
		char* encoded = CRC_generate(packet,"1011");
		char* error = generate_error(p,encoded);
	}
}
