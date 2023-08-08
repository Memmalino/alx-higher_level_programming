#include "lists.h"
/**
 * check_cycle - check if linked list is cyclic
 * @list: the linked list
 * Return: 0 on False and 1 if true
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *nxt;

	if (list  == NULL)
		return (0);
	current = list;
	nxt = list;
	while (nxt != NULL && nxt->next != NULL)
	{
		current = current->next;
		nxt = hxt->next->next;

		if (current == nxt)
			return (1);
	}
	return (0);
}
