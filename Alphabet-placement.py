#!/usr/bin/env python3
# Created By: Emmanuella Taiwo
# created on 2nd nov, 2026
# This program asks the user for an alphabet letter as a string
# and displays if it is a vowel , a consonant or both and catches errors


def main():
    # this function checks if the alphabet is a vowel or consonant
    # input
    alphabet = input("Enter an alphabet: ")
    vowel = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
    consonant = {"b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
                  "n", "p", "q", "r", "s", "t", "v", "w", "x", "z" ,
                    "B", "C", "D", "F", "G", "H", "J", "K", "L", "M",
                    "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"}
    vowel_and_consonant = {"y", "Y"}
        #if the alphabet is a digit, display an error message
    if alphabet.isdigit():
        print("{alphabet} is not a valid alphabet. Enter a valid alphabet.".format(alphabet=alphabet))


        # process and output
        # set the alphabet as a string
    try:
        alphabet = str(alphabet)
                # check if the alphabet is a vowel or consonant
        if alphabet in vowel and alphabet not in consonant:
            print("{alphabet} is a vowel.".format(alphabet=str(alphabet)))
        elif alphabet in consonant and alphabet not in vowel:
            print("{alphabet} is a consonant.".format(alphabet=str(alphabet)))
        elif alphabet in vowel_and_consonant:
            print("{alphabet} is both a vowel and a consonant.".format(alphabet=str(alphabet)))
    except Exception:
        print("{alphabet} is not a valid alphabet. Enter a valid alphabet.".format(alphabet=alphabet))


if __name__ == "__main__":
    main()
