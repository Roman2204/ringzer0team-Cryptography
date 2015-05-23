# Caesar_cipher
KEY = 13

cipher_text = input()

print (cipher_text)
cipher_text_ascii = [ord(c) for c in cipher_text]
print (cipher_text_ascii)

plain_text_ascii = []
for each_cipher_char in cipher_text_ascii:
    if  each_cipher_char >= 65 and  each_cipher_char <= 90 :
         each_cipher_char =  ( each_cipher_char - (65 + KEY) ) % 26 + 65
    elif each_cipher_char >= 97 and  each_cipher_char <= 122 :
        each_cipher_char =  ( each_cipher_char - (97 + KEY) ) % 26 + 97
    else : print ("The symbol '" + each_cipher_char + "' does not belong to the range of English letters")
    plain_text_ascii.append(each_cipher_char)
    
print (plain_text_ascii)
plain_text = [chr(a) for a in plain_text_ascii]
print (plain_text)

for each_plain_char in plain_text:
    print (each_plain_char, end='')
