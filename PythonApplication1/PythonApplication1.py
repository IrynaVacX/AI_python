import urllib.request

req = urllib.request.Request('https://random-word-api.herokuapp.com/word')
with urllib.request.urlopen(req) as response:
   WORD = response.read()

def print_word(word_to_guess, letters_used):
    global correct_letters
    for ch in word_to_guess:
        if ch in letters_used:
            print(f"{ch}", end = '')
            correct_letters += 1
        else:
            print("_", end = '')
    print()
  
def print_letter(letters):
    for l in letters:
        print(f"{l} ", end = '')
    print()

gallows = ["\n\n\n\n\n\n ________\n/        \\\n",
"\n   |\n   |\n   |\n   |\n   |\n __|______\n/         \\\n",
"   _______\n   |\n   |\n   |\n   |\n   |\n __|______\n/         \\\n",
"   _______\n   |/\n   |\n   |\n   |\n   |\n __|______\n/         \\\n",
"   _______\n   |/    |\n   |\n   |\n   |\n   |\n __|______\n/         \\\n",
"   _______\n   |/    |\n   |    ()\n   |\n   |\n   |\n __|______\n/         \\\n",
"   _______\n   |/    |\n   |    (O)\n   |\n   |\n   |\n __|______\n/         \\\n",
"   _______\n   |/    |\n   |    (O)\n   |     I\n   |\n   |\n __|______\n/         \\\n",
"   _______\n   |/    |\n   |    (O)\n   |    /I\\\n   |\n   |\n __|______\n/         \\\n",
"   _______\n   |/    |\n   |    (O)\n   |    /I\\\n   |    /\\\n   |\n __|______\n/         \\\n"]
word = WORD.decode('UTF-8')
word_to_guess = ''
for c in word:
    if c != '[' and c != ']' and c != '"':
        word_to_guess += c
letters_used = ""
failed_attempts = 0

print_word(word_to_guess, letters_used)

while failed_attempts < 10:
    letter = input("Enter your letter: ")
    if letter.lower() not in letters_used:
        letters_used += letter.lower()
    else:
        failed_attempts = failed_attempts - 1

    if letter in word_to_guess:
        print(f"Well done! Letter {letter} is present in this word")
    else:
        print("Sorry! You are wrong :(")
        failed_attempts = failed_attempts + 1
    print(f"Attempts left: {10 - failed_attempts}")
    print(gallows[failed_attempts-1])
        
    correct_letters = 0
    print_word(word_to_guess, letters_used)
    print_letter(letters_used)

    if correct_letters == len(word_to_guess):
        print(f"Great! You won! The word is {word_to_guess}")
        break
else: 
    print("Sorry, you lost!")
    print(f"P.s. {word_to_guess}")
