#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - function that check if a linked list is palindrome
 * @head: double pointer to the head of the linked list to check
 * Return: return 0 if it is not palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int n, i, a, j;
	int *name;
	listint_t *current;
	listint_t  *new;

	current = *head;
	if (*head == NULL)
	{
		return (1);
	}
	n = 0;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}
	name = malloc(sizeof(int) * n);
	if (name == NULL)
	{
		return (0);
	}
	new = *head;
	for (i = 0; new != NULL && i < n; i++)
	{
		name[i] = new->n;
		new = new->next;
	}
	for (a = 0; a < n / 2; a++)
	{
		j = n - a - 1;
		if (name[a] != name[j])
		{
			free(name);
			return (0);
		}
	}
	free(name);
	return (1);
}
