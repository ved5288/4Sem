#include<stdio.h>
#include<math.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>

struct BinaryTree
{
	int prob;
	int left_value;
	int right_value;
	struct BinaryTree *left_node,*right_node;
};
struct character
{
	float prob;
	int ascii_value;
};
int cmpfunc (const void * a, const void * b)
{
    const struct character **lhs = (const struct character **)a;
    const struct character **rhs = (const struct character **)b;
    return (*lhs)->prob < (*rhs)->prob ? -1
        : ((*rhs)->prob < (*lhs)->prob ? 1 : 0);
}


int main(int argc, char *argv[])
{
	struct BinaryTree *root;
	struct character c[150],new;
	char ch;
	long int val,a[150],i,j;
	int size = sizeof(c)/sizeof(c[0]);
	float prob=0.0,counter = 0.0,t;
	FILE *fp;
	if(argc != 2)
	{
		printf("Enter the command line arguments in the following format: ./huffman <Text file>\n");
		exit(-1);
	}
	for(i=0;i<150;i++)
	{
		a[i] = 0;
		c[i].ascii_value = i;
	}
	fp = fopen(argv[1],"r");
	if(fp == NULL)
	{
		printf("Error in opening the file\n");
		exit(-1);
	}
	while(!feof(fp))
	{
		fscanf(fp,"%c",&ch);
		val = toascii(ch);
		a[val]++;
		counter += 1.0;
	}
	fclose(fp);
	fp = fopen("probs.txt","w");
	for(i=0;i<150;i++)
	{
		c[i].prob = a[i]/counter;
		prob += c[i].prob;
		fprintf(fp,"%f\n",c[i].prob);
	}
	fclose(fp);
	for (i = 1 ; i < 150; i++) 
	{
		j = i;
	 
		while ( j > 0 && c[j].prob < c[j-1].prob) 
		{
		  new.prob = c[j].prob;
		  new.ascii_value = c[j].ascii_value;
		  c[j].prob = c[j-1].prob;
		  c[j].ascii_value =  c[j-1].ascii_value;
		  c[j-1].prob = new.prob;
		  c[j-1].ascii_value = new.ascii_value;
	 
		  j--;
		}
  	}
	fp = fopen("probs_sorted.txt","w");
	for(i=0;i<150;i++)
	{
		if(c[i].prob > 0)fprintf(fp,"%lf\t%d\n",c[i].prob,c[i].ascii_value);
	}
	fclose(fp);
	return 0;
}
