# AoC Day 5 2020 - I'm Hair!
Today's the first day where nothing weird happened pre-challenge!

Well... not really.

You see, I had to have a haircut before the challenge, so I'm going to go have a shower after this.

But, finally, a day where I wasn't stressed  about missing out on doing the challenge!

## Explanation of the Challenge
The input I received is [here](https://github.com/TheXXOs/AdventOfCode/blob/main/My%20Solutions/2020/Day%205/input.txt).

### [Part One](https://adventofcode.com/2020/day/5)
The challenge involved finding a location in a 128-by-8 map through directions.

`F` and `B` mean "take the front-or-back half only", and `L` and `R` are the same but for, well, left-to-right.

You get a string of Fs and Bs which dictate a specific row, and Ls and Rs which dictate a specific column.

I... haven't really explained it too well, so maybe go look at the actual explanation.

ANYWAY, with each row-and-column for locations, you had to find the "ID" of that location,
through the formula `row * 8 + column = ID`.

The challenge was finding the *highest* ID in the list of directions.

You can see my code [here](https://github.com/TheXXOs/AdventOfCode/blob/main/My%20Solutions/2020/Day%205/5a.py), and my answer was `944`.

### [Part Two](https://adventofcode.com/2020/day/5#part2)
Part Two took the answers from Part One, and made you find the *missing* one.

However, you had to disregard the first and last 100 or so (because of whatever reason).

That wasn't too challenging, if you have all the IDs.

You can see my code [here](https://github.com/TheXXOs/AdventOfCode/blob/main/My%20Solutions/2020/Day%205/5b.py), and my answer was `554`.

## Positions on leaderboards
![r/xkcd: 2/7](https://img.shields.io/badge/r%2Fxkcd%20discord%20leaderboard-2/7-green)

![Worldwide: 1770th](https://img.shields.io/badge/Worldwide%20leaderboard-1770-red)

![School: 1/5](https://img.shields.io/badge/School%20leaderboard-1/5-brightgreen)
