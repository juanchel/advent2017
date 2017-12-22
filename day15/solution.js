let valueA = 783;
let valueB = 325;
let matches = 0;

for (let numChecked = 0; numChecked < 40000000; numChecked++) {
  valueA *= 16807;
  valueA %= 2147483647;
  valueB *= 48271;
  valueB %= 2147483647;
  let rightA = valueA % 65536;
  let rightB = valueB % 65536;
  if (rightA === rightB) {
    matches++;
  }
}
console.log(matches);
