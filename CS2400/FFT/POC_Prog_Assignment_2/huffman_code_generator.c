#include<stdio.h>
#include<math.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>

struct BinaryNode
{
	float prob;
	int ascii_value;
	struct BinaryNode *parent,*left,*right;
	struct BinaryNode *next;
	char *code;
};

struct BinaryNode *head=NULL;
void inorder_traversal(struct BinaryNode *root,char *code,FILE *file)
{
	char temp[100],temp2[100];
	int n;
	static double entropy = 0.0,avg_code=0.0;
	
	strcpy(temp,code);
	strcat(temp,"0");
	if(root->ascii_value != -1)
	{
		printf("%f\t%d\t%s\t",root->prob,root->ascii_value,code);
		n = strlen(code);
		entropy -= root->prob*log2(root->prob);
		avg_code += root->prob*n;
		printf ("%f\t%f\n",entropy,avg_code);
		fprintf(file,"%d\t%s\n",root->ascii_value,code);
	}

	if(root->left != NULL)
	{
		inorder_traversal(root->left,temp,file);
	}
	strcpy(temp,code);	
	strcat(temp,"1");
	if(root->right != NULL)
	{
		inorder_traversal(root->right,temp,file);
	}
}

int main()
{
	FILE *fp,*code_book_file;
	
	struct BinaryNode *point,*first,*second,*new_node,*insert;
	int size= 0;
	float prob;
	int ascii; 
	fp = fopen("probs_sorted.txt","r");
	while(!(feof(fp)))
	{
		fscanf(fp,"%f%d",&prob,&ascii);
		if(head == NULL)
		{
			head = (struct BinaryNode *)malloc(sizeof(struct BinaryNode));
			head->prob = prob;
			head->ascii_value = ascii;
			head->parent  = NULL;
			head->left = NULL;
			head->right = NULL;
			head->next = NULL;
		}
		else
		{
			point = (struct BinaryNode *)malloc(sizeof(struct BinaryNode));
			point->prob = prob;
			point->ascii_value = ascii;
			point->parent  = NULL;
			point->left = NULL;
			point->right = NULL;
			point->next = head;
			head = point;
		}
	}
	head = head->next;
	point = head;
	prob = 0.0;
	while (point != NULL)
	{
		printf("%f\t%d\n",point->prob,point->ascii_value);
		prob += point->prob;
		point = point->next;
	}
	while(head->next->next != NULL)
	{
		point = head;
		while(point->next->next->next != NULL)
		{
			point = point->next;
		}
		second = point->next->next;
		point->next->next = NULL;
		first = point->next;
		point->next = NULL;
		new_node = (struct BinaryNode *)malloc(sizeof(struct BinaryNode));
		new_node->prob = first->prob +second->prob;
		new_node->ascii_value = -1;
		new_node->parent = NULL;
		new_node->left = first;
		new_node->right = second;
		new_node->next = NULL;
		first->parent = new_node;
		second->parent = new_node;
		prob = new_node->prob;
		point = head;
		while(point->next !=NULL && point->next->prob > prob)
		{
			point = point->next;
		}
		if(point -> next == NULL)
		{
			point->next = new_node;
		}
		else
		{
			insert = point->next;
			point->next = new_node;
			new_node->next = insert;
		}
	}
	
	second = head->next;
	head->next = NULL;
	first = head;
	head = (struct BinaryNode *)malloc(sizeof(struct BinaryNode));
	head->prob = first->prob +second->prob;
	head->ascii_value = -1;
	head->parent = NULL;
	head->left = first;
	head->right = second;
	head->next = NULL;
	first->parent = head;
	second->parent = head;
	printf("Inorder_trav ersal\n");
	code_book_file = fopen("code_book.txt","w");
	inorder_traversal(head,"\0",code_book_file);
	fclose(code_book_file);
	return 0;
}
