# AoC Day 2 2020 - Adrenaline Rush
Today's challenge, for me, started off... hectic.

You see, I was told that I wasn't allowed to go on technology until after I'd done some exercise (this was 20-30 minutes before the challenge started).

So, I did! But I underestimated how long it would take - I was *literally* sprinting back home!

I got there with **ten seconds before the challenge started**. And since I was *running* to get back, I still... had a lot of adrenaline.
This meant that I was very frantic at doing the challenge.

*(**EDIT**, roughly 6 hours after the challenge: I have now joined my school's leaderboard.)*

## Explanation of the Challenge
The input I received is [here](https://github.com/TheXXOs/AdventOfCode/blob/main/My%20Solutions/2020/Day%202/input.txt).

### [Part One](https://adventofcode.com/2020/day/2)
Part One of today's challenge took a *long* list of 'passwords' and you had to find how many matched a specific criteria.

The passwords were of the format `#-# a: Password` where `#` are numbers and `a` is a letter.

The criteria for the first part of the challenge was to check if the `Password` had somewhere between `#` and `#` of the letter `a` in it.

You can see my code [here](https://github.com/TheXXOs/AdventOfCode/blob/main/My%20Solutions/2020/Day%202/2a.py), and my answer was `548`.

### [Part Two](https://adventofcode.com/2020/day/2#part2)
Part Two of today's challenge took the same list of passwords, but you had to filter them by a different criteria.

This time, you had to find if character #`#` **xor** character #`#` of `Password` had `a` in it.

Because it's **xor**, that means that *one and only one* of `#` and `#` could have `a` for it to be valid.

(Also, there's no index zero - the counting starts from 1.)

You can see my code [here](https://github.com/TheXXOs/AdventOfCode/blob/main/My%20Solutions/2020/Day%202/2b.py), and my answer was `502`.

## Positions on leaderboards
![r/xkcd: 2/6](https://img.shields.io/badge/r%2Fxkcd%20discord%20leaderboard-2/6-green)

![Worldwide: N/A](https://img.shields.io/badge/Worldwide%20leaderboard-N%2FA-red)

![School: 1/3](https://img.shields.io/badge/School%20leaderboard-1/3-brightgreen)