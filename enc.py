#! /usr/bin/python3
from Crypto.Cipher import AES 
from Crypto.Util 
import Padding 
import sys

n=len(sys.argv)
print("Arguments passed:", n)

# takes arguments from commandline

data = bytearray(sys.argv[1], 'utf-8') # plaintext
ciphertext = bytearray.fromhex(sys.argv[2]) # encrypted result
iv = bytearray.fromhex(sys.argv[3]) # initialization vector

with open("/.words.txt""r") as file:
  for line in file:
    guess = line.strip().ljust(16,"#")
    if len(guess) <= 16:
      key = bytearray(guess, 'utf-8')
      newcipher = AES.new(key, AES.MODE_CBC, iv)
      newciphertext = newcipher.encrypt(Padding.pad(data, 16))
      
      print("Test String:", newciphertext.hex())
      print("Original Encrypted:", ciphertext.hex())
      
      if ciphertext.hex() == newciphertext.hex):
        print ("Key Found:", guess)
        exit(0)
        exit_program (0)
        break
