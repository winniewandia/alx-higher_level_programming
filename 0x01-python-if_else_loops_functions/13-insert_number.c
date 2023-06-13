#include "lists.h"
/**
 * insert_node - inserts a node in alist
 * @head: Address of next node
 * @number: Number to be added
 *
 * Return: Address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *prev, *current, *new;

    current = *head;
    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);
    while (current != NULL)
    {
        if (current->n > number)
            break;
        prev = current;
        current = current->next;
    }
    new->n = number;
    if (*head == NULL)
    {
        new->next = NULL;
        *head = new;
    }
    else
    {
        new->next = current;
        if (current == *head)
        {
            *head = new;
        }
        else
        {
            prev->next = new;
        }
    }
    return (new);
}