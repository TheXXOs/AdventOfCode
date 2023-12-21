const fs = require("fs");

var text = fs.readFileSync("./in.txt").toString();

var total = 0;
for (let card of text.split("\r\n")) {
    let score = 0;
    let wins = card.replace(/\s+/g,' ').split(": ")[1].split(" | ")[0].split(" ");
    let nums = card.replace(/\s+/g,' ').split(": ")[1].split(" | ")[1].split(" ");
    for (let num of nums) {
        if (wins.includes(num)) {
            if (score == 0) { score = 1; }
            else { score *= 2; }
        }
    }
    total += score;
}
console.log(total);