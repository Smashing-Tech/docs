# Save File Encyption

Progression (save) files in Mediocre games are encrypted, but usually with very weak encryption (e.g. ciphers that have been known to be broken for centuries).

## Background

In the user data folder for Smash Hit, there are a few different files: one for achivements, one for the configuration, quicksave info, `key.dat` and the save progression file.

The save progression file is `progression.xml` and is the only encrypted file.

## Helpful knowledge

The encryption is essentially just a [Vigenère cipher](https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/polyalphabetic-cipher) applied in addition to a [Cesar cipher](https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/caesar-cipher). (Yes. Please click the links.)

To explain it in short:

* **Cesar chiphers** work by taking each byte in a message and adding a constant value to it, called the shift. For example, you could have the message be the digits `5902359` and shift each character in it by one which results in `6013460`.
  * Note that the arithmetic is modular ("clock face arithmetic"), so you "cut off" any extra digits or bits you don't need. For example 9 + 1 = 10, but we only the the first digit, so it's 0.
* **Vigenère ciphers** work simiarly, but change according to a repating key instead of one constant value. For example, you might have the message `5902359` and then the key `14`. The key will expand out to `1414141` to repeat as long as the message, and then the two are added to get the encrypted text:


|   |   |   |   |   |   |   |   |
| - | - | - | - | - | - | - | - |
|   | 5 | 9 | 0 | 2 | 3 | 5 | 9 |
| + | 1 | 4 | 1 | 4 | 1 | 4 | 1 |
| - | - | - | - | - | - | - | - |
|   | 6 | 3 | 1 | 6 | 4 | 9 | 0 |

## Encryption

For the byte at index `n`, the chipertext is `Key[n % KeyLength] + (PlaintextLength & 0xff)` added to the original byte. (Or to say it differently: that is the keystream at each byte.)

## Mathematical description

Given a plaintext $p$ (of length $|p|$) and a key $k$ (of length $|k|$), the encryption function $e(p, k)$ encrypts a byte of plaintext $p_i$ as:

$$e(p, k) = (p_i + (k_{i \mod |k|} + |p|)) \mod 256$$

Given a ciphertext $c$ (of length $|c|$) and a key $k$ (of length $|k|$), the decryption function $d(c, k)$ decrypts a byte of plaintext $c_i$ as:

$$d(c, k) = (c_i - (k_{i \mod |k|} + |c|)) \mod 256$$

## Keys

For quick reference, here are the keys for some of the games:

| Game | Key | Unleetspeaked |
| --- | --- | --- |
| Sprinkle | `HulT3T__R0ck5!` | Hultet Rocks!<sup>3</sup> |
| Sprinkle Jr | `HulT3T__R0ck5!` | Hultet Rocks!<sup>3</sup> |
| Sprinkle Islands | `0u1er0ck5` | Ouie rocks |
| Granny Smith | `gr4nny0n5k47es` | Granny On Stakes |
| Smash Hit | `5m45hh1t41ght` | Smash Hit Aight |
| Beyondium | `d1r4c15Da5h1T` | DIRAC Is Da Shit<sup>2</sup> |
| Does not Commute | `d035n0tc0mmut3inl33t` | Does not commute in leet |
| PinOut | `n01t15ntp1n0ut1s` | No it isn't, PinOut is |

1. The free versions of the first few games appear to share the encryption keys with their paid versions.
2. DIRAC was the former name of Beyondium.
3. Not sure what it means.
