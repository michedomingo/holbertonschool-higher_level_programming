#!/usr/bin/node
function factorial (arg) {
  if (isNaN(arg)) {
    return (1);
  } else if (arg === 0) {
    return (1);
  } else {
    return (arg * factorial(arg - 1));
  }
}
let input = process.argv[2];
input = parseInt(input);
console.log(factorial(input));
