#include "main.h"
/***
 * print_dlistint - A function to print elements of a doubly link list
 * @h : Head parameter received
 *
 * Return : Size_t signed integer data type
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t k;
	k = 0;
	/*struct dlistint_s *k = head; */
	new = malloc(sizeof(dlistint_t));
	if (new == NULL)
	{
		dprintf(2, "Error: Can't malloc\n");
		return (EXIT_FAILURE);
	}
	struct dlistint_s *p = h;
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
	free(new);
	return(k);
}
