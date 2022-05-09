#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: double pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *p = (*head)->next;
	int *list_int = malloc(1024 * sizeof(int));
	int i = 0;

	if (!*head || !head)
		return (1);

	while (p->n != (*head)->n)
	{
		list_int[i] = (*head)->n;
		i++;
		p = p->next;
		*head = (*head)->next;
	}
	list_int[i] = (*head)->n;
	for (; i >= 0; i--)
	{
		if (list_int[i] != p->n)
			return (0);
		p = p->next;
	}
	return (1);
}
