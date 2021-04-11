while True:
 chars = {}
 text = input()
 for char in text:
     if char.isalpha():
         if char.lower() in chars:
             chars[char.lower()] += 1
         else:
             chars[char.lower()] = 1

 print(chars)
