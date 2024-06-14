#ifndef STACK_H
#define STACK_H

#include <stdbool.h>
#include <stdint.h>

typedef struct
{
    int32_t *arr;
    int64_t size;
    int64_t capacity;
} Stack_32;

Stack_32 *create_stack_32(int64_t capacity);
bool push_stack_32(Stack_32 *stack, int32_t data);
int32_t pop_stack_32(Stack_32 *stack);
bool is_stack_32_empty(Stack_32 *stack);
bool is_stack_32_full(Stack_32 *stack);
int32_t top_stack_32(Stack_32 *stack);
void free_stack_32(Stack_32 *stack);

#endif