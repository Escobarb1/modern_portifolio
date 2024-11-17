// const groceryList = ['orange juice', 'bananas', 'coffee beans', 'brown rice', 'pasta', 'coconut oil', 'plantains'];
// groceryList.shift('');
// console.log(groceryList);
// groceryList.unshift('popcorn');
// console.log(groceryList);

// groceryList.slice(1, 4);

// console.log(groceryList);

// const pastaIndex = groceryList.indexOf('pasta');
// console.log(pastaIndex);




// const vacationSpots = ['Bali', 'Paris', 'Tulum'];

// // Write your code below
// for (let i = 0; i < vacationSpots.length; i++ ){
//   console.log('I would love to visit ' + vacationSpots[i]);
// }






// const bobsFollowers = ["Jackson", "Bruno", "Rashford", "Ganarcho"];
// const tinasFollowers = ["Jackson", "Bruno", "Darwin"];
// const mutualFollowers = [];
// for (let i = 0; i < bobsFollowers.length; i++) {
//   for (let j = 0; j < tinasFollowers.length; j++) {
//     if (bobsFollowers[i] === tinasFollowers[j]) {
//       mutualFollowers.push(bobsFollowers[i]);
//     }
//   }
// };





// Write your code below
// let cupsOfSugarNeeded = 100;
// let cupsAdded = 0;
// do {
//   cupsAdded++
//   console.log(cupsAdded + ' cup was added')
// } while (cupsAdded < cupsOfSugarNeeded);








// for (let i = 0; i < 99; i++) {
//   if (i > 2 ) {
//      break;
//   }
//   console.log('Banana.');
// }

// console.log('Orange you glad I broke out the loop!');








// const rapperArray = ["Lil' Kim", "Jay-Z", "Notorious B.I.G.", "Tupac"];

// // Write your code below
// for (let i = 0; i < rapperArray.length; i++){
//    console.log(rapperArray[i]);
//     if (rapperArray[i] === 'Jay-Z'){
//     break;
//   }
// }
// console.log("And if you don't know, now you know.");







// const family = ['Dad', 'Mum', 'Stranger', 'Kelex', 'Escobar', 'Gooddy'];
// for (i = 0; i < family.length; i++) {
//   console.log(family[i]);
//   if (family[i] === 'Kelex'){
//     console.log('He is the second born');
//     break;
//   }
// }







// const checkThatTwoPlusTwoEqualsFourAMillionTimes = () => {
//   for(let i = 1; i <= 1000000; i++) {
//     if ( (2 + 2) != 4) {
//       console.log('Something has gone very wrong :( ');
//     }
//   }
// };

// // Write your code below
// const isTwoPlusTwo = checkThatTwoPlusTwoEqualsFourAMillionTimes;
// isTwoPlusTwo();
// isTwoPlusTwo();
// console.log(isTwoPlusTwo.name);








// const addTwo = num => {
//   return num + 2;
// }

// const checkConsistentOutput = (func, val) => {
//   let checkA = val + 2;
//   let checkB = func(val);
//   return checkA === checkB ? func(val) : 'inconsistent results'; 
// }

// console.log(checkConsistentOutput(addTwo, 10));























// const artists = ['Picasso', 'Kahlo', 'Matisse', 'Utamaro'];

// artists.forEach(artist => {
//   console.log(artist + ' is one of my favorite artists.');
// });

// const numbers = [1, 2, 3, 4, 5];

// const squareNumbers = numbers.map(number => {
//   return number * number;
// });

// console.log(squareNumbers);

// const things = ['desk', 'chair', 5, 'backpack', 3.14, 100];

// const onlyNumbers = things.filter(thing => {
//   return typeof thing === 'number';
// });

// console.log(onlyNumbers);



















// const fruits = ['mango', 'papaya', 'pineapple', 'apple'];

// // Iterate over fruits below
// fruits.forEach(fruit => console.log(`i want to eat ${fruit}`));












//////////// .map() method



// const animals = ['Hen', 'elephant', 'llama', 'leopard', 'ostrich', 'Whale', 'octopus', 'rabbit', 'lion', 'dog'];

// // Create the secretMessage array below
// const secretMessage = animals.map(animal => animal[0]);
// console.log(secretMessage);

// console.log(secretMessage.join(''));

// const bigNumbers = [100, 200, 300, 400, 500];

// // Create the smallNumbers array below
// const smallNumbers = bigNumbers.map(bigNumber => {
//   return bigNumber / 100;
// });
// console.log(smallNumbers);















//////////////////// .filter() method




// const randomNumbers = [375, 200, 3.14, 7, 13, 852];

// // Call .filter() on randomNumbers below
// const smallNumbers = randomNumbers.filter(randomNumber => randomNumber < 250);
// console.log(smallNumbers);

// const favoriteWords = ['nostalgia', 'hyperbole', 'fervent', 'esoteric', 'serene'];


// // Call .filter() on favoriteWords below
// const longFavoriteWords = favoriteWords.filter(favoriteWord => favoriteWord.length > 7);
// console.log(longFavoriteWords);













