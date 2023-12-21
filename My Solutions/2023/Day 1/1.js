const fs = require("fs");

var text = fs.readFileSync("./in.txt").toString();
var total = 0;
for (let line of text.split("\n")) {
    let thisNum = "";
    for (let char of line) {
        if (!isNaN(Number(char)) && !/\s/.test(char)) {
            if (thisNum.length < 2) {
                thisNum += char;
            } else {
                thisNum = thisNum.slice(0,-1) + char;
            }
        }
    }
    if (thisNum.length == 1) {
        thisNum += thisNum;
    }
    total += Number(thisNum);
}
console.log(total);