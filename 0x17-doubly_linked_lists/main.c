#include "main.h"
/***
 *
 *
 */

int printList(){
	size_t k;
	k = 0;
	struct dlistint_s *p = head;
	printf("\n[");

	/*start from the beginning*/
	while(p != NULL) {
		k++;
		printf(" %d",p->n);
		p = p->next;
		if (p != NULL)
			printf(",");
	}
	printf("]");
return(k);
}
void insertatbegin(int data){
	//create a link
	struct dlistint_s *lk = (struct dlistint_s*) malloc(sizeof(struct dlistint_s));
	lk->n = data;

	// point it to old first node
	lk->next = head;

	//point first to new first node
	head = lk;
//	return(lk);
}
void main()
{
	size_t k = 0;
	//size_t k;
	insertatbegin(12);
	insertatbegin(22);
	// print list
	k = printList();
	struct dlistint_s *current = head;
	while (current != NULL) 
	{
		struct dlistint_s *temp = current;
		//printf("hi: %d",current->n);
		current = current->next;
		//printf("hi: %d",current->data);
		free(temp);
	}
	printf("-> %lu elements\n", k);
}
