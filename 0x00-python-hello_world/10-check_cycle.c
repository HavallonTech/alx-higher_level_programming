#include "lists.h"

/**
 * check_cycle - function in C that checks if a singly linked list has a cycle
 * @list: linked list to be checked
 *
 * Return: 1 if the list has a cycle, 0 if it does not exit
 */

int check_cycle(listint_t *list)
{
	listint_t *slw = list;
	listint_t *fst = list;

	if (!list)
		return (0);

	while (slw && fst && fst->next)
	{
		slw = slw->next;
		fst = fst->next->next;
		if (slw == fst)
			return (1);
	}

	return (0);
}
