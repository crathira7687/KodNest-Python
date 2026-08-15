n = int(input("enter the number of words:"))
word_frequency = {}
for i in range(n):
    word = input("enter the word:")
    if word in word_frequency:
        word_frequency[word]+=1
    else:
        word_frequency[word] = 1

for word, count in word_frequency.items():
    print(word, count)