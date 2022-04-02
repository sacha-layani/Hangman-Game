#  Copyright (c) 2022
#
#  MIT License
#
#  Copyright (c) 2022 Sacha
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import RandomWord
import GameState

def __searchWord():
    """
    :return: Hide the Word
    """
    newWord = ""
    length = len(__GetWord)
    lengthNewWord = len(newWord)
    while lengthNewWord < length:
        newWord += "_"
        lengthNewWord += 1
    return newWord

__GetWord = RandomWord.RandomElement() # Secret Word


HideWord = __searchWord() # Hide Secret Word

usedLetters = [] # Letters which are not in the __GetWord variable

def __verify(letter, usedLetterList):
    """
    :param letter: The letter used by the user.
    :param usedLetterList: usedLetterList varibale
    :return: return True if letter is in the usedLetterList and False in other cases.
    """
    indice  = 0
    length = len(usedLetterList)
    while indice < length:
        if usedLetterList[indice] == letter:
            return True
        indice += 1
    return False

def getInput():
    """
    :return: returns the user's input
    """
    value = input("Please enter a letter : ")
    length = len(value)
    while (__verify(value, usedLetters)) or (length != 1 or not value.isalpha()) or value == value.upper():
        value = input("[Error : Repetition or incorect format ] Please enter a letter : ")
        length = len(value)
    else:
        return value



def DisplayHangman(usedLetterList:list = usedLetters):
    """
    :param usedLetterList: List with the letter which not in the word
    :param usedLetter: list
    :return: return the string representation of the Hangman
    """
    length = len(usedLetterList)
    print(GameState.status(length+1))


def ValidateLetter():
    """
    :return: Verify if the word contains the letter and replace the word in the function !
    """
    global HideWord
    global gameS
    value = getInput()
    notLetter = 0
    indice = 0
    for letter in __GetWord:
        if value == letter:
            HideWord = HideWord[:indice] + letter + HideWord[indice + 1:]
            notLetter +=1
        indice += 1
    if notLetter == 0:
        usedLetters.append(value)
    print(f"Not value in Hide Word : {usedLetters}")
    print(HideWord)
    return notLetter == 0

def EndScreen():
    """
    :return: EndScreen of the game : Win or Game Over
    """
    if HideWord != __GetWord:
        return f"Game Over. The hide word is : {__GetWord}"
    else:
        return f"{GameState.status(9)} \n You win"

def Game():
    """
    :return: Hangman Game compilation
    """
    attempts = 0
    while HideWord != __GetWord and attempts < 7:
        if ValidateLetter():
            attempts += 1
        DisplayHangman()

    return EndScreen()

print(Game())