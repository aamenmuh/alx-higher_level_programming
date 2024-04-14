#include "lists.h"

/**
 * check_cycle - check if cycle exists
 * @list: pointer to list
 *
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
    listint_t *singleStep = list;
    listint_t *doubleStep = list;

   if (!list)
       return (0);

   while (singleStep && doubleStep && doubleStep->next)
   {
        singleStep = singleStep->next;
        doubleStep = doubleStep->next->next;
        if (singleStep == doubleStep)
        {
            return (1);
        }
   }

   return (0);
}
