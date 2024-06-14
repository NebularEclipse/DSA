#include <stdio.h>

#include "stack.h"

int main(void)
{
    Stack_32 *stack = create_stack_32(5);

    for (int i = 0; i <= 5; i++)
    {
        if (push_stack_32(stack, i))
            printf("%i pushed successfully\n", i);

        else
            printf("Failed to push %i\n", i);
    }

    for (int i = 0; i < 5; i++)
        printf("%i ", pop_stack_32(stack));

    free_stack_32(stack);

    return 0;
}