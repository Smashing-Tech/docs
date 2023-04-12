# TdContextInternal

Holds internal context data for the physics context.

This struct is 24 bytes:

```cpp
typedef void *(*memory_alloc_t)(size_t size);
typedef void (*memory_free_t)(void *block);

struct TdContextInternal {
    memory_alloc_t memory_alloc;
    memory_free_t memory_free;
    int32_t max_iterations;
    float tolerence;
};
```

> Tip: In C++, a struct is a class where every member is public by default.
