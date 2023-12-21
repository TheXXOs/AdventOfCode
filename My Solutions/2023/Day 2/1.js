const fs = require("fs");

var text = fs.readFileSync("./in.txt").toString();
var total = 0;
var roundID = 1;
for (let line of text.split("\n")) {
    let maxes = {"red":0,"green":0,"blue":0};
    for (let round of line.split(": ")[1].trim().split("; ")) {
        for (let chips of round.split(", ")) {
            if (maxes[chips.split(" ")[1]] < Number(chips.split(" ")[0])) {
                maxes[chips.split(" ")[1]] = Number(chips.split(" ")[0]);
            }
        }
    }
    if (maxes.red <= 12 && maxes.green <= 13 && maxes.blue <= 14) {
        total += roundID;
    }
    roundID++;
}
console.log(total);