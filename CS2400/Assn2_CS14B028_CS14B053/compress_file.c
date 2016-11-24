#include<stdio.h>
#include<math.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>
int current_bit = 0;
int ascii_value = 0;
char bit_buffer;

FILE *f;

void WriteBit (int bit,int flag)
{
	if(flag == 1)
	{
		bit_buffer = ascii_value;
  		//printf("%d\n",ascii_value);
    	fprintf(f,"%c",bit_buffer);
    	current_bit = 0;
    	bit_buffer = 0;
    	ascii_value = 0;
    	return;
	}
 ascii_value = 2*ascii_value + bit;

  current_bit++;
  if (current_bit == 7)
  {
  	bit_buffer = ascii_value;
  	//printf("%d\n",ascii_value);
    fprintf(f,"%c",bit_buffer);
    current_bit = 0;
    bit_buffer = 0;
    ascii_value = 0;
  }
}
int main(int argc,char *argv[])
{
	FILE *codes,*text;
	if(argc != 2)
	{
		printf("Enter the command line arguments in the following format: ./compress <Text file>\n");
		exit(-1);
	}
	text = fopen(argv[1],"r");
	codes = fopen("code_book.txt","r");
	f = fopen("compressed.txt","w");
	char ch,a[100];
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
			if(a[i]=='0')WriteBit(0,0);
			else WriteBit(1,0);
		}
	}
	WriteBit(0,1);
	fclose(text);
	fclose(f);
	fclose(codes);
}
