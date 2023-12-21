const fs = require("fs");

var text = fs.readFileSync("./in.txt").toString();

function findNumber(grid, y, x) {
    let findingLeft = true;
    let leftCount = 1;
    while (findingLeft) {
        if (isNaN(grid[y][x-leftCount])) {
            findingLeft = false;
            leftCount = x-leftCount+1;
        } else {
            leftCount++;
        }
    }
    let findingRight = true;
    let rightCount = 1;
    while (findingRight) {
        if (isNaN(grid[y][x+rightCount])) {
            findingRight = false;
            rightCount = x+rightCount;
        } else {
            rightCount++;
        }
    }
    return Number(grid[y].substring(leftCount,rightCount));
}

// Step 0: convert the file into a grid
var grid = text.split("\r\n");

// Step 1: find each gear
var gearLocs = [];
for (let y in grid) {
    for (let x in grid) {
        if (grid[y][x] == "*") {
            gearLocs.push([Number(y),Number(x)]);
        }
    }
}

// Step 2: Check valid gears
var total = 0;
for (let gear of gearLocs) {
    adjs = [
        [grid[gear[0]-1][gear[1]-1],grid[gear[0]-1][gear[1]],grid[gear[0]-1][gear[1]+1]],
        [grid[gear[0]][gear[1]-1]],                         [grid[gear[0]][gear[1]+1]],
        [grid[gear[0]+1][gear[1]-1],grid[gear[0]+1][gear[1]],grid[gear[0]+1][gear[1]+1]]
    ];
    boolAdjs = adjs.map(x => x.map(x2 => !isNaN(x2))).map((x) => x = x.filter((val,ind) => (val != x[ind+1] || val == false)))
    if (boolAdjs.flat(1).filter((x) => x).length == 2) { // gear only has two connected values
        let ratio = 1;
        for (let sq in boolAdjs[0]) { // top
            if (boolAdjs[0][sq]) {
                ratio *= findNumber(grid,gear[0]-1,gear[1]-1+Number(sq));
            }
        }
        for (let sq in boolAdjs[3]) { // bottom
            if (boolAdjs[3][sq]) {
                ratio *= findNumber(grid,gear[0]+1,gear[1]-1+Number(sq));
            }
        }
        if (boolAdjs[1][0]) {
            ratio *= findNumber(grid,gear[0],gear[1]-1);
        }
        if (boolAdjs[2][0]) {
            ratio *= findNumber(grid,gear[0],gear[1]+1);
        }
        total += ratio;
    }
}
console.log(total);
