# Save File Encyption

Progression (save) files in Smash Hit (and other Mediocre games) are encrypted, though it is usually weak.

## Background

In the user data folder for Smash Hit, there are a few different files: one for achivements, one for the configuration, quicksave info, `key.dat` and the save progression file.

The save progression file is `progression.xml` and is the only encrypted file.

## Encryption

> TODO Actually explain the encryption

The encryption is essentially just a Vigenère cipher with an added constant to make the keystream less obvious.

For the byte at index `n`, the chipertext is `Key[n % KeyLength] + (PlaintextLength % 256)` added to the original byte. (Or to say it differently: that is the keystream at each byte.)
