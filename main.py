import random
from rich.console import Console
from string import ascii_letters, ascii_uppercase

console = Console(width=70, highlight=True)

NUM_LETTERS = 5
NUM_GUESSES = 6
FILE_NAME = 'wordlist.txt'

def main():
    word = getWord()
    counter = 1
    guesses = ['_'* NUM_LETTERS] * NUM_GUESSES
    guessed = False
    while not guessed and counter <= NUM_GUESSES:
        refresh_page(f'Guess {counter}')
        showGuesses(guesses, word)
        guesses[counter-1] = input('Guess word: ').upper()
        valid = check_guess(guesses[counter-1])
        while not valid:
            guesses[counter-1] = input(f'Guess word: ').upper()
            valid = check_guess(guesses[counter - 1])
        if guesses[counter-1] == word:
            guessed = True
        counter += 1
    game_over(guesses, word, guessed)


def showGuesses(guesses, word):
    letter_status = {letter: letter for letter in ascii_uppercase}
    for guess in guesses:
        styled_guess = []
        for letter, correct in zip(guess, word):
            if letter == correct:
                style = 'bold #FFFFFF on #008000'
            elif letter in word:
                style = 'bold #FFFFFF on #dbac15'
            elif letter in ascii_letters:
                style = '#FFFFFF on #666666'
            else:
                style = 'dim'
            styled_guess.append(f'[{style}]{letter}[/]')
            if letter != '_':
                letter_status[letter] = f'[{style}]{letter}[/]'
        console.print(''.join(styled_guess), justify= 'center')
    console.print(''.join(letter_status.values()), justify = 'center')

def getWord():
    file = open(FILE_NAME, 'r')
    word = file.readline().strip().upper()
    wordlist = []
    while word != '':
        wordlist.append(word)
        word = file.readline().strip().upper()

    word = random.choice(wordlist)
    return word


def game_over(guesses, word, guessed_correctly):
    refresh_page('Game Over')
    showGuesses(guesses, word)
    if guessed_correctly:
        console.print(f'\n[bold #FFFFFF on #008000]Correct! The word is {word}[/]')
    else:
        console.print(f'\n[bold #FFFFFF on red]GAME OVER! The word was {word}[/]')

def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue]:leafy_green: {headline} :leafy_green:[/]\n")

def check_guess(guess):
    returnValue = True
    if len(guess) != 5:
        console.print('[#ffffff on red]Your guess has to be[/][bold #00ffff on red] 5 [/][#ffffff on red]letters long[/]')
        returnValue = False
    else:
        for letter in guess:
            if letter not in ascii_letters:
                console.print(f'[#ffffff on red]{letter} is not a valid letter. Please use the english lexicon only[/]')
                returnValue = False
    return returnValue

main()