# AoC Day 8 2020 - A simple mistake...
Don't you *hate* it when you miss a single, simple, easy-to-overlook thing?

That's what happened today.

## Explanation of the Challenge
The input I received is [here](https://github.com/TheXXOs/AdventOfCode/blob/main/My%20Solutions/2020/Day%208/input.txt).

### [Part One](https://adventofcode.com/2020/day/8)
Part One I actually did *really* fast, it was just Part Two that I slipped up in.

Part One required you to take a list of computer instructions, which did:
 - `acc`: Increase/decrease a **variable** by (number)
 - `nop`: Do nothing
 - `jmp`: Increase/decrease the *instruction #* by (number)

You had to find the point at which it started an infinite loop, and find the value of the **variable** at that point.

You can see my code [here](https://github.com/TheXXOs/AdventOfCode/blob/main/My%20Solutions/2020/Day%208/8a.py), and my answer was `1709`.

### [Part Two](https://adventofcode.com/2020/day/8#part2)
Part Two was similar to Part One, except you had to change ***one*** `nop` to a `jmp` or vice versa,
and if it got to the end of the program successfully you had to output the value of the **variable**.

My issue, which took me at least 20 minutes to find, was that a part of my code *wasn't indented properly*, which matters in Python.

It meant that I wasn't getting *any* output, which was very confusing.

It was especially confusing because I edited my Part One code to be a function, so I thought that maybe that was the issue (it wasn't).

I eventually got it, but it took a while and some help from the same person as yesterday.

I've marked the line that was incorrectly indented in my code with a `# comment`.

You can see my code [here](https://github.com/TheXXOs/AdventOfCode/blob/main/My%20Solutions/2020/Day%208/8b.py), and my answer was `1976`.

## Positions on leaderboards
![r/xkcd: 2/7](https://img.shields.io/badge/r%2Fxkcd%20discord%20leaderboard-2/7-green)

![Worldwide: 5614th](https://img.shields.io/badge/Worldwide%20leaderboard-5614-red)

![School: 1/5](https://img.shields.io/badge/School%20leaderboard-1/5-brightgreen)
