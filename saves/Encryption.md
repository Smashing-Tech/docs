# Save File Encyption

Progression (save) files in Smash Hit (and other Mediocre games) are encrypted, though it is usually weak.

## Background

In the user data folder for Smash Hit, there are a few different files: one for achivements, one for the configuration, quicksave info, `key.dat` and the save progression file.

The save progression file is `progression.xml` and is the only encrypted file.

## Helpful knowledge

The encryption is essentially just an Affine cipher, which is a [Vigenère cipher](https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/polyalphabetic-cipher) applied in addition to a [Cesar cipher](https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/caesar-cipher). (Yes. Please click the links.)

For those who don't know:

* **Cesar chiphers** work by taking each byte in a message and adding a constant value to it, called the shift. For example, you could have the message be the digits `5902359` and shift each character in it by one which results in `6013460`.
  * Remember that the arithmetic is modular ("clock face arithmetic"), so you "cut off" any extra digits or bits you don't need. For example 9 + 1 = 10, but we only the the first digit, so it's 0.
* **Vigenère ciphers** work simiarly, but change according to a repating key instead of one constant value. For example, you might have the message `5902359` and then the key `14`. The key will expand out to `1414141` to repeat as long as the message, and then the two are added to get the encrypted text:


|   |   |   |   |   |   |   |   |
| - | - | - | - | - | - | - | - |
|   | 5 | 9 | 0 | 2 | 3 | 5 | 9 |
| + | 1 | 4 | 1 | 4 | 1 | 4 | 1 |
| - | - | - | - | - | - | - | - |
|   | 6 | 3 | 1 | 6 | 4 | 9 | 0 |

## Encryption

For the byte at index `n`, the chipertext is `Key[n % KeyLength] + (PlaintextLength & 0xff)` added to the original byte. (Or to say it differently: that is the keystream at each byte.)

## Keys

For quick reference, here are the keys for some of the games:

| Game | Key | Unleetspeaked |
| --- | --- | --- |
| Sprinkle Islands | `0u1er0ck5` | Ouie rocks |
| Granny Smith | `gr4nny0n5k47es` | Granny On Stakes |
| Smash Hit | `5m45hh1t41ght` | Smash Hit Aight |
| Beyondium | `d1r4c15Da5h1T` | Dirac Is Da Shit |
| Does not Commute | `d035n0tc0mmut3inl33t` | Does not commute in leet |
| PinOut | `n01t15ntp1n0ut1s` | no it isnt pinout is |
