with open("nato_phonetic_alphabet.csv") as file:
    data = file.readlines()
    obj = {}
    for d in data[1:]:
        d = d.split(",")
        obj[d[0]] = d[1].strip()

while True:
    word = input("enter word: ").upper()
    alpha = []
    for i in word:
        for key,value in obj.items():
            if i == key:
                alpha.append(value)    
    print(alpha)
    if input("again (yes / no)? ") != "yes":
        print("Bye!")
        break
    
