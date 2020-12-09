# AoC Day 9 2020 - [Read the ~~clue~~ *question*](https://www.theloop.ca/the-amazing-race-teams-seriously-need-to-read-the-clues-if-they-want-to-stay-in-this-thing/)
Wow, I *love* taking *forever* on Part Two of stuff! (sarcastic sarcasm)

## Explanation of the Challenge
The input I received is [here](https://github.com/TheXXOs/AdventOfCode/blob/main/My%20Solutions/2020/Day%209/input.txt).

### [Part One](https://adventofcode.com/2020/day/9)
Part One required you to, from a list of numbers, find *one* that didn't fit the following criteria:

**After the first 25 numbers, each number you receive should be the sum of any two of the 25 immediately previous numbers.**

This didn't take me too long.

You can see my code [here](https://github.com/TheXXOs/AdventOfCode/blob/main/My%20Solutions/2020/Day%209/9a.py), and my answer was `21806024`.

### [Part Two](https://adventofcode.com/2020/day/9#part2)
Once you'd found the number in Part One, Part Two required you to find a consecutive string of numbers in the list (of length 2 or more) that added up to the invalid number.

From that list, you had to add together the **highest and lowest** numbers, which was your answer.

I messed up here, because I was adding together the *first and last* numbers in the list, not the *highest and lowest*.

It took me a while to figure it out, and I only did when I looked at the question again.

(Seriously, I watch the Amazing Race and I didn't read the question?)

You can see my code [here](https://github.com/TheXXOs/AdventOfCode/blob/main/My%20Solutions/2020/Day%209/9b.py), and my answer was `2986195`.

## Positions on leaderboards
![r/xkcd: 2/7](https://img.shields.io/badge/r%2Fxkcd%20discord%20leaderboard-2/7-green)

![Worldwide: 6791st](https://img.shields.io/badge/Worldwide%20leaderboard-6791-red)

![School: 1/5](https://img.shields.io/badge/School%20leaderboard-1/5-brightgreen)
