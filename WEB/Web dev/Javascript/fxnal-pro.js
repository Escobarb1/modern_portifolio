// functional programming

// var currencyOne = 100;
// var currencyTwo = 0;
// var exchangeRate = 1.2;

// function converCurrent(amount, rate) {
//     return amount * rate;
// }

// currencyTwo  = converCurrent(currencyOne, exchangeRate);
// console.log(currencyTwo);


// let counter = 3;    
// function example(){
//     console.log(counter);
//     counter = counter - 1;
//     if (counter === 0) return;
//     example();
// }
// example();



// // creating an object
// var virtualPet = {
//     sleepy: true,
//     nap: function() {
//         this.sleepy = false
//     }
// }
// console.log(virtualPet.sleepy) // true
// virtualPet.nap()
// console.log(virtualPet.sleepy) // false






var globalVar = 77;

function scopeTest() {
    var localVar = 88;
    console.log(localVar);
}

console.log(scopeTest());