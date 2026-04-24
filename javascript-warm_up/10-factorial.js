#!/usr/bin/node
function factorial (n) {
  let result = 1;
  if (isNaN(n) || n === 1 || n === 0) {
    return 1;
  } else {
    result *= n;
    factorial(n - 1);
  }
  return result;
}

console.log(factorial(parseInt(process.argv[2], 10)));
