# AoC Day 10 2020 - Brute-forcing is dumb
Hey, it's another day where I do really well in Part One but horribly in Part Two!

## Explanation of the Challenge
The input I received is [here](https://github.com/TheXXOs/AdventOfCode/blob/main/My%20Solutions/2020/Day%2010/input.txt).

### [Part One](https://adventofcode.com/2020/day/10)
Part One of today's challenge required you to find, in a list of numbers (if ordered from smallest to largest), how many one-sized gaps and how many three-sized gaps there were.

The answer could be found by multiplying them together.

You can see my code [here](https://github.com/TheXXOs/AdventOfCode/blob/main/My%20Solutions/2020/Day%2010/10a.py), and my answer was `1876`.

### [Part Two](https://adventofcode.com/2020/day/10#part2)
Part Two was, once again, *harder*.

You had to find how many ways you could get from 0 to 3 more than the highest number in the list, using *only* jumps of 3 or lower.

This took me a while, because initially I was brute-forcing it, but I was talked out of doing that by **the same person who has been helping me a lot**.

So, I eventually made it so that it works backwards - it counts how many ways the final number can get to the final number,
then how many ways the second-final number can, and so on.

The trick is that if it comes across a number that has already been solved for, it will just add that number's number of ways! It's much more efficient.

You can see my code [here](https://github.com/TheXXOs/AdventOfCode/blob/main/My%20Solutions/2020/Day%2010/10b.py), and my answer was `14173478093824`.

## Positions on leaderboards
![r/xkcd: 2/7](https://img.shields.io/badge/r%2Fxkcd%20discord%20leaderboard-2/7-green)

![Worldwide: 4778th](https://img.shields.io/badge/Worldwide%20leaderboard-4778-red)

![School: 1/5](https://img.shields.io/badge/School%20leaderboard-1/5-brightgreen)
