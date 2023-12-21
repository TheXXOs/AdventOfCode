const fs = require("fs");

var text = fs.readFileSync("./in.txt").toString();

// Step 0: convert the file into a grid
var grid = text.split("\r\n");

// Step 1: find each number
var numLocs = [];
for (let y in grid) {
    let findingNum = false;
    let currentNum = new Array(3); // line, start, end
    for (let x in grid) {
        if (!isNaN(grid[y][x])) {
            if (!findingNum) {
                currentNum[0] = Number(y);
                currentNum[1] = Number(x);
                currentNum[2] = Number(x)+1;
                findingNum = true;
            } else {
                currentNum[2] = Number(x)+1;
            }
        } else if (findingNum) {
            numLocs.push(currentNum);
            currentNum = new Array(3);
            findingNum = false;
        }
    }
    if (findingNum) {
        numLocs.push(currentNum);
        currentNum = new Array(3);
        findingNum = false;
    }
}

// Step 2: Check surrounding squares
var total = 0;
for (let num of numLocs) {
    if (/[^\.\n\d]/.test((grid[num[0]-1] || "").substring(num[1]-1,num[2]+1)) // top + corners
        || /[^\.\n\d]/.test((grid[num[0]][num[1]-1]||"")) // left
        || /[^\.\n\d]/.test((grid[num[0]][num[2]]||"")) // right
        || /[^\.\n\d]/.test((grid[num[0]+1] || "").substring(num[1]-1,num[2]+1))) { // bottom + corners
        total += Number(grid[num[0]].substring(num[1],num[2]));
    }
}
console.log(total);