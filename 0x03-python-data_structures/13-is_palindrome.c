#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: double pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *p;
	int *list_int = malloc(1024 * sizeof(int));
	int i = 0;

	if (!*head || !head)
	{
		free(list_int);
		return (1);
	}

	p = (*head)->next;
	if (!p)
	{
		free(list_int);
		return (0);
	}
	while (p->n != (*head)->n)
	{
		list_int[i] = (*head)->n;
		i++;
		p = p->next;
		if (!p)
		{
			free(list_int);
			return (0);
		}
		*head = (*head)->next;
	}
	list_int[i] = (*head)->n;
	for (; i >= 0; i--)
	{
		if (!p)
		{
			free(list_int);
			return (0);
		}
		if (list_int[i] != p->n)
		{
			free(list_int);
			return (0);
		}
		p = p->next;
	}
	free(list_int);
	return (1);
}
