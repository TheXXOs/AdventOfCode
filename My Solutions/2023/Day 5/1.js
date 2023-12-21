const fs = require("fs");

const text = fs.readFileSync("./in.txt").toString().split("\r\n\r\n");

const seeds = text[0].split(": ")[1].split(" ");
const maps = text.slice(1).map((z) => z.split("\r\n").slice(1).map((x) => x.split(" ").map((y) => Number(y))));
var output = -1;

for (let seed of seeds) {
    let value = Number(seed);
    for (let map of maps) {
        for (let line of map) {
            // line[0] is soil, line[1] is seed, line[2] is range
            if (value-line[1] >= 0 && value-line[1] < line[2]) {
                value = value + (line[0]-line[1]);
                break;
            }
        }
    }
    if (output == -1 || output > value) {
        output = value;
    }
}
console.log(output);