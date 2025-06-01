import random
import string
length=int(input("enter desired password length:"))
chars=string.ascii_letters+string.digits+string.punctuation
password=' '.join(random.choice(chars)for _ in range(length))
print("generated password:",password)
