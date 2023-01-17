# Mod Loader

We are planning a mod loader for Smash Hit that will allow downloading stages from a server.

## Method 1: Use builtin HTTP loading

Since Smash Hit already supports loading assets over HTTP, we could already download menus from a server (as images) to suggest stages and then load them from the network.

This has a few problems:

1. HTTP loading blocks the main thread, and it loads a segment *every time* it is placed, leading to 2 - 4 second pauses between rooms.
2. HTTP loading is not reliable and fails in obtuse ways.
3. You cannot use HTTPS, which may limit the types of servers that can be used.
4. You cannot just search for segments, you need to find the one you want each time.
5. ....

## Method 2: Use custom download() lua function + lua `io` module loading

A custom download method requires more work (more custom code + how to load it to scripts) but could allow us to be more dynamic in how we download things. For example, we could download a definitions file, then use that to download images and text desriptions, then download each segment file to the device the first time and then always just load from internal storage.
