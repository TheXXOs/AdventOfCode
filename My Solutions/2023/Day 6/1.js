const fs = require("fs");

var text = fs.readFileSync("./in.txt").toString();

var times = text.split("\r\n")[0].replace(/\s+/g,' ').split(": ")[1].split(" ");
var dists = text.split("\r\n")[1].replace(/\s+/g,' ').split(": ")[1].split(" ");

var total = 1;

for (race in times) {
    let wins = 0;
    let time = times[race];
    let dist = dists[race];
    for (let i = 0; i <= time; i++) {
        if ((time-i)*i > dist) {
            wins++;
        }
    }
    total *= wins;
}
console.log(total);