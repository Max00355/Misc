import json
import string
import pprint
import random

def train(training_file, length):
    print "Training..."
    training_data = {}
    for letter in string.lowercase:# + string.punctuation:
        training_data[letter] = {}
    data = open(training_file, 'r').read().split()
    for data in data:
        data = data.lower()
        if len(data) != length:
            continue
        prev = None
        for char in data:
            if char == " ":
                prev = None
                continue
            if char not in string.lowercase:# and char not in string.punctuation:
                continue
            if prev == None:
                prev = char
                continue
            if char not in training_data[prev]:
                training_data[prev][char] = 1
            else:
                training_data[prev][char] += 1
            prev = char

    pprint.pprint(training_data)
    json.dump(training_data, open("training_data.json", 'w'))

def generate_chain():
    data = json.load(open("training_data.json"))
    chain = {}
    for letter in data:
        chain[letter] = []
        total_letters = 0
        for following_letter in data[letter]:
            total_letters += data[letter][following_letter]             
        for following_letter in data[letter]:
            following = data[letter][following_letter]
            percentage = {"letter":following_letter, "percentage":float(following) / total_letters}
            chain[letter].append(percentage)
        
        chain[letter] = sorted(chain[letter], key=lambda x: x['percentage'])
        chain[letter].reverse()
    return chain

def generator(words, length):
    chain = generate_chain()
    pprint.pprint(chain)
    for x in range(words):
        word = ""
        prev = None
        for x in range(length):
            if prev == None:
                prev = random.choice(string.lowercase)
            else:
                letters = chain[prev]
                chances = random.randint(1, 100)/100.0
                for letter in letters:
                    if letter['percentage'] <= chances:
                        percent = letter['percentage']
                        break
                else:
                    if len(letters) == 0:
                        continue
                    percent = letters[-1]['percentage']

                all_letters = []
                for letter in letters:
                    if letter['percentage'] == percent:
                        all_letters.append(letter)
                next_letter = random.choice(all_letters)
                word += prev
                prev = next_letter['letter']
        word += prev
        print word
todo = raw_input("What would you like to do? [train/generate] ")

if todo.lower() == "train":
    training_file = raw_input("Training file: ")
    train(training_file, int(raw_input("How long are the words that you want to generate? ")))
else:
    generator(int(raw_input("How many words would you like to generate? ")), int(raw_input("How long are the words that you want to generate? ")))
