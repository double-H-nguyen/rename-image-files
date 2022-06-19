import re

phrase = "hello world: how are you?"
print(phrase)

# \s are white space, \: is colon, | means OR
phrase2 = re.sub(pattern=r'\s|\:', repl='_', string=phrase)
print(phrase2)
