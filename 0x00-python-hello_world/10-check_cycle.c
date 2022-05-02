#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check if the linked list is a circular link
 * @list: pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	size_t i, j;
	listint_t *addr = list, *head = list;

	for (i = 0; list; i++)
	{
		addr = head;
		for (j = 0; j < i; j++)
		{
			if (addr == list->next)
				return (1);
			addr = addr->next;
		}
		list = list->next;
	}
	return (0);
}
