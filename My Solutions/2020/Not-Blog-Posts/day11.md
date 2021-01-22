# AoC Day 11 2020 - Deepcopying lists of lists
Today I learned that `newList = list(oldList)` only works if `oldList` doesn't contain lists or dicts;
you need to use `newList = copy.deepcopy(oldList)` if it does...

That's annoying!

P.S. Today's challenge is very Conway's-Game-of-Life-esque

## Explanation of the Challenge
The input I received is [here](https://github.com/TheXXOs/AdventOfCode/blob/main/My%20Solutions/2020/Day%2011/input.txt).

### [Part One](https://adventofcode.com/2020/day/11)
Part One required you to, from a grid of `.`s and `L`s, repeat these steps until the grid doesn't change:
- If it's a `L` and there are 0 `#`s adjacent (incl. diagonals), change to `#`
- If it's a `#` and there are at least 4 `#`s adjacent, change to `L`.

This took me a while due to the reason explained at the top, and a few other things that I'd missed.

You can see my code [here](https://github.com/TheXXOs/AdventOfCode/blob/main/My%20Solutions/2020/Day%2011/11a.py), and my answer was `2265`.

### [Part Two](https://adventofcode.com/2020/day/11#part2)
Part Two was doing the same things as Part One, but with 2 differences:
- Instead of adjacent `#`s, use the first `#` in the line of sight for each of the 8 directions
- Instead of at least 4 `#`s, it's at least 5 `#`s.

This took me... longer than expected.

You can see my code [here](https://github.com/TheXXOs/AdventOfCode/blob/main/My%20Solutions/2020/Day%2011/11b.py), and my answer was `2045`.

## Positions on leaderboards
![r/xkcd: 2/7](https://img.shields.io/badge/r%2Fxkcd%20discord%20leaderboard-2/7-green)

![Worldwide: 5194th](https://img.shields.io/badge/Worldwide%20leaderboard-5194-red)

![School: 1/5](https://img.shields.io/badge/School%20leaderboard-1/5-brightgreen)
