const fs = require("fs");

var text = fs.readFileSync("./in.txt").toString();
var total = 0;

function thisNumChange(thisNum,value) {
    if (thisNum.length < 2) {
        thisNum += value;
    } else {
        thisNum = thisNum.slice(0,-1) + value;
    }
    return thisNum;
}


for (let line of text.split("\n")) {
    let thisNum = "";
    for (let char in line) {
        if (!isNaN(Number(line[char])) && !/\s/.test(line[char])) {
            thisNum = thisNumChange(thisNum,line[char]);
        } else {
            let subLine = line.slice(char);
            if (subLine.slice(0,3) == "one") {
                thisNum = thisNumChange(thisNum,"1");
            } else if (subLine.slice(0,3) == "two") {
                thisNum = thisNumChange(thisNum,"2");
            } else if (subLine.slice(0,5) == "three") {
                thisNum = thisNumChange(thisNum,"3");
            } else if (subLine.slice(0,4) == "four") {
                thisNum = thisNumChange(thisNum,"4");
            } else if (subLine.slice(0,4) == "five") {
                thisNum = thisNumChange(thisNum,"5");
            } else if (subLine.slice(0,3) == "six") {
                thisNum = thisNumChange(thisNum,"6");
            } else if (subLine.slice(0,5) == "seven") {
                thisNum = thisNumChange(thisNum,"7");
            } else if (subLine.slice(0,5) == "eight") {
                thisNum = thisNumChange(thisNum,"8");
            } else if (subLine.slice(0,4) == "nine") {
                thisNum = thisNumChange(thisNum,"9");
            }
        }
    }
    if (thisNum.length == 1) {
        thisNum += thisNum;
    }
    total += Number(thisNum);
}
console.log(total);