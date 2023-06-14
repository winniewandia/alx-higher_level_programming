#include "lists.h"

/**
 * reverseList - reverses a list
 * @head: Pointer to head of list
 *
 * Return: a reversed list
 */

listint_t *reverseList(listint_t *head)
{
    listint_t *prev = NULL;
    listint_t *current = head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return (prev);
}
/**
 * compareLists - checks if 2 lists are equal
 * @list1: First list to be checked
 * @list2: 2nd list to be checked
 *
 * Return: 0 if lists are equal and 1 otherwise
 */

int compareLists(listint_t *list1, listint_t *list2)
{
    while (list1 != NULL && list2 != NULL)
    {
        if (list1->n != list2->n)
            return (0);
        list1 = list1->next;
        list2 = list2->next;
    }
    if (list1 == NULL && list2 == NULL)
        return (1);
    return (0);
}
/**
 * is_palindrome - checks if a list is a palindrome
 * @head: Pointer to the head of the list
 *
 * Return: 1 if its a palindrome and 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev_slow = *head;
    listint_t *mid = NULL;
    listint_t *second_half;
    int is_palindrome;

    if (*head == NULL)
        return (1);
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }
    if (fast != NULL)
    {
        mid = slow;
        slow = slow->next;
    }
    second_half = slow;
    prev_slow->next = NULL;
    second_half = reverseList(second_half);
    is_palindrome = compareLists(*head, second_half);
    second_half = reverseList(second_half);
    if (mid != NULL)
    {
        prev_slow->next = mid;
        mid->next = second_half;
    }
    else
    {
        prev_slow->next = second_half;
    }

    return (is_palindrome);
}
