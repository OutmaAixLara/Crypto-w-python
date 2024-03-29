#Caesar cipher - shift by 3 rule

alphabets_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabets_min = "abcdefghijklmnopqrstuvwxyz"
str_in = input("Enter a message: ")

n = len(str_in)
str_out = ""

for i in range(n):
    c = str_in[i]
    if c in alphabets_maj:
        loc = alphabets_maj.find(c)
        newLoc = (loc + 3)%26
        str_out += alphabets_maj[newLoc]
        print(loc, c, newLoc, str_out)
    elif c in alphabets_min:
        loc = alphabets_min.find(c)
        newLoc = (loc + 3)%26
        str_out += alphabets_min[newLoc]
        print(loc, c, newLoc, str_out)
    else:
        print("Invalid message!")
        str_in = input("Enter a message: ")
print("Your Caesar ciphertext: ", str_out)
