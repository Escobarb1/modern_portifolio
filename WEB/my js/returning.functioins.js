// Dont do this


// var myVariables = 'I am at the global scope';

// var myFunction = function() {
//     console.log('me too!');
// }

// function one() {
//     return 'one';
// }

// let value = one();
// console.log(value);
// console.log(one());


// let value = one;
// console.log(typeof value);
// console.log(typeof one);
// console.log(value());


// datatypes!!!
// string
// number
// boolean
// underfined
// function


// function two() {
//     return function() {
//         console.log('two');
//     }
// }

// let myFunction = two();
// myFunction();



function three() {
    return function() {
        return 'three';
    }
}

console.log(three()());