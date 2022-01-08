"""
Muhammad Shahmil Shahidan
Program that spell a number requested.
Number range is from 0 to 99999
"""


# Case 1: For single digits
def ones(number):
    if number == '0':
        return 'zero'
    elif number == '1':
        return 'one'
    elif number == '2':
        return 'two'
    elif number == '3':
        return 'three'
    elif number == '4':
        return 'four'
    elif number == '5':
        return 'five'
    elif number == '6':
        return 'six'
    elif number == '7':
        return 'seven'
    elif number == '8':
        return 'eight'
    elif number == '9':
        return 'nine'

# Case 2: For two digits(20+) and above
def ones_mul(number):
    if number == '1':
        return 'one'
    elif number == '2':
        return 'two'
    elif number == '3':
        return 'three'
    elif number == '4':
        return 'four'
    elif number == '5':
        return 'five'
    elif number == '6':
        return 'six'
    elif number == '7':
        return 'seven'
    elif number == '8':
        return 'eight'
    elif number == '9':
        return 'nine'

def tens(number):
    if number[0] == '2':
        return 'twenty'
    elif number[0] == '3':
        return 'thirty'
    elif number[0] == '4':
        return 'forty'
    elif number[0] == '5':
        return 'fifty'
    elif number[0] == '6':
        return 'sixty'
    elif number[0] == '7':
        return 'seventy'
    elif number[0] == '8':
        return 'eighty'
    elif number[0] == '9':
        return 'ninety'

def teens(number):
    # If number in ones is 0, set to ten
    if number[-1] == '0':
        return 'ten'
    # Check for teens (11 - 19)
    if number[-1] == '1':
        return 'eleven'
    elif number[-1] == '2':
        return 'twelve'
    elif number[-1] == '3':
        return 'thirteen'
    elif number[-1] == '4':
        return 'fourteen'
    elif number[-1] == '5':
        return 'fifteen'
    elif number[-1] == '6':
        return 'sixteen'
    elif number[-1] == '7':
        return 'seventeen'
    elif number[-1] == '8':
        return 'eighteen'
    elif number[-1] == '9':
        return 'ninteen'


def hundreds(number):
    if number == '1':
        return 'one hundred'
    elif number == '2':
        return 'two hundred'
    elif number == '3':
        return 'three hundred'
    elif number == '4':
        return 'four hundred'
    elif number == '5':
        return 'five hundred'
    elif number == '6':
        return 'six hundred'
    elif number == '7':
        return 'seven hundred'
    elif number == '8':
        return 'eight hundred'
    elif number == '9':
        return 'nine hundred'


def thousands(number):
    if number == '1':
        return 'one thousand'
    elif number == '2':
        return 'two thousand'
    elif number == '3':
        return 'three thousand'
    elif number == '4':
        return 'four thousand'
    elif number == '5':
        return 'five thousand'
    elif number == '6':
        return 'six thousand'
    elif number == '7':
        return 'seven thousand'
    elif number == '8':
        return 'eight thousand'
    elif number == '9':
        return 'nine thousand'


def ten_thousands(number):
    if number == '1':
        return 'ten'
    elif number == '2':
        return 'twenty'
    elif number == '3':
        return 'thirty'
    elif number == '4':
        return 'forty'
    elif number == '5':
        return 'fifty'
    elif number == '6':
        return 'sixty'
    elif number == '7':
        return 'seventy'
    elif number == '8':
        return 'eighty'
    elif number == '9':
        return 'ninety'


def spellNum(n):
    n = str(n)
    word_number = ""
    num_digits = len(str(n))
    # Single digit case
    if num_digits == 1:
            # If input is single digit
            if word_number == '':
                word_number = ones(n[-num_digits])
                return word_number
    while num_digits > 1:
        if num_digits == 5:
            if n[-num_digits] != '0':
                word = ten_thousands(n[-num_digits])
                word_number += word
                word_number += " "
            else:
                pass
        elif num_digits == 4:
            if n[-num_digits] != '0':
                word = thousands(n[-num_digits])
                word_number += word
                word_number += " "
            else:
                word_number += "thousand"
                word_number += " "
        elif num_digits == 3:
            if n[-num_digits] != '0':
                word = hundreds(n[-num_digits])
                word_number += word
                word_number += " "
            else:
                pass
        elif num_digits == 2:
            if n[-num_digits] == '0':
                pass
            elif n[-num_digits] == '1':
                word = teens(n[-num_digits:])
                word_number += word
                return word_number
            # Double digits case
            else:
                word = tens(n[-num_digits:])
                word_number += word
                word_number += " "
        num_digits -= 1
    if n[-num_digits] != '0':
        word = ones_mul(n[-num_digits])
        word_number += word
    word_number = word_number.rstrip(' ')
    return word_number
