#!/usr/bin/env python3

"""Documentation of module mastermind.py.

This module provides functions to solve a round of the Mastermind game. Given a
secret code as a sequence of integers between 1 and 9, e.g. 1 7 9 3 7, and a
guess respecting the same structure, e.g. 2 7 3 3 1, the solution is
represented by a tuple (#strong, #weak), where 'strong' means correct digit in
correct position and 'weak' means correct digit in wrong position. For the
example above, the answer is (2, 1). In the guess sequence, the first seven and
the second three are 'strong' guesses, and the last one is a 'weak' guess.

Functions
---------
    - solve(secret_code: list[int], guess: list[int]) -> tuple[int, int]
    - get_strong_count(pairs: list[tuple[int, int]]) -> int
    - convert_to_binary(value: int) -> int
    - get_weak_count(pairs: list[tuple[int, int]]) -> int
    - is_invalid(sequence: list[int]) -> bool
    - is_valid_range(sequence: list[int]) -> bool
    - is_list_of_int(sequence: list[int]) -> bool
    - convert_to_list_of_ints(argument: str) -> list[int]
"""

from argparse import ArgumentParser
from typing import Union


SECRET_IDX: int = 0
GUESS_IDX: int = 1


def solve(secret_code: list[int], guess: list[int]) -> tuple[int, int]:
    """Solve a round (i.e. a guess atempt) of the mastermind game.

    Parameters
    ----------
        - secret_code: list[int] \\
            A sequence of integer numbers stored as a list.
        - guess: list[int] \\
            A sequence of integer numbers stored as a list.
    """
    if (is_invalid(secret_code) or is_invalid(guess)
            or (len(secret_code) != len(guess))):
        return (0, 0)

    pairs = list(zip(secret_code, guess))
    return (get_strong_count(pairs), get_weak_count(pairs))


def get_strong_count(pairs: list[tuple[int, int]]) -> int:
    """Get the count of correct digits in correct positions.

    Parameters
    ----------
        - pairs: list[tuple[int, int]] \\
            A sequence of tuples of integer numbers stored as a list.
    """
    return sum([convert_to_binary(pair[0]-pair[1]) for pair in pairs])


def convert_to_binary(value: int) -> int:
    """ Convert value either to 0 or 1.

    Conversion rule: if value == 0, return 1; otherwise, return 0.
    """
    if value == 0:
        return 1
    return 0


def get_weak_count(pairs: list[tuple[int, int]]) -> int:
    """Get the count of correct digits in wrong positions.

    Parameters
    ----------
        - pairs: list[tuple[int, int]] \\
            A sequence of tuples of integer numbers stored as a list.
    """
    filtered_pairs: list = [
        pair for pair in pairs if pair[SECRET_IDX] != pair[GUESS_IDX]
    ]

    secret_values: list = []
    guess_values: list = []
    for pair in filtered_pairs:
        secret_values.append(pair[SECRET_IDX])
        guess_values.append(pair[GUESS_IDX])

    return int(
        sum(
            [digit/digit for digit in set(guess_values)
                if digit in set(secret_values)]
        )
    )


def is_invalid(sequence: list[int]) -> bool:
    """Return True if sequence is invalid; False otherwise.

    A sequence is invalid if (a) it is not a list of ints or (b) it's entries
    are not in the accepted integer range [1, 9].

    Parameters
    ----------
        - sequence: list[int] \\
            A sequence of integer numbers stored as a list.
    """
    return (not is_list_of_int(sequence)) or (not is_valid_range(sequence))


def is_valid_range(sequence: list[int]) -> bool:
    """Return True if sequence is valid; False otherwise.

    Valid sequences contain digits inside the integer range [1, 9].

    Parameters
    ----------
        - sequence: list[int] \\
            A sequence of integer numbers stored as a list.
    """
    return all((1 <= entry <= 9) for entry in set(sequence))


def is_list_of_int(sequence: list[int]) -> bool:
    """Return True if sequence is a list of ints; False otherwise.

    Parameters
    ----------
        - sequence: list[int] \\
            A sequence of integer numbers stored as a list.
    """
    return isinstance(sequence, list) and \
        all([isinstance(entry, int) for entry in sequence])


def convert_to_list_of_ints(argument: str) -> list[int]:
    """Convert a string to a list of integers.

    The string must be a comma separated list of integers as in "1,2,3,4,5".
    """
    return list(map(int, argument.split(',')))


def main() -> Union[None, tuple[int, int]]:
    """Run the script in full."""
    parser = ArgumentParser(
        prog='MasterMind',
        description='Solves a round (i.e. an atempt) of the MasterMind game.',
    )
    parser.add_argument(
        '-s',
        '--secret_code',
        type=convert_to_list_of_ints,
        required=True,
    )
    parser.add_argument(
        '-g',
        '--guess',
        type=convert_to_list_of_ints,
        required=True,
    )

    try:
        args = parser.parse_args()
    except SystemExit:
        print(
            "Please use only integers between 1 and 9 (both inclusive), as "
            "in 2,5,4,4,9,3."
        )
        return None
    else:
        return solve(args.secret_code, args.guess)


if __name__ == '__main__':
    print(f"Result: {main()}.")
