#!/usr/bin/env python
"""
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. 
If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. T
he balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. 
Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
"""
import itertools

text = open("p059_cipher.txt").read().split(",")
ciphertext = [int(x) for x in text]
print ciphertext

# generator of  ascii codes for all lowercase chars
all_chars = xrange(ord('a'), ord('z') + 1)
# all possible keys
all_keys = itertools.product(all_chars, repeat=3)

def try_key(key):
	decrypt = range(len(ciphertext))
	for i, k in enumerate(key):
		for j in xrange(i, len(decrypt), len(key)):
			decrypt[j] = ciphertext[j] ^ k
	decrypt_str = ''.join((chr(x) for x in decrypt))
	if ' the ' in decrypt_str:
		return (decrypt_str, sum(decrypt))
	return None

result = []
for key in all_keys:
	decrypted_str = try_key(key)
	if(decrypted_str):
		print decrypted_str

print result

		