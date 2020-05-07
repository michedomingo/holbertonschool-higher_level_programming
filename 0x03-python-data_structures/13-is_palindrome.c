#include "lists.h"

listint_t *reverse(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next;
	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	*head = prev;
	return (*head);
}

int is_palindrome(listint_t **head)
{
	listint_t *first_ptr = *head;
	listint_t *last_ptr = *head;

	for (; first_ptr && first_ptr->next; last_ptr = last_ptr->next)
	{
		first_ptr = first_ptr->next->next;
	}
	first_ptr = *head;
	last_ptr = reverse(&last_ptr);

	while (first_ptr && last_ptr)
	{
		if (first_ptr->n == last_ptr->n)
		{
			first_ptr = first_ptr->next;
			last_ptr = last_ptr->next;
		}
		else
			return (0);
	}
	return (1);
}
