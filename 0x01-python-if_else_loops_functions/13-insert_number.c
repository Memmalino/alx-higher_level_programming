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
	listint_t  *tmp = *head;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (tmp->next != NULL && number >= tmp->next->n)
		tmp  = tmp->next;
	new_node->next = tmp->next;
	tmp->next = new;
	return (new_node);
}
