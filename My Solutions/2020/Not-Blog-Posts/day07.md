# AoC Day 7 2020 - I hate Recursion
Today's challenge was... horrible.

*(By that, I mean I did horribly.)*

I have *never* done anything with recursion before, so I guess it's understandable?

## Explanation of the Challenge
The input I received is [here](https://github.com/TheXXOs/AdventOfCode/blob/main/My%20Solutions/2020/Day%207/input.txt).

### [Part One](https://adventofcode.com/2020/day/7)
The first part of the challenge was to, from a list of "instructions" on which bags can hold which bags,
find how many different bags can hold a `shiny gold` bag.

This took me *forever*, because I had no understanding of recursion in Python until now.

I finally realised that you could just call `functionX()` from *inside* `functionX()`, but that took me way too long to figure out.

Thanks to **Flumble** from the r/xkcd discord for helping me out!

You can see my code [here](https://github.com/TheXXOs/AdventOfCode/blob/main/My%20Solutions/2020/Day%207/7a.py), and my answer was `101`.

### [Part Two](https://adventofcode.com/2020/day/7#part2)
Part Two wasn't too easy either.

You had to find out how many individual bags maximum the `shiny gold` bag had to hold.

First, I had to restructure the first half of my code (which was converting the `input.txt` to a dictionary)
so that it involved the *number* of required bags.

Then, I actually had to do the recursion.

You can see my code [here](https://github.com/TheXXOs/AdventOfCode/blob/main/My%20Solutions/2020/Day%207/7b.py), and my answer was `108636`.

All in all, both parts took me **one hour and fourty-seven minutes**,
although surprisingly I haven't moved any places on any private leaderboards.

## Positions on leaderboards
![r/xkcd: 2/7](https://img.shields.io/badge/r%2Fxkcd%20discord%20leaderboard-2/7-green)

![Worldwide: 5933th](https://img.shields.io/badge/Worldwide%20leaderboard-5933-red)

![School: 1/5](https://img.shields.io/badge/School%20leaderboard-1/5-brightgreen)
