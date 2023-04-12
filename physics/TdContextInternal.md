# TdContextInternal

Holds internal context data for the physics context.

This struct is 24 bytes:

```cpp
struct TdContextInternal {
    void *memory_alloc;
    void *memory_free;
    int32_t max_iterations;
    int32_t tolerence;
};
```

> Tip: In C++, a struct is a class where every member is public by default.
