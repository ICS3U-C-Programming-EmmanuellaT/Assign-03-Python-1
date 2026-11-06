#!/usr/bin/env python3
# Created By: Emmanuella Taiwo
# created on 6th November, 2026
# This program asks the user for three numbers and displays the smallest number and catches errors


def main():
    # this function checks if the number is a positive number
    # input
    first_number_as_string = input("Enter the first number: ")
    second_number_as_string = input("Enter the second number: ")
    third_number_as_string = input("Enter the third number: ")

    print(
        "The first number is {first_number}, the second number is {second_number} and the third number is {third_number}".format(
            first_number=first_number_as_string,
            second_number=second_number_as_string,
            third_number=third_number_as_string,
        )
    )

    # process & output
    try:
        first_number_as_integer = int(first_number_as_string)
        second_number_as_integer = int(second_number_as_string)
        third_number_as_integer = int(third_number_as_string)

        # find the smallest number among the three numbers
        smallest_number = min(
            first_number_as_integer, second_number_as_integer, third_number_as_integer
        )
        if (
            first_number_as_integer
            == second_number_as_integer
            == third_number_as_integer
        ):
            print(
                "{first_number}, {second_number} and {third_number} are the same numbers".format(
                    first_number=first_number_as_integer,
                    second_number=second_number_as_integer,
                    third_number=third_number_as_integer,
                )
            )
        else:
            print(
                "The smallest number among {first_number}, {second_number} and {third_number} is {smallest_number}".format(
                    first_number=first_number_as_integer,
                    second_number=second_number_as_integer,
                    third_number=third_number_as_integer,
                    smallest_number=smallest_number,
                )
            )
    except Exception:
        print(
            "One or more of the numbers entered are not valid integers, please enter valid integers"
        )


if __name__ == "__main__":
    main()
