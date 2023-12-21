const fs = require("fs");

var text = fs.readFileSync("./in.txt").toString();

var total = 0;
var copies = new Array(text.split("\r\n").length).fill(1);

for (let card in text.split("\r\n")) {
    let score = 0;
    let wins = text.split("\r\n")[card].replace(/\s+/g,' ').split(": ")[1].split(" | ")[0].split(" ");
    let nums = text.split("\r\n")[card].replace(/\s+/g,' ').split(": ")[1].split(" | ")[1].split(" ");
    for (let num of nums) {
        if (wins.includes(num)) {
            score++;
        }
    }
    for (let i = 1; i <= score; i++) {
        copies[i+Number(card)] = copies[i+Number(card)] + copies[Number(card)];
    }
}

for (card of copies) {
    total += card;
}
console.log(total);