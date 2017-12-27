
import random

def guessName(wordname):
    enteredChars = []
    guess = getGuessPatter(wordname)
    print(guess)
    maxChance = 5
    chance = 0
    while chance < maxChance:
        guessChar = input('Guess any character ').upper()
        if len(guessChar) == 1 and guessChar not in enteredChars:
            enteredChars.append(guessChar)
        else:
            print('You have already entered %s character '%guessChar)
            continue
        while len(guessChar) > 1 or len(guessChar) == 0:
            print('Enter single character !!')
            guessChar = input('Again guess the character ').upper()
        if wordname.find(guessChar) != -1:
            guess = replaceAllOccurences(guessChar, wordname, guess)
            print(guess)
        else:
            print('Character is not in the word ')
            chance = chance + 1

        if guess.find('*') == -1 and wordname.upper() == guess.upper():
            return True, chance+1
    return False, chance+1

def getGuessPatter(originalWord):
    strSplit = originalWord.split(" ")
    guess = ""
    for word in strSplit:
        strLen = len(word)
        guess = guess+" "+"*"*strLen
    return guess.strip()

def replaceAllOccurences(guessChar, originalWord, guessword):
    itr = 0
    strtolist = list(guessword)
    while itr < len(strtolist):
        if guessChar[0] == originalWord[itr]:
            strtolist[itr] = guessChar[0]
        itr = itr + 1

    return "".join(str(x) for x in strtolist)

def main():
    while True:
        wordList = ['North America','Europe','Africa','ASIA']
        randomIndex = random.randint(0, len(wordList)-1)
        guessRight, chance = guessName(wordList[randomIndex].upper())
        if guessRight:
            print('You were able to correctly guess the word in %d chance '%chance)
        else:
            print('You are out of chances. Play again!! ')
        gamecontinue = input('Want to play again? (yes/no) ')
        if(gamecontinue.upper() != 'YES'):
            break;
    print('Have a good day. Bye!! ')

if __name__ == "__main__":
    main()