///////////////////////// The .findIndex() Method



// const animals = ['hippo', 'tiger', 'lion', 'seal', 'cheetah', 'monkey', 'salamander', 'elephant'];
// const foundAnimal = animals.findIndex(animal => {
//   return animal === 'elephant';
// });
// console.log(foundAnimal);

// const startsWithS = animals.findIndex(animal => {
//   return animal[0] === 's' ? true : false;
// })
// console.log(startsWithS);







///////////////////// The .reduce() Method



// const newNumbers = [1, 3, 5, 7];
// const newSum = newNumbers.reduce((accumulator, currentValue) => {
//   console.log('The value of accumulator: ', accumulator);
//   console.log('The value of currentValue: ', currentValue);
//   return accumulator + currentValue; 
// }, 10)
// console.log(newSum, 10);








/////////////////////// Iterator Documentation


// const words = ['unique', 'uncanny', 'pique', 'oxymoron', 'guise'];

// // Something is missing in the method call below

// console.log(words.some(word => {
//   return word.length < 6;
// }));

// // Use filter to create a new array
// const interestingWords = words.filter((word) => {return word.length > 5});


// // Make sure to uncomment the code below and fix the incorrect code before running it

// console.log(interestingWords.every((word) => {return word.length > 5}));












/////////////////////////////// object methods


// let retreatMessage = 'We no longer wish to conquer your planet. It is full of dogs, which we do not care for.';

// // Write your code below
// const alienShip = {
//   retreat(){
//     console.log(retreatMessage);
//   },
//   takeOff() {
//     console.log('Spim... Borp... Glix... Blastoff!');
//   }
// };
// alienShip.retreat();
// alienShip.takeOff();









// ////////////////////////////////// Nested object


// let spaceship = {
//   passengers: null,
//   telescope: {
//     yearBuilt: 2018,
//     model: "91031-XLT",
//     focalLength: 2032 
//   },
//   crew: {
//     captain: { 
//       name: 'Sandra', 
//       degree: 'Computer Engineering', 
//       encourageTeam() { console.log('We got this!') },
//      'favorite foods': ['cookies', 'cakes', 'candy', 'spinach'] }
//   },
//   engine: {
//     model: "Nimbus2000"
//   },
//   nanoelectronics: {
//     computer: {
//       terabytes: 100,
//       monitors: "HD"
//     },
//     'back-up': {
//       battery: "Lithium",
//       terabytes: 50
//     }
//   }
// }; 
// const capFave = spaceship.crew.captain['favorite foods'][0];
// spaceship.passengers = [{name: 'Space Dog'}];
// let firstPassenger = spaceship.passengers[0];











// //////////////////////////////////// Looping Through Objects


// let spaceship = {
//   crew: {
//   captain: { 
//       name: 'Lily', 
//       degree: 'Computer Engineering', 
//       cheerTeam() { console.log('You got this!') } 
//       },
//   'chief officer': { 
//       name: 'Dan', 
//       degree: 'Aerospace Engineering', 
//       agree() { console.log('I agree, captain!') } 
//       },
//   medic: { 
//       name: 'Clementine', 
//       degree: 'Physics', 
//       announce() { console.log(`Jets on!`) } },
//   translator: {
//       name: 'Shauna', 
//       degree: 'Conservation Science', 
//       powerFuel() { console.log('The tank is full!') } 
//       }
//   }
// }; 

// // Write your code below

// for (let crewMember in spaceship.crew) {
// console.log(`${crewMember}: ${spaceship.crew[crewMember].name}`)
// };

// for (let crewMember in spaceship.crew) {
// console.log(`${spaceship.crew[crewMember].name}: ${spaceship.crew[crewMember].degree}`)
// };
















const goat = {
  dietType: 'herbivore',
  makeSound() {
    console.log('baaa');
  },
  diet() {
    console.log(this.dietType);
  }
};
goat.diet();







const person = {
  _firstName: 'John',
  _lastName: 'Doe',
  get fullName() {
    if (this._firstName && this._lastName){
      return `${this._firstName} ${this._lastName}`;
    } else {
      return 'Missing a first name or a last name.';
    }
  }
}

// To call the getter method: 
person.fullName; // 'John Doe'














const robot = {
  _model: '1E78V2',
  _energyLevel: 100,
  _numOfSensors: 15,
  get numOfSensors(){
    if(typeof this._numOfSensors === 'number'){
      return this._numOfSensors;
    } else {
      return 'Sensors are currently down.'
    }
  },
  set numOfSensors(num) {
    if (typeof num === 'number' && num >= 0){
      this._numOfSensors = num;
    } else {
      console.log('Pass in a number that is greater than or equal to 0')
    }   
  } 
};

robot.numOfSensors = 100;
console.log(robot.numOfSensors);
















const robot = {
  model: '1E78V2',
  energyLevel: 100,
  functionality: {
    beep() {
      console.log('Beep Boop');
    },
    fireLaser() {
      console.log('Pew Pew');
    },
  }
};
const { functionality } = robot;
functionality.beep();