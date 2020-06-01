'''

Apply a Cesar cipher of 7 to the 'secret' variable.

'''

secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7

'''
secret = input("What is your secret? : ")
cipher = int(input("Apply cipher? (value) : "))
'''

# The encrypted code should be decrypted using the negative of the encryption cipher.
# This script deals with +ve ciphers. Adding 26 to a -ve cipher gives the equivalent +ve cipher.
if cipher < 0:
    cipher += 26

plain_l = 'abcdefghijklmnopqrstuvwxyz'
plain_u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cipher_l = plain_l[26-cipher:] + plain_l[:26-cipher]
cipher_u = cipher_l.upper()

cipher_dict = {}
for i in range(26):
    cipher_dict[plain_u[i]] = cipher_u[i]
    cipher_dict[plain_l[i]] = cipher_l[i]

cipher_text = []
for char in secret:
    if char.isalpha():
        cipher_text.append(cipher_dict[char])
    else:
        cipher_text.append(char)

cipher_str = ''.join(cipher_text)

print(f"With cipher applied to secret: \n {cipher_str}")
