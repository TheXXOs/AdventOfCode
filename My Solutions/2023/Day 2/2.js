const fs = require("fs");

var text = fs.readFileSync("./in.txt").toString();
var total = 0;
for (let line of text.split("\n")) {
    let maxes = {"red":0,"green":0,"blue":0};
    for (let round of line.split(": ")[1].trim().split("; ")) {
        for (let chips of round.split(", ")) {
            if (maxes[chips.split(" ")[1]] < Number(chips.split(" ")[0])) {
                maxes[chips.split(" ")[1]] = Number(chips.split(" ")[0]);
            }
        }
    }
    total += (maxes.red * maxes.green * maxes.blue);
}
console.log(total);