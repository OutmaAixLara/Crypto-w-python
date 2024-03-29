#Caesar cipher - shift by 3 rule

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str_in = input("Enter a message: ")

n = len(str_in)
str_out = ""

for i in range(n):
    c = str_in[i]
    if c in alphabets:
        loc = alphabets.find(c)
        newLoc = loc + 3
        str_out += alphabets[newLoc]
        print(newLoc, str_out)
print("Your Caesar ciphertext: ", str_out)
