# AoC Day 3 2020 - Late Start
I was a *bit* late to the start of the challenge (by ~20 minutes) because of a family thing that I had to do.

However, surprisingly, I still managed to hold my 1st on the school leaderboard *and* my 2nd on the r/xkcd leaderboard. Wow!

## Explanation of the Challenge
The input I received is [here](https://github.com/TheXXOs/AdventOfCode/blob/main/My%20Solutions/2020/Day%203/input.txt).

### [Part One](https://adventofcode.com/2020/day/3)
Part One of today's challenge took a random-ish grid of `.`s and `#`s, and from it you had to find, if you moved **three right and one down** each time, starting from the top left position, how many `#`s would you run into?

This was further complicated by the fact that it wraps horizontally, but that's nothing that the modulo operand can't handle.

You can see my code [here](https://github.com/TheXXOs/AdventOfCode/blob/main/My%20Solutions/2020/Day%203/3a.py), and my answer was `228`.

### [Part Two](https://adventofcode.com/2020/day/3#part2)
Part Two of today's challenge was the same as Part 1, but you had to find the product of the number of `#`s you'd cross with the following patterns:

 - 1 down, 1 across
 - 1 down, 3 across
 - 1 down, 5 across
 - 1 down, 7 across
 - 2 down, 1 across

This did complicate things a bit, but I just used Ctrl+C Ctrl+V to sort it out. I later realised that I could have used functions.

You can see my code [here](https://github.com/TheXXOs/AdventOfCode/blob/main/My%20Solutions/2020/Day%203/3b.py), and my answer was `6818112000`.

I later made a better version of Part Two that uses *functions* instead of copy+pasting [here](https://github.com/TheXXOs/AdventOfCode/blob/main/My%20Solutions/2020/Day%203/3bETTER.py).

## Positions on leaderboards
![r/xkcd: 2/6](https://img.shields.io/badge/r%2Fxkcd%20discord%20leaderboard-2/6-green)

![Worldwide: 6968th](https://img.shields.io/badge/Worldwide%20leaderboard-6968-red)

![School: 1/4](https://img.shields.io/badge/School%20leaderboard-1/4-brightgreen)
