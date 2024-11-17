// // Join arrays, objects using the rest operator

// const fruits = ['apple', 'pear', 'plum']
// const berries = ['blueberry', 'strawberry']
// const fruitsAndBerries = [...fruits, ...berries] // concatenate
// console.log(fruitsAndBerries); // outputs a single array



// const colors = ['Yellow', 'Blue', 'Purple'];
// const moreColors = ['Black', 'White', 'Green'];
// const allColors = [...colors, ...moreColors];
// console.log(allColors);


// // Joining Objects

// const flying = { wings: 2 }
// const car = { wheels: 4 }
// const flyingCar = {...flying, ...car}
// console.log(flyingCar) // {wings: 2, wheels: 4}



// const school = {
//     Teacher : 10,
//     Student : 500
// };
// const schooll = {
//     Class : 15,
//     Chairs : 510
// };
// const all = {...school, ...schooll};
// console.log(all);




// // // Add new members to arrays without using the push() method

// let veggies = ['onion', 'parsley'];
// veggies = [...veggies, 'carrot', 'beetroot'];
// console.log(veggies);


// let colors = ['Yellow', 'Blue', 'Purple'];
// colors = [...colors, 'Black', 'White', 'Green'];
// console.log(colors);



// Convert a string to an array using the spread operator

// const greeting = "Hello";
// const arrayOfChars = [...greeting];
// console.log(arrayOfChars); //  ['H', 'e', 'l', 'l', 'o'];




// Copy either an object or an array into a separate one

// const car1 = {
//     speed: 200,
//     color: 'yellow'
// }
// const car2 = {...car1}

// car1.speed = 201

// console.log(car1.speed, car2.speed)



// const fruits1 = ['apples', 'pears']
// const fruits2 = [...fruits1]
// fruits1.pop()
// console.log(fruits1, "not", fruits2)


// const meal = ["soup", "steak", "ice cream"]
// let [starter] = meal;
// console.log(starter);




function count(...basket) {
    console.log(basket.length)
}

count(10, 9, 8, 7, 6);