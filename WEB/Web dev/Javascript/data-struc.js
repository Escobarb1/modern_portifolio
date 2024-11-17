// The forEach() method

// const fruits = ['Mango', 'Apple', 'Kiwi', 'Pear'];
// function appendIndex(fruit, index) {
//     console.log(`${index}. ${fruit}`);
// }
// fruits.forEach(appendIndex);

// To explain the syntax, the forEach() method accepts a function that
//  will work on each array item. That function's first parameter is the 
//  current array item itself, and the second (optional) parameter is the index.

// const veggies = ['Onions', 'Garlic', 'Potato','Onions', 'Garlic', 'Potato','Onions', 'Garlic', 'Potato'];
// veggies.forEach( function(veggie, index) {
//     console.log(`${index}. ${veggie}`);
// })


// const familys = ['Stranger', 'Kelex-Evans', 'Escobar', 'Gooddy'];
// familys.forEach(function(family, index) {
//     console.log(`${index}: ${family}`);
// });




// The filter() method

// const nums = [0, 10, 20, 30, 40, 50];
// nums.filter(function(num){
//     return num > 20;
// })

// const nums = [0,10,20,30,40,50];
// nums.filter( function(num) {
//     return num > 20;
// })




// The map method

// [0,10,20,30,40,50].map( function(num) {
//     return num / 10
// })



// Working with Objects in JavaScript

// const result = [];
// const drone = {
//     speed : 100,
//     color : 'yellow'
// }

// const droneKeys = Object.keys(drone);
// droneKeys.forEach(function(key) {
//     result.push(key, drone[key])
// })
// console.log(result);




// Working with Maps in JavaScript


// let bestBoxers = new Map();
// bestBoxers.set(1, "The Champion");
// bestBoxers.set(2, "The Runner-up");
// bestBoxers.set(3, "The third place");

// bestBoxers.get(1); // 'The Champion'

// console.log(bestBoxers);


// Working with Sets in JavaScript

const repetitiveFruits = ['apple','pear','apple','pear','plum', 'apple'];
const uniqueFruits = new Set(repetitiveFruits);
console.log(uniqueFruits);