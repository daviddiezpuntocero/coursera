#!/usr/bin/env node
function isPrime(number) {
    var s = Math.floor(Math.sqrt(number));
    var found = true;
    // console.log("number = " + number + ", s = " + s);
    for(var j = 1; j <= s; j++) {
        // console.log("number =" + number + ", j = " + j + ", number%j = " + number%j);
        if (number%j == 0 && 1 != j) {
            found = true;
            break;
        } else if (j == s) {
            found = false;
        }
    }
    return !found;
}

function convertArrayToStr(arr) {
    var outstr= arr[0];
    for(var i = 1; i < arr.length; i ++) {
        outstr += "," + arr[i];
    }
    return outstr;
}

var fs = require('fs');
var outfile = "prime.txt";
var primes = [];
for (var i = 2; ; i++) {
    if( isPrime(i) ){
        primes.push(i);
    }
    if (primes.length >= 100) {
        break;
    }
}

var outstr = convertArrayToStr(primes);
fs.writeFileSync(outfile, outstr);
console.log("Script: " + __filename + "\n Wrote: [" +　outstr + "] To: " + outfile);
