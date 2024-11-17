
// function greet() {
//     console.log("Hello world!");
// } 

// greet();




// function greet(user) {
//     return `Hello ${user}!!`
// } 

// let user = 'Ernest';
// let str = greet(user);
// console.log(str);




// // // function expression



// let add = function(num1, num2) {
//     return num1 + num2;
// }

// let sum = add;

// let result = sum(5, 7);
// console.log(result);




// let user = 'Ernest';

// function greet(u) {
//     let num = 5;
//     console.log(num);
//     return `Hello ${u}!`
// } 

// console.log("num value is " + num);
// let str = greet(user);
// console.log(str);





// function add(num1, num2, num3 = 1){
//     console.log(num1, num2, num3);
//     return num1 + num2 + num3;
// }

// let result = add(5, 6);
// console.log(result);





// // // // Arrow function

// let greet = () => {
//     console.log("Hello World");
//     return 1;
// }

// console.log(greet());



// let add = (num1, num2) => num1 + num2;

// let result = add(5, 6);

// console.log(result);




////////// how to add an object and a function


let laptop = {
    cpu: '19',
    ram: 16,
    brand: 'HP',

    greet: function() {
        console.log('Hello world!');
    }
}

laptop.greet();