#!/usr/bin/env node
const args = process.argv.slice(2);
if (args.length < 2) {
    console.log(0);
} else {
    const numbers = args.map(Number);
    const max = Math.max(...numbers);
    const filteredNumbers = numbers.filter(num => num !== max);
    if (filteredNumbers.length === 0) {
        console.log(0);
    } else {
        const secondMax = Math.max(...filteredNumbers);
        console.log(secondMax);
    }
}
