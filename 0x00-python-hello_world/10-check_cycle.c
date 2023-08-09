#include "lists.h"
/**
 * check_cycle - function that checks if a linked list\\
 contains a cycle
 * @list: the pointer to the head node of the list
 * Return: 1 if cycle is found, 0 if not found
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}

