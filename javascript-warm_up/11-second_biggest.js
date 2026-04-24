#!/usr/bin/node
const argvArr = process.argv.slice(2);
if (argvArr.length <= 1) {
  console.log(0);
} else {
  argvArr.splice(argvArr.indexOf(Math.max(argvArr)), 1);
  console.log(Math.max(...argvArr));
}
