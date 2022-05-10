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
	int i = 0, case_odd = 0;

	if (!*head || !head || !(*head)->next)
	{
		free(list_int);
		return (1);
	}
	p = (*head)->next;
	while ((p->n != (*head)->n))
	{
		if (p->next && (*head)->n == p->next->n)
		{
			case_odd = 1;
			break;
		}
		list_int[i] = (*head)->n, i++, p = p->next;
		if (!p)
		{
			free(list_int);
			return (0);
		}
		*head = (*head)->next;
	}
	if (case_odd)
		p = p->next;
	list_int[i] = (*head)->n;
	while (i >= 0)
	{
		if (list_int[i] != p->n)
		{
			free(list_int);
			return (0);
		}
		p = p->next, i--;
	}
	free(list_int);
	return (1);
}
