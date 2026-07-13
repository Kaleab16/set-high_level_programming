#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 *
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *next = NULL;
    listint_t *second_half;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    /* Find middle of linked list */
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        slow = slow->next;
    }

    /* Reverse second half */
    second_half = slow;
    while (second_half != NULL)
    {
        next = second_half->next;
        second_half->next = prev;
        prev = second_half;
        second_half = next;
    }

    /* Compare first and second halves */
    second_half = prev;
    slow = *head;
    while (second_half != NULL)
    {
        if (slow->n != second_half->n)
            return (0);
        slow = slow->next;
        second_half = second_half->next;
    }

    return (1);
}
