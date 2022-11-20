# Anti-tamper

Mediocre games on Android released starting with Smash Hit 1.3.0 contain anti-tamper that checks file hashes for a few game binaries, probably to prevent piracy and/or make cracked APKs harder to make.

iOS IPAs have not been checked for any protections, but it is unlikely they contain protections since sideloading is much harder on iOS.

## Description

The global variable `gGenuine` keeps track of the game being considered untampered. While it is true by default, there are checks throughout the game which compare the checksum in `gChecksum`, and if it is not the same, they set this variable to false.

The contents of `gChecksum` are computed at runtime and contain the current APK checksum. The APK checksum takes into account any files that end with the strings `classes.dex` or `.so`, but any other files are ignored.

The function `void computeChecksum(QiString& path, const char *output)` will compute the checksum for the current set of files. It is called once at the start of `android_main` with it's output being written to `gChecksum`. It looks like it uses a custom hash function.

It's currently not clear where the expected checksum of the files is loaded from. In Ghidra, it appears to already be present in the stack in `android_main` when the function begins, though this might be a decompiler error.

## Behaviour

### `gGenuine == false`

When `gGenuine` is false, the game exits as it is part of the while loop that keeps the game running.

### `LoadedChecksum != gChecksum`

When the checksum does not match, the game usually either:

1. Continues running normally
2. Exit the game nicely

There is no one function that compares the checksum, probably to make it harder to patch out. Instead, it is done manually each time.

Some version of the check appears in each of these functions at least once:

* `FUN_00146170`
* `android_main`

## Notes

1. Smash Hit versions before 1.3.0 did not have anti-tamper protection.
2. Reversing was done using Smash Hit 1.4.2 for Android (ARM 64-bit)
