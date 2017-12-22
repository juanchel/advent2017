let fs = require('fs');
let _ = require('underscore');

let content = fs.readFileSync('input.txt', 'utf8');
let blocks = content.split(/\s+/).map(n => +n);
blocks.splice(-1, 1);

let seen = new Set();
let times = 0;

while(true) {
  let max = Math.max(...blocks);
  let maxIndex = _.findIndex(blocks, n => n === max);
  blocks[maxIndex] = 0;
  while(max > 0) {
    maxIndex++;
    if (maxIndex == blocks.length) {
      maxIndex = 0;
    }
    blocks[maxIndex]++;
    max--;
  }
  times++;
  let result = blocks.join(' ');
  if (seen.has(result)) {
    console.log(times);
    break;
  } else {
    seen.add(result);
  }
}
