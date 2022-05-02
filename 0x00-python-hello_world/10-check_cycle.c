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
	size_t i;
	listint_t *addr = list;

	for (i = 0; list && addr && addr->next; i++)
	{
		list = list->next;
		addr = addr->next->next;
		if (addr == list)
			return (1);
	}
	return (0);
}
