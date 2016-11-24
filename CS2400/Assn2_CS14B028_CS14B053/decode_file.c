#include<stdio.h>
#include<math.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>

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

void main(int argc, char *argv[])
{
	FILE* fp,*new,*answer	;
	char a;
	int b,n,current_number,i,j;
	char s[150];
	if(argc != 3)
	{
		printf("Enter the command line arguments in the following format: ./decode <Encoded File> <Decode file name>\n");
		exit(-1);
	}
	fp=fopen(argv[1],"r");
	new=fopen("new_file.txt","w");
	while(!feof(fp))
	{
		fscanf(fp,"%c",&a);
		fprintf(new,"%s",convert_to_packet(a));
	}
	fclose(fp);
	fclose(new);
	new=fopen("new_file.txt","r");
	fp=fopen("code_book.txt","r");
	answer=fopen(argv[2],"w");
	n=0;
	while(!feof(fp))
	{
		fscanf(fp,"%d\t%s\n",&b,s);
		if(strlen(s)>n)
			n=strlen(s);
	}
	fseek(fp,0,SEEK_SET);
	char map[n+1];
	char temp[n+1];

	current_number=0;

	while(!feof(new))
	{
	
	for(i=0;i<n-current_number&&!feof(new);i++)
	{
		fscanf(new,"%c",&map[current_number+i]);
	}
	map[n]='\0';
	//puts(map);
	for(i=1;i<=n;i++)
	{
		strncpy(temp,map,i);
		temp[i]='\0';
		//puts(temp);
		fseek(fp,0,SEEK_SET);
		while(!feof(fp))
		{
			fscanf(fp,"%d\t%s\n",&b,s);
			//printf("%s - %s - %d\n",s,temp,strcmp(temp,s));
			if(strcmp(temp,s)<=0)
				break;
		}
		if(strcmp(temp,s)==0)
			break;
	}
	fprintf(answer,"%c",b);
	current_number=n-i;
	//printf("%d\n",current_number);
	for(j=0;j<current_number;j++)
	{
		map[j]=map[i+j];
	}
	}
	fclose(new);
	fclose(fp);
	fclose(answer);
}
