#include "lists.h"

/**
 * *insert_node - inserts a new node in sorted linked list.
 * @head: listint_t double pointer input
 * @number: int input
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *aux = *head, *tmp;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		free(new);
		return (NULL);
	}
	while (aux)
	{
		if (number <= aux->n)
			break;
		tmp = aux;
		aux = (aux)->next;
		if (!aux)
			return (NULL);
	}
	new->n = number;
	if (aux)
		new->next = aux;
	else
		new->next = NULL;
	tmp->next = new;
	return (new);
}
