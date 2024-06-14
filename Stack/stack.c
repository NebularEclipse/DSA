#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "stack.h"

Stack_32 *create_stack_32(int64_t capacity)
{
    // Allocate memory for the stack structure.
    Stack_32 *stack = (Stack_32 *)malloc(sizeof(Stack_32));
    if (stack == NULL)
        return NULL; // Return NULL in case of memory allocation failure.

    // Allocate memory for the stack array
    stack->arr = (int32_t *)malloc(sizeof(int32_t) * capacity);
    if (stack->arr == NULL)
    {
        // Free the stack structure and return NULL in case of memory allocation failure.
        free(stack);
        return NULL;
    }

    // Set stack capacity to the capacity parameter of the function.
    stack->capacity = capacity;
    // Set stack size to 0.
    stack->size = 0;

    return stack;
}

bool push_stack_32(Stack_32 *stack, int32_t data)
{
    // Check if stack is not full before pushing the data.
    if (!is_stack_32_full(stack))
    {
        stack->arr[stack->size++] = data;
        return true; // Return true if push was successful.
    }
    
    // Return false in case stack is full.
    fprintf(stderr, "Stack is full\n");  // Print error message to stderr
    return false;
}

int32_t pop_stack_32(Stack_32 *stack)
{
    // Check if stack is not empty before popping a value.
    if (!is_stack_32_empty(stack))
        return stack->arr[--stack->size];

    fprintf(stderr, "Stack is empty\n");  // Print error message to stderr.
    return -1; // Returns a sentinel value.
}

bool is_stack_32_empty(Stack_32 *stack)
{
    // Check if stack is empty or not
    return stack->size == 0;
}

bool is_stack_32_full(Stack_32 *stack)
{
    // Check if stack is full or not
    return (stack->size >= stack->capacity) ? true : false;
}

int32_t top_stack_32(Stack_32 *stack)
{
    if (!is_stack_32_empty(stack))
        return stack->arr[(stack->size) - 1];
    
    fprintf(stderr, "Stack is empty\n");  // Print error message to stderr.
    return -1; // Returns a sentinel value.
}

void free_stack_32(Stack_32 *stack)
{
    // If stack is not NULL, free.
    if (stack != NULL)
    {
        free(stack->arr);  // Free the array
        free(stack);       // Free the stack structure
    }
}