# Mastermind

It is a puzzle game about guessing a secret code interactively throughout a finite number of rounds [1].

This repo contains a script capable of solving a round of a particular version of the Mastermind game. Given a secret code as a sequence of digits between 1 and 9, e.g. 1 7 9 3 7, and a guess respecting the same structure, e.g. 2 7 3 3 1, the solution is represented by a tuple (#strong, #weak), where 'strong' means correct digit in correct position and 'weak' means correct digit in wrong position. 

For the example above, the answer is (2, 1). In the given guess sequence, the first 7 and the second 3 are 'strong' guesses, and the last 1 is a 'weak' guess.

### Environment and Usage

The script requires only Python 3.12+.

It can be run as:

`python3 mastermind.py -s <secret_code> -g <guess>`

E.g.: `python3 mastermind.py -s 1,7,9,3,7 -g 2,7,3,3,1`

The inputs are comma separated natural numbers in the range [1, 9]; the inputs must have the same length (i.e. number of digits).

### Output

A tuple of integers as in (#strong, #weak) or None if an error occurs.

### References
[1] https://www.wikihow.com/Play-Mastermind
