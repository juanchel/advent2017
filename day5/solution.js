let fs = require('fs');

let contents = fs.readFileSync('input.txt', 'utf8');
let lines = contents.split('\n').map(n => +n);
lines.splice(-1, 1);

let curIndex = 0;
let jumps = 0;

while (curIndex < lines.length) {
  let newIndex = curIndex + lines[curIndex];
  lines[curIndex]++;
  curIndex = newIndex;
  jumps++;
}

console.log(jumps);
