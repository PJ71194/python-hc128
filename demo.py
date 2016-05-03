import hc128

key = "0F62B5085BAE0154A7FA4DA0F34699EC"
IV = "288FF65DC42B92F960C72E95FC63CA31"

print "Initializing HC-128 cipher state"
print "Key = " + key
print "IV = " + IV

hc128.init(key, IV)

print "\nHC-128 Cipher state initialized"

while True:
  plain_text = raw_input("\nEnter plain text(in hex bytes, 4 at a time) to encrypt: ")

  if len(plain_text) != 8:
    break

  print "\nGenerating keystream, 4 bytes at a time"
  k = hc128.keygen()
  print "Keystream generated: " + k

  plain_text = plain_text.decode("hex")
  k = k.decode("hex")
  cipher_text = ""

  for i in range(0, 4):
    cipher_text += chr(ord(plain_text[i]) ^ ord(k[i]))

  cipher_text = cipher_text.encode("hex")

  print "Encrypted cipher text: " + cipher_text

hc128.init(key, IV)
hc128.i = 0

print "Reinitializing HC-128 cipher"

while True:
  cipher_text = raw_input("\nEnter cipher text(in hex bytes, 4 at a time) to decrypt: ")

  if len(cipher_text) != 8:
    break
  
  print "\nGenerating keystream, 4 bytes at a time"
  k = hc128.keygen()
  print "Keystream generated: " + k

  cipher_text = cipher_text.decode("hex")
  k = k.decode("hex")
  plain_text = ""

  for i in range(0, 4):
    plain_text += chr(ord(cipher_text[i]) ^ ord(k[i]))

  plain_text = plain_text.encode("hex")

  print "Decrypted plain text: " + plain_text
