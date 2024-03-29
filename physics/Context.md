# Contexts

Contexts hold some state for the physics library.

## Functions

### `TdContextInternal *tdContextCreate(memory_alloc_t alloc_function, memory_free_t free_function)`

Creates and returns a default context.

Here is a decompilation of what is happening:

```cpp
TdContextInternal *tdContextCreate(memory_alloc_t alloc_function, memory_free_t free_function) {
    if (alloc_function == nullptr) {
        alloc_function = &malloc;
    }
    
    if (free_function == nullptr) {
        free_function = &free;
    }
    
    TdContextInternal *context = (TdContextInternal *) alloc_function(sizeof *context);
    
    context->memory_alloc = alloc_function;
    context->memory_free = free_function;
    
    // Comment: Yes, the params are really reversed like this.
    tdContextSetMaxIterations(context, 0x20);
    tdContextSetTolerance(0.001f, context);
    
    return context;
}
```

### `void tdContextDestroy(TdContextInternal *context)`

Frees the context.
