// let hi = () => { console.log('howdy'); }

// hi();

// let name = () => { console.log('hello, shammy!!'); }
// name();

// let hi = (name) => { console.log(`howdy ${name}`); } 
// hi('Ernest');

// let add = (a, b) => { return a + b };
// console.log(add(3, 7));


// let multiplication = (a, b) => { return a * b };
// console.log(multiplication(5, 4));


// let names = ['david', 'eddie', 'alex', 'michael'];
// names.map((name) => { console.log(`howdy ${name}`) });


// let names = ['david', 'eddie', 'alex', 'michael'];
// let i = 0;
// names.map((name) => {i++, console.log(`howdy ${name} ${i}!`) });


let names = ['david', 'eddie', 'alex', 'michael'];
var transformed = names.map((name) => { return `howdy ${name}!` });
console.log(transformed);