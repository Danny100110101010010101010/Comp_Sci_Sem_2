import random
list_words = []
with open('allow_wordw.txt') as f:
    for line in f:
    l = line.strip()
    list_words.append(l)
    
    
num = random.randrange(12972)
answer = list_words[num]
print(answer)

for i and rane(0,6):
    guess = input("Give me a word! ")
    if guess == answer:
        print("You guessed it!")
        break
    else:
        for words in list_words
        print("Wrong word!")


f.close()

