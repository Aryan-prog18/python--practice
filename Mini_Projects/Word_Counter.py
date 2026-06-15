# concepts we are going to use are spilt(), count()
Sentence = input("Enter a sentence: ")
word = input("Enter a word to find: ")

words = Sentence.split()

print("Total words are: ", len(words))
print("The word repeate's : ", Sentence.lower().count(word.lower()))
