let valueA = 783;
let valueB = 325;
let matches = 0;

for (let numChecked = 0; numChecked < 5000000; numChecked++) {
  while(true) {
    valueA *= 16807;
    valueA %= 2147483647;
    if (valueA % 4 === 0) {
      break;
    }
  }
  while(true) {
    valueB *= 48271;
    valueB %= 2147483647;
    if (valueB % 8 === 0) {
      break;
    }
  }

  let rightA = valueA % 65536;
  let rightB = valueB % 65536;
  if (rightA === rightB) {
    matches++;
  }
}
console.log(matches);
