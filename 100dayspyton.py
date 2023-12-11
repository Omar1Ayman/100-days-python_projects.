def binary():
    base = 2
    binary = []
    number = int(input("convert to binary "))
    while number > 0:
        #print(f"number : {number}")
        if(number == 1):
            binary.append("1")
            number = 0
            break
        else:
            if(number % 2 == 0):
                number = int(int(number) / base)
                binary.append("0")
            else:
                number = int(int(number) / base)
                binary.append("1")
    binary.reverse()
    b = ''.join(binary)
    print(f"0b{b}")

#binary()




#admin = [ {"username" : "omar" , "password" : "123456"} , {"username" : "moh" , "password" : "12345"} ]

import random
lsit_words = ["camel" , "rabbit" , "cat" , "donky"]
chosen_word = random.choice(lsit_words)
#print(f"the word chosen is {chosen_word}")

display = ["_" for i in range(len(chosen_word))]

lives = len(chosen_word)

#print(f"length word is {len(chosen_word)} {chosen_word}")
#end_of_game = False
##while not end_of_game:
##    guess = input(f"your guess letter: ").lower()
##    for pos in range(len(chosen_word)):
##        letter = chosen_word[pos]
##        if letter == guess:
##            display[pos] = letter
##    print(display)
##    if guess not in chosen_word:
##        lives -=1
##        if lives == 0:
##            end_of_game = True
##            word = "".join(display)
##            print(f"you lose the word you gused was {word} , the real word was {chosen_word}")
##    if "_" not in display:
##        end_of_game = True
##        word = "".join(display)
##        print(f"you won the word yuo gused was {word}")
##    



from math import ceil

def num_can(height , width ,cover= 5):
    numofcan = (height * width ) / cover
    print(f"you need {ceil(numofcan)} to paint {height * width} m")



#h = int(input("height: "))
#w = int(input("width: "))
#num_can(h,w)



def isPrime(x):
    isprime = True
    for i in range(2 , x):
        if x % i == 0:
            isprime = False
    if isprime:
        print("prime")
    else:
        print("not prime")


from string import ascii_uppercase 
def Encode_Caesar_cipher(s,k):
    res = ""
    letters = ascii_uppercase
    for i in s.upper():
        if i in letters:
            index = (letters.index(i) + k) % len(letters)
            res += letters[index]
        else:
            res += i
    return res



def Decode_Caesar_cipher(s,k):
    res = ""
    letters = ascii_uppercase
    for i in s.upper():
        if i in letters:
            index = (letters.index(i) - k) % len(letters)
            res += letters[index]
        else:
            res += i
    return res
       


repeat = False
while repeat:
    typ = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    if typ == 'encode':
        mes = input("Type your message: \n")
        key = int(input("Type your shift number: \n"))
        print(Encode_Caesar_cipher(mes,key))
    elif typ == 'decode':
        mes = input("Type your message: \n")
        key = int(input("Type your shift number: \n"))
        print(Decode_Caesar_cipher(mes,key))
    again = input("type 'yes' if you want to go again. Otherwise type 'no' ").lower()
    if again == "no":
        print("Bye!")
        repeat = False

 
print("welcome to the secret action program.")
bidders = {}
r= True
while r:
    name = input("what is your name?: ")
    bid = int(input("what is your bid?: $"))
    if name not in bidders:
        bidders[name] = bid
        ask = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    else:
        print("this name already exist")
        ask = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if ask == "yes":
        continue
    else:
        h = 0
        n = ""
        for k,v in bidders.items():
            if v > h:
                h = v
                n = k
        print(f"The winner is {n} with a bid of ${h}")
        print("Bye!")
        r = False


    

