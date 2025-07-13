#!/usr/bin/env node

const args = process.argv.slice(2);
const num = parseInt(args[0]);

is (isNaN(num)) {
  console.log("Not a number");
} else {
  console.log("My number is: " + num);
}