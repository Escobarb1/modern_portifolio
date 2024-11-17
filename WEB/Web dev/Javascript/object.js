// //creating an object with properties and their values
// var assistantManager = {
//     rangeTilesPerTurn: 3,
//     socialSkills: 30,
//     streetSmarts: 30,
//     health: 40,
//     specialAbility: "young and ambitious",
//     greeting: "Let's make some money"
// }



// var house2 = {};
// house2.rooms = 4;
// house2.color = "pink";
// house2.priceUSD = 12345;

// console.log(house2.color);



// // Object Literals and the Brackets Notation

// var house2 = {};
// house2["rooms"] = 4;
// house2['color']= "pink";
// house2["priceUSD"] = 12345;
// console.log(house2); // {rooms: 4, color: 'pink', priceUSD: 12345}


// var car = {};
// car.color = "red";
// car["color"] = "green";
// car["speed"] = 200;
// car.speed = 100;
// console.log(car); // {color: "green", speed: 100}



// var arrOfKeys = ['speed', 'altitude', 'color'];
// var drone = {
//     speed: 100,
//     altitude: 200,
//     color: "red"
// }
// for (var i = 0; i < arrOfKeys.length; i++) {
//     console.log(drone[arrOfKeys[i]])
// }



// var fruits = [];
// fruits.push("apple"); // ['apple']
// fruits.push('pear'); // ['apple', 'pear']
// fruits.pop();
// console.log(fruits); // ['apple']



// function arrayBuilder(one, two, three) {
//     var arr = [];
//     arr.push(one);
//     arr.push(two);
//     arr.push(three);
//     console.log(arr);
// }

// arrayBuilder(1,2,3);

// function arrayBuilder(one, two, three) {
//     var arr = [];
//     arr.push(one);
//     arr.push(two);
//     arr.push(three);
//     return arr;
// }

// var simpleArr = arrayBuilder('apple', 'pear', 'plum');
// console.log(simpleArr); // ['apple','pear','plum']


// var car = {};

// car.color = "red";

// //add a method to the car object so that it can be called as car.turnkey()
// car.turnKey = function() { 
//   console.log('engine running'); 
// }
// car.turnKey();




//example of adding properties and methods to an object
var car = {};
car.mileage = 98765;
car.color = "red";
console.log(car);
car.turnTheKey = function() {
    console.log("The engine is running")
}
car.lightsOn = function() {
    console.log("The lights are on.")
}
console.log(car);
car.turnTheKey();
car.lightsOn()