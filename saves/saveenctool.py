"""
Smash Hit save decryptor

The encryption is pretty cheap, it's essentially this:

Ciphertext[n] = Plaintext[n] + (Key[n % KeyLength] + (DataLength & 0xff))
Plaintext[n] = Ciphertext[n] - (Key[n % KeyLength] + (DataLength & 0xff))

It is essentially just a Vigenère cipher with a bit of extra stuff to make the
keystream less obvious.

This seems like a nice website:
https://crypto.interactive-maths.com/vigenegravere-cipher.html

But if you look at a video you will probably get a better idea.
"""

import struct

def printHelp(argv):
	print("Usage:")
	print(argv[0], "encrypt [input] [output]")
	print(argv[0], "decrypt [input] [output]")

def decryptBytes(data, key = "5m45hh1t41ght"):
	"""
	Decrypt save data
	"""
	
	out = bytearray()
	
	for i in range(len(data)):
		# Unpack the byte
		byte = data[i]
		
		# Decrypt byte
		byte = byte - (ord(key[i % len(key)]) + (len(data) % 256))
		
		# Emulate interger overflow
		byte %= 256
		
		# Write byte out
		out += struct.pack('B', byte)
	
	return out

def decryptFile(input, output):
	# Read save file
	f = open(input, "rb")
	content = f.read()
	f.close()
	
	# Decrypt
	out = decryptBytes(content)
	
	# Write plaintext file
	f = open(output, "wb")
	content = f.write(out)
	f.close()

def encryptBytes(data, key = "5m45hh1t41ght"):
	"""
	Encrypt save data
	"""
	
	out = bytearray()
	
	for i in range(len(data)):
		# Unpack the byte
		byte = data[i]
		
		# Decrypt byte
		byte = byte + (ord(key[i % len(key)]) + (len(data) % 256))
		
		# Emulate interger overflow
		byte %= 256
		
		# Write byte out
		out += struct.pack('B', byte)
	
	return out

def encryptFile(input, output):
	# Read save file
	f = open(input, "rb")
	content = f.read()
	f.close()
	
	# Decrypt
	out = encryptBytes(content)
	
	# Write plaintext file
	f = open(output, "wb")
	content = f.write(out)
	f.close()

def main():
	import sys
	
	if (len(sys.argv) == 4):
		if (sys.argv[1] == "encrypt"):
			encryptFile(sys.argv[2], sys.argv[3])
		elif (sys.argv[1] == "decrypt"):
			decryptFile(sys.argv[2], sys.argv[3])
		else:
			printHelp(sys.argv)
	else:
		printHelp(sys.argv)

if (__name__ == "__main__"):
	main()
