from passwordunblock import *
password = "abcda"

generator = latter_password(5)
gen_pass = next(generator)

while generator != password:
    gen_pass = next(generator)
    print(gen_pass)

print(gen_pass)
