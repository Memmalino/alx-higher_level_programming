#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - function that insert a new node to a linked list
 * @head: pointer to the head of a linked list
 * @number: the value to be added to the new node
 * Return: the new node on success  else Null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t  *tmp = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (tmp->next != NULL && number >= tmp->next->n)
		tmp  = tmp->next;
	new->next = tmp->next;
	tmp->next = new;
	return (new);
}
