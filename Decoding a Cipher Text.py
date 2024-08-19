def decode_ciphertext(ciphertext, key):
  # Write your code here
  alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  #print(type(key))
  
  key_dict = dict(zip(key,alphabet))
  #print(key_dict)
  
  deciphertext =''
  for char in ciphertext:
    if char.isalpha():
      deciphertext += key_dict[char]
    else:
      deciphertext += char
  print(deciphertext)
    
ciphertext = 'W RANU JEYA'
key = 'WXYZABCDEFGHIJKLMNOPQRSTUV'
decode_ciphertext(ciphertext, key)